
# Library
import serial

# This dir
from .conn import Conn


class Write(Conn):
    """
    Esta clase envía la trama de datos recibida al puerto serial seleccionado
    """
    def __init__(self, port: str, frame: str):
        super().__init__(port)
        
        self.frame = frame.encode('utf-8')
        self.len_frame = hex(len(self.frame) - 1)[2:]

        if self.status:
            self.write()

    def write(self):
        
        self.hex_value()

        # Cabecera para iniciar la lectura
        cabecera_escritura = bytes.fromhex(f'6C{self.len_frame}40')
        self.ser.write(cabecera_escritura)  # Envía la cabecera
        print("Cabecera mandada")
        
        escritura = bytes.fromhex(self.frame.hex())
        self.ser.write(escritura)  # Envía la cabecera
        print("Escritura realizada")
        
    def hex_value(self):
        
        if len(self.len_frame) == 1:
            self.len_frame = f'0{self.len_frame}'
        else:
            pass
