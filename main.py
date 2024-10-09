

import serial
import time

import serial.tools.list_ports

# Obtén la lista de puertos seriales disponibles
puertos = serial.tools.list_ports.comports()

# Imprime la información de cada puerto encontrado
if puertos:
    for puerto in puertos:
        print(f"Puerto: {puerto.device} - Descripción: {puerto.description} - HWID: {puerto.hwid}\n")

port = input("Seleccione un puerto serial: ")

# Configuración del puerto serial
ser = serial.Serial(
    port=port.strip().upper(),  # Reemplaza con el puerto serial correcto, por ejemplo 'COM3' en Windows o '/dev/ttyUSB0' en Linux.
    baudrate=9600,  # Reemplaza con la velocidad de baudios adecuada para tu FPGA
    parity=serial.PARITY_NONE, # PARITY_NONE significa que no se usará ningún bit de paridad, es decir, no se realizará verificación de errores mediante paridad.
    stopbits=serial.STOPBITS_ONE, # STOPBITS_ONE significa que se usará un solo bit de parada. El valor puede ser uno, uno y medio (STOPBITS_ONE_POINT_FIVE), o dos (STOPBITS_TWO).
    bytesize=serial.EIGHTBITS, # EIGHTBITS significa que cada byte de datos tiene 8 bits, lo cual es estándar en la mayoría de los sistemas seriales.
    timeout=1  # Tiempo de espera para la respuesta (en segundos)
)

########################################
####### Enviar petición x"5C32" ########
########################################

# Petición a enviar (5C32 en hexadecimal)
peticion = bytes.fromhex('5C32')
ser.write(peticion)

########################################
####### Respuesta del FPGA x"A6" #######
########################################

# Leer respuesta del FPGA
respuesta = ser.read(1)  # Esperamos una respuesta de 1 byte

# Verificar si la respuesta es la esperada (A6 en hexadecimal)
if respuesta == bytes.fromhex('A6'):
    print("Respuesta correcta recibida: A6")
else:
    print(f"Respuesta inesperada: {respuesta.hex()}")

########################################
############ Envío cabecera ############
########################################

# Cabecera para iniciar la lectura (C1 en hexadecimal)
cabecera_lectura = bytes.fromhex('100000')
ser.write(cabecera_lectura)  # Envía la cabecera C1

########################################
############# Espero datos #############
########################################

# Leer los datos esperados desde el FPGA
datos = ser.read(8)  # Lee 8 bytes

# Imprime los datos recibidos en hexadecimal
print("Datos recibidos:", datos.hex())


########################################
############ Envío de datos ############
########################################

# String a enviar
string_a_enviar = "Hola"

# Convertir el string a bytes hexadecimal
# Convertimos cada carácter a su equivalente en bytes
datos_a_enviar = string_a_enviar.encode('ascii')

# Envía los datos al FPGA
ser.write(datos_a_enviar)

print(f"Datos enviados: {datos_a_enviar.hex()}")

# Cerrar el puerto serial
ser.close()
