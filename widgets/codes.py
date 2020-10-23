from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

import data.render as rndr

class Codes(QDockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kod")
        self.setUI()

    def ReCode(self):
        try:
            self.object_name = self.object.objectName()
        except Exception as ex:
            self.object_name = self.object[0].objectName()
        rndr.Render(self.header.currentText(), self.object_type, self.object_name, self.data)
        self.css_code.setText(open("a", "r").read())


    def SetCodes(self, object_type, object_name):
        self.object_type = object_type
        self.object_name = object_name

        try:
            self.object.setObjectName(self.object_name)
        except Exception as ex:
            self.object[0].setObjectName(self.object_name)
            self.object[1].setObjectName(self.object_name)

        self.css_code.clear()
        self.header.clear()
        if object_type == "QMenu":
            self.header.addItems(["QMenuBar", "#" + object_name])
        else:
            self.header.addItems([object_type, "#" + object_name])

    def SetData(self, data):
        self.data = data

    def SetScreenObject(self, screen):
        self.object = screen


    def setUI(self):
        w = QWidget()
        layout = QHBoxLayout()

        self.css_code = QTextEdit()
        self.css_code.setObjectName("css_code")
        self.css_code.setReadOnly(False)
        self.css_code.textChanged.connect(self.set_css)

        layout.addWidget(self.css_code)

        vbox = QVBoxLayout()

        self.header = QComboBox()
        self.header.setObjectName("header")
        self.header.currentIndexChanged.connect(self.change_combo)

        vbox.addWidget(self.header)
        vbox.addStretch()

        save = QPushButton()
        save.setObjectName("save")
        save.setIcon(QIcon("image/save.png"))
        save.setFixedSize(65,65)
        save.setIconSize(QSize(30,30))
        save.setCursor(QCursor(Qt.PointingHandCursor))
        save.clicked.connect(self.file_save)
        vbox.addWidget(save)

        copy = QPushButton("Kopyala")
        copy.setObjectName("copy")
        copy.setCursor(QCursor(Qt.PointingHandCursor))
        #vbox.addWidget(copy)

        layout.addLayout(vbox)
        w.setLayout(layout)
        self.setWidget(w)

    def set_css(self):
        try:
            self.object.setStyleSheet(self.css_code.toPlainText())
        except:
            try:
                self.object[0].setStyleSheet(self.css_code.toPlainText())
                self.object[1].setStyleSheet(self.css_code.toPlainText())
            except:
                pass

    def change_combo(self):
        try:
            self.ReCode()
        except:
            pass


    def file_save(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')
        try:
            file = open(name[0],'w')
            text = self.css_code.toPlainText()
            file.write(text)
            file.close()
        except:
            pass
