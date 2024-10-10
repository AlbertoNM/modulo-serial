
# Library
import serial

# This dir
from .conn import Conn


class Write(Conn):
    """
    Esta clase envía la trama de datos recibida al puerto serial seleccionado
    """
    def __init__(self, port: str) -> None:
        super().__init__(port)

        if self.status:
            self.write()

    def write(self) -> None:

        # Cabecera para iniciar la lectura
        cabecera_escritura = bytes.fromhex('680000')
        self.ser.write(cabecera_escritura)  # Envía la cabecera
