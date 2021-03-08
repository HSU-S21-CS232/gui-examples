import sys
from enum import Enum
from PySide2.QtUiTools import QUiLoader #allows us to load .ui files

#be sure to import any widget that you want to manipulate
from PySide2.QtWidgets import QApplication, QPushButton, QGridLayout, QSizePolicy
from PySide2.QtCore import QFile, QObject
import random

class MainWindow(QObject):

    #class constructor
    def __init__(self, ui_file = 'MainWindow.ui', parent=None):

        self._num_buttons = 8
        self._num_rows = 3
        self._num_cols = 3

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

        #randomize button placement
        self.initializeGame()

        #show window to the user
        self.window.show()

    def addEventListeners(self):
        pass

    def initializeGame(self):

        #create buttons
        self.buttons = {}
        for i in range(1, self._num_buttons + 1):
            self.buttons[i] = QPushButton(str(i))
            self.buttons[i].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        #initialize spaces
        available_rows = []
        available_cols = []
        for i in range(self._num_rows):
            available_rows.append(i)
        for i in range(self._num_cols):
            available_cols.append(i)
        random.shuffle(available_rows)
        random.shuffle(available_cols)

        layout_grid = self.window.findChild(QGridLayout, 'mainWindowGridLayout')
        
        #place buttons in random spaces
        current_button = 1
        for i in range(len(available_rows)):
            for j in range(len(available_cols)):
                next_row = available_rows[i]
                next_col = available_cols[j]
                if current_button in buttons:
                    layout_grid.addWidget(self.buttons[current_button], next_row, next_col)
                    current_button += 1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())