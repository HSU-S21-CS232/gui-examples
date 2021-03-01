import sys
from PySide2.QtUiTools import QUiLoader #allows us to load .ui files

#be sure to import any widget that you want to manipulate
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton, QMessageBox 
from PySide2.QtCore import QFile, QObject

#in C++...
#class CalculatorViewModel : public QObject
class CalculatorViewModel(QObject):

    #class constructor
    def __init__(self, ui_file, parent=None):

        #call class parent (QObject) constructor
        super(CalculatorViewModel, self).__init__(parent)

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
        self.window.findChild(QPushButton, 'zeroButton').clicked.connect(self.zeroButtonClicked)
        self.window.findChild(QPushButton, 'oneButton').clicked.connect(self.oneButtonClicked)
        self.window.findChild(QPushButton, 'twoButton').clicked.connect(self.twoButtonClicked)
        self.window.findChild(QPushButton, 'threeButton').clicked.connect(self.threeButtonClicked)
        self.window.findChild(QPushButton, 'fourButton').clicked.connect(self.fourButtonClicked)
        self.window.findChild(QPushButton, 'fiveButton').clicked.connect(self.fiveButtonClicked)
        self.window.findChild(QPushButton, 'sixButton').clicked.connect(self.sixButtonClicked)
        self.window.findChild(QPushButton, 'sevenButton').clicked.connect(self.sevenButtonClicked)
        self.window.findChild(QPushButton, 'eightButton').clicked.connect(self.eightButtonClicked)
        self.window.findChild(QPushButton, 'nineButton').clicked.connect(self.nineButtonClicked)


    def zeroButtonClicked(self):
        self.handlButtonClick(self.window.findChild(QPushButton, 'zeroButton'))

    def oneButtonClicked(self):
        button = self.window.findChild(QPushButton, 'oneButton')
        self.handlButtonClick(button)

    def twoButtonClicked(self):
        button = self.window.findChild(QPushButton, 'twoButton')
        self.handlButtonClick(button)

    def threeButtonClicked(self):
        button = self.window.findChild(QPushButton, 'threeButton')
        self.handlButtonClick(button)
    
    def fourButtonClicked(self):
        button = self.window.findChild(QPushButton, 'fourButton')
        self.handlButtonClick(button)

    def fiveButtonClicked(self):
        button = self.window.findChild(QPushButton, 'fiveButton')
        self.handlButtonClick(button)

    def sixButtonClicked(self):
        button = self.window.findChild(QPushButton, 'sixButton')
        self.handlButtonClick(button)

    def sevenButtonClicked(self):
        button = self.window.findChild(QPushButton, 'sevenButton')
        self.handlButtonClick(button)

    def eightButtonClicked(self):
        button = self.window.findChild(QPushButton, 'eightButton')
        self.handlButtonClick(button)

    def nineButtonClicked(self):
        button = self.window.findChild(QPushButton, 'nineButton')
        self.handlButtonClick(button)

    def handlButtonClick(self, button):
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        new_text = accumulator.text() + button.text()
        accumulator.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = CalculatorViewModel('calculator.ui')
    sys.exit(app.exec_())