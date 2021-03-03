import sys
from enum import Enum
from PySide2.QtUiTools import QUiLoader #allows us to load .ui files

#be sure to import any widget that you want to manipulate
from PySide2.QtWidgets import QApplication
from calculatorViewModel import CalculatorViewModel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calcWindow = CalculatorViewModel()
    sys.exit(app.exec_())