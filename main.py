
import serial.tools.list_ports

from modules.serial.read import Read, Conn

# Obtén la lista de puertos seriales disponibles
puertos = serial.tools.list_ports.comports()

# Imprime la información de cada puerto encontrado
if puertos:
    for puerto in puertos:
        print(f"\nPuerto: {puerto.device}\nDescripción: {puerto.description} - HWID: {puerto.hwid}\n")
else: 
    print("No se detectan puertos")
        
port = input("Seleccione un puerto serial: ")

Read(port=port)
