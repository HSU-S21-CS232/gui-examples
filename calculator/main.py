import sys
from PySide2.QtUiTools import QUiLoader #allows us to load .ui files

#be sure to import any widget that you want to manipulate
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton, QMessageBox 
from PySide2.QtCore import QFile, QObject

#in C++...
#class MainWindow : public QObject
class MainWindow(QObject):

    #class constructor
    def __init__(self, ui_file, parent=None):

        #call class parent (QObject) constructor
        super(MainWindow, self).__init__(parent)

        #load the UI file into Python
        #ui_file was a string, now it's a proper QT object
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)

        #always remember to close files
        ui_file.close()

        #add event listeners for UI events
        self.addEventListeners()

        #show window to the user
        self.window.show()

    def addEventListeners(self):

        #add an event listener for press of the 7 button
        sevenButton = self.window.findChild(QPushButton, 'sevenButton')
        sevenButton.clicked.connect(self.sevenButtonClicked)
        eightButton = self.window.findChild(QPushButton, 'eightButton')
        eightButton.clicked.connect(self.eightButtonClicked)

    def sevenButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'sevenButton')
        self.handlButtonClick(button)

    def eightButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'eightButton')
        self.handlButtonClick(button)

    def handlButtonClick(self, button):
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        new_text = accumulator.text() + button.text()
        accumulator.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('calculator.ui')
    sys.exit(app.exec_())