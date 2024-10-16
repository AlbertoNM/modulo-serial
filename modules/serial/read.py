
# Library
import serial

# This dir
from .conn import Conn


class Read(Conn):
    
    def __init__(self, port):
        super().__init__(port)

        if self.status:
            self.read()

    def read(self):

        # Cabecera para iniciar la lectura de la segunda memoria
        cabecera_lectura = bytes.fromhex('140940')
        self.ser.write(cabecera_lectura)  # Envía la cabecera

        # Leer los datos esperados desde el FPGA
        datos = self.ser.read(10)  # Num de bytes

        # Imprime los datos recibidos en hexadecimal
        print("Datos recibidos:", datos.hex())
        print("Datos recibidos:", datos)
        
