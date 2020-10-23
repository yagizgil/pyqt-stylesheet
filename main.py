from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

import widget as wid
import toolbar as tb


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(open("style.css","r").read())
        self.setWindowTitle("PyQt Stylesheet")
        self.setGeometry(200,200,1200,750)
        self.setWindowIcon(QIcon("image/logo.png"))
        self.setUI()
        self.show()

    def setUI(self):
        self.toolbar = tb.Toolbar(self)
        self.main = wid.Widget()

        self.toolbar.set_main(self.main)
        self.main.set_toolbar(self.toolbar)  #dock widgetlerin açıp kapamak için

        self.toolbar.SetNewsDock(self.main.tools, self.main.codes, self.main.object)

        self.toolbar.DefaultObject()

        self.setCentralWidget(self.main)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec())
