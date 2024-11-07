
# This dir
from .conn import Conn


class Read(Conn):
    """
    Esta clase lee información del puerto serial
    """
    def __init__(self, port: str, bytes_len: int):
        super().__init__(port)

        # Longitud en bytes a leer
        self.bytes_len = bytes_len

    @Conn.check_status
    def read(self):
        """
        Esta función manda a leer cierta cantidad de bytes en la dirección asignada de la memoria
        """

        # Longitud en hexadecimal
        len_hex = hex(self.bytes_len - 1)[2:]

        # Cabecera para iniciar la lectura de la segunda memoria
        cabecera_lectura = bytes.fromhex(f'14{len_hex}40')
        self.ser.write(cabecera_lectura)  # Envía la cabecera

        # Leer los datos esperados desde el FPGA
        datos = self.ser.read(self.bytes_len)  # Num de bytes

        try:
            # Convertir de bytes a string
            string_data = datos.decode("utf-8")

        # Si no se pueden decodificar los datos, mandar el error y el status de respuesta True
        except UnicodeDecodeError as error:
            # Si no se pueden decodificar los datos, mandar el error y el status de respuesta True
            self.ser.close()
            print("Puerto cerrado por error en decodificación")

            # Devolvemos el status de la conexión y el error
            return self.status, error

        else:
            # Imprime los datos recibidos en hexadecimal
            print("Datos recibidos:", datos.hex())
            print("Datos recibidos:", string_data)

        return self.status, string_data
