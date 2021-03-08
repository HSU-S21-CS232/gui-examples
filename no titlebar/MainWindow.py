import sys
from enum import Enum
from PySide2.QtUiTools import QUiLoader #allows us to load .ui files

#be sure to import any widget that you want to manipulate
from PySide2.QtWidgets import QApplication, QPushButton, QGridLayout, QSizePolicy
from PySide2.QtCore import QFile, QObject, Qt
import random

class MainWindow(QObject):

    #class constructor
    def __init__(self, ui_file = 'MainWindow.ui', parent=None):

        #call class parent (QObject) constructor
        super(MainWindow, self).__init__(parent)

        #load the UI file into Python
        #ui_file was a string, now it's a proper QT object
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        
        self.window.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

        #always remember to close files
        ui_file.close()

        #add event listeners for UI events
        self.addEventListeners()

        #show window to the user
        self.window.show()

    def addEventListeners(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())