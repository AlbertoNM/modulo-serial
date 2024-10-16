
import serial.tools.list_ports

from modules.serial.read import Read
from modules.serial.write import Write

# Obtén la lista de puertos seriales disponibles
puertos = serial.tools.list_ports.comports()

# Imprime la información de cada puerto encontrado
if puertos:
    for puerto in puertos:
        print(f"\nPuerto: {puerto.device}\nDescripción: {puerto.description} - HWID: {puerto.hwid}\n")
else: 
    print("No se detectan puertos")
        
port = input("\nSeleccione un puerto serial: ")

frame = input("\nEscribe lo que quieras escribir en memoria:\n-> ")

Write(port=port, frame=frame)

Read(port=port)
