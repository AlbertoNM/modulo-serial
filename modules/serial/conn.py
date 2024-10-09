import serial


class Conn:

    def __init__(
            self,
            port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
    ):

        self.status = False

        # Parámetros de la conexión
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

        # Enviar petición x"5C32" (5C32 en hexadecimal)
        request = bytes.fromhex('5C32')
        self.ser.write(request)

        # Leer respuesta del FPGA
        self.answer = self.ser.read()  # Esperamos una respuesta de 1 byte

        # Verificar si la respuesta es la esperada (A6 en hexadecimal)
        if self.answer == bytes.fromhex('A6'):
            print("Respuesta correcta recibida: A6")
            self.status = True

        else:
            print(f"Respuesta inesperada: {self.answer.hex()}")
