# This dir
from .conn import Conn


class Write(Conn):
    """
    Esta clase envía la trama de datos recibida al puerto serial seleccionado
    """

    def __init__(self, port: str, frame: str):

        # Puerto que se maneja
        self.port = port
        super().__init__(self.port)  # Iniciamos el constructor

        # Trama de datos a escribir transformada a bytes
        self.frame = frame.encode()

        # valor hexadecimal de la longitud de la trama de datos
        self.len_frame = hex(len(self.frame) - 1)[2:]

        # Función que transforma en dos índices la cantidad de bytes a escribir
        self.hex_value()

    @Conn.check_status
    def write(self):
        """
        Esta función escribe cierta cantidad de bytes en la dirección asignada de la memoria
        """

        # Cabecera para iniciar la lectura
        cabecera_escritura = bytes.fromhex(f'6C{self.len_frame}40')
        self.ser.write(cabecera_escritura)  # Envía la cabecera
        print("Cabecera mandada")

        # Envío de la información a la memoria
        escritura = bytes.fromhex(self.frame.hex())
        self.ser.write(escritura)  # Envía la cabecera
        print("Escritura realizada")

        # Leer estado del FPGA
        state = self.ser.read()

        # Casos
        match state:

            case b'\x0C':

                # Completamos la secuencia y mandamos True
                return True, ""

            case b'\xE1':

                # Volvemos a iniciar el constructor
                super().__init__(self.port)
                self.write()  # Reiniciamos el proceso

            case _:

                # Generamos un bloque basura de 256 bytes de largo de ceros
                trash_block = b'0' * 256
                self.ser.write(trash_block)  # Mandamos el bloque

                # Leemos la respuesta del serial
                answer = self.ser.read()

                # Si la respuesta es 0C volvemos a realizar la secuencia
                if answer == bytes.fromhex('0C'):
                    self.write()

                # Si la respuesta es E1
                if answer == bytes.fromhex('E1'):
                    # Volvemos a iniciar el constructor
                    super().__init__(self.port)
                    self.write()  # Reiniciamos el proceso

                # Si no hay respuesta detenemos el procedo
                else:
                    return False, ""

    def hex_value(self):
        """
        Esta función transforma en dos índices el valor hexadecimal de la longitud de bytes a escribir
        """

        if len(self.len_frame) == 1:
            self.len_frame = f'0{self.len_frame}'
        else:
            pass
