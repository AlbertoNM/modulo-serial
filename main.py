
import serial.tools.list_ports

from modules.serial.read import Read

# Obtén la lista de puertos seriales disponibles
puertos = serial.tools.list_ports.comports()

# Imprime la información de cada puerto encontrado
if puertos:
    for puerto in puertos:
        print(f"Puerto: {puerto.device} - Descripción: {puerto.description} - HWID: {puerto.hwid}\n")

port = input("Seleccione un puerto serial: ")

Read(port=port)
