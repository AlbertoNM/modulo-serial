
from __future__ import annotations
from typing import Tuple

import serial
from serial.serialutil import SerialException


class Conn:
    """
    Clase padre que corrobora la conexión con el puerto serial
    """

    def __init__(
        self,
        port,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    ):

        # Sin estado por default
        self.status = False

        # Parámetros de la conexión
        try:
            # Configuración del puerto serial
            self.ser = serial.Serial(
                # Reemplaza con el puerto serial correcto, por ejemplo 'COM3' en Windows o '/dev/ttyUSB0' en Linux.
                port=port.strip().upper(),
                # Reemplaza con la velocidad de baudios adecuada para tu FPGA
                baudrate=baudrate,
                # PARITY_NONE significa que no se usará ningún bit de paridad, es decir, no se realizará verificación de
                # errores mediante paridad.
                parity=parity,
                # STOPBITS_ONE significa que se usará un solo bit de parada. El valor puede ser uno, uno y medio
                # (STOPBITS_ONE_POINT_FIVE), o dos (STOPBITS_TWO).
                stopbits=stopbits,
                # EIGHTBITS significa que cada byte de datos tiene 8 bits, lo cual es estándar en la mayoría de los
                # sistemas seriales.
                bytesize=bytesize,
                # Tiempo de espera para la respuesta (en segundos)
                timeout=timeout
            )

        except SerialException:
            # No hacer nada si existe un serial error
            print("Error en conexión")

        else:
            # Enviar petición x"5C32" (5C32 en hexadecimal)
            request = bytes.fromhex('5C32')
            self.ser.write(request)

            # Leer respuesta del FPGA
            answer = self.ser.read()  # Esperamos una respuesta de 1 byte

            # Casos
            match answer:

                # Si responde A6
                case b'\xA6':

                    print(f"Respuesta correcta recibida: {answer.hex()}")
                    self.status = True  # Validamos la conexión

                # Cualquier otra cosa
                case _:
                    print(f"Respuesta inesperada: {answer.hex()}")

    @staticmethod
    def check_status(func):

        def wrapper(self):

            print("Checando status")

            if self.status:
                print("Estatus correcto: A6")
                resultado = func(self)
                return resultado
            else:
                print("Estatus incorrecto")
                return False, ""

        return wrapper

    @check_status
    def check_id(self) -> tuple[bool, UnicodeDecodeError] | tuple[bool, str]:
        """
        Esta función hace una petición al radio de leer su ID, devolviendo el id del radio y un status de True.
        @return: tuple[UnicodeDecodeError, bool] | tuple[str, bool]
        """

        # Cabecera para iniciar la lectura de la segunda memoria, específicamente en el ID
        cabecera_lectura = bytes.fromhex(f'143440')
        self.ser.write(cabecera_lectura)  # Envía la cabecera

        # Leer los datos esperados desde el FPGA
        datos = self.ser.read(53)  # Num de bytes

        try:
            # Convertir de bytes a string
            string_data = datos.decode()

        except UnicodeDecodeError as error:
            # Si no se pueden decodificar los datos, mandar el error y el status de respuesta True
            self.ser.close()
            print("Puerto cerrado por error en decodificación")

            # Devolvemos el status de la conexión y el error
            return self.status, error

        else:
            # Capturamos solo la parte del ID del radio
            id_radio = string_data[38:44]

            # Devuelve los datos leído del serial y el status
            return self.status, id_radio

    def __del__(self):

        try:
            # Cerramos el puerto al finalizar la variable
            self.ser.close()
            print("Puerto cerrado")

        except AttributeError:
            # Si no se instanció ninguna variable, mandamos mensaje de error:
            print("No se pudo conectar al puerto")
