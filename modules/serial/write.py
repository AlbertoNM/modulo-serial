
# Library
import serial

# This dir
from .conn import Conn


class Write(Conn):
    
    def __init__(self):
        super().__init__()
