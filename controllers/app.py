
# PyQt imports
from PyQt5.QtWidgets import QMainWindow

# Components imports
from components.mainwindow import Ui_MainWindow

# Imports
import serial.tools.list_ports


class MainApp(QMainWindow):
    """
    Clase principal de la interfaz de usuario
    """

    def __init__(self):
        QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.fill_combo_box_with_ports()

    def fill_combo_box_with_ports(self):
        # Obtener lista de puertos seriales disponibles
        puertos = serial.tools.list_ports.comports()

        # Agregar cada puerto disponible al ComboBox
        for puerto in puertos:
            # Formato: "Puerto (Descripción)"
            item_text = f"{puerto.device} ({puerto.description})"
            self.ui.PuertoCB.addItem(item_text)
    