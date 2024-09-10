
# PyQt imports
from PyQt5.QtWidgets import QMainWindow

# Components imports
from components.mainwindow import Ui_MainWindow


class MainApp(QMainWindow):
    """
    Clase principal de la interfaz de usuario
    """

    def __init__(self):
        QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    
    