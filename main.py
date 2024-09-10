
# PyQt imports
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

# Controller import
from controllers.app import MainApp

# Imports
import sys

if __name__ == "__main__":

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # enable high dpi scaling
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # use high dpi icons
    app = QApplication([])

    ex = MainApp()
    ex.show()

    sys.exit(app.exec_())