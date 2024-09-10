
import os
import serial.tools.list_ports
import time


def clean_terminal():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para macOS y Linux (nombre del sistema es 'posix')
    else:
        os.system('clear')


def serial_list():
    # Obtén la lista de puertos seriales disponibles
    print("Lista de puertos disponibles")
    puertos = serial.tools.list_ports.comports()

    # Imprime la información de cada puerto encontrado
    for puerto in puertos:
        print(f"Puerto: {puerto.device} - Descripción: {puerto.description} - HWID: {puerto.hwid}")


serial_list()

while True:

    clean_terminal()
    print("##### Pruebas serial V.1 #####")

    print(
        """
        1. Lista de puertos.
        2. Conectar <PUERTO>.
        Exit.
        """
    )

    response = input("Acción: ")

    if response == "exit":
        break

    elif response == "1":
        serial_list()
        time.sleep(5)
