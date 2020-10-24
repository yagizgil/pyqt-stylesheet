from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys,os


class ObjectScreen(QMainWindow):
    style = ""
    def __init__(self,obje, object):
        super().__init__()
        self.obje = obje
        self.object = object

        self.setUI(self.obje)

    def SetData(self, data):
        self.data = data

    def setUI(self,obj):
        if obj == "QLabel":
            self.set_wid_lbl()
            self.obje = obj
        elif obj == "QPushButton":
            self.set_wid_btn()
            self.obje = obj
        elif obj == "QLineEdit":
            self.set_wid_edit()
            self.obje = obj
        elif obj == "QTextEdit":
            self.set_wid_text()
            self.obje = obj
        elif obj == "QRadioButton":
            self.set_wid_rbtn()
            self.obje = obj
        elif obj == "QCheckBox":
            self.set_wid_chb()
            self.obje = obj
        elif obj == "QComboBox":
            self.set_wid_cmb()
            self.obje = obj
        elif obj == "QSpinBox":
            self.set_wid_spin()
            self.obje = obj
        elif obj == "QSlider":
            self.set_wid_sld()
            self.obje = obj
        elif obj == "QListWidget":
            self.set_wid_listwid()
            self.obje = obj
        elif obj == "QProgressBar":
            self.set_wid_prb()
            self.obje = obj
        elif obj == "QGroupBox":
            self.set_wid_grb()
            self.obje = obj
        elif obj == "QTabWidget":
            self.set_wid_tbw()
            self.obje = obj
        elif obj == "QDockWidget":
            self.set_wid_dcw()
            self.obje = obj
        elif obj == "QMenu":
            self.set_wid_menu()
            self.obje = obj
        elif obj == "QScrollBar":
            self.set_wid_scb()
            self.obje = obj

    def set_wid_lbl(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        l = QLabel("Label")
        self.object.SetScreenObject(l)

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_btn(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        l = QPushButton("Button")
        self.object.SetScreenObject(l)

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_edit(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        l = QLineEdit("Line edit")
        self.object.SetScreenObject(l)

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_text(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        l = QTextEdit("Text edit")
        self.object.SetScreenObject(l)

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_rbtn(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        l = QRadioButton("Radio button")
        self.object.SetScreenObject(l)

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_chb(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        l = QCheckBox("Check box")
        self.object.SetScreenObject(l)

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_cmb(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        l = QComboBox()
        l.addItems(["1","2","3","4","5"])
        self.object.SetScreenObject(l)

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_spin(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        l = QSpinBox()
        l.setMaximum(500)
        self.object.SetScreenObject(l)

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_sld(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        l = QSlider()
        l2 = QSlider(Qt.Horizontal)
        self.object.SetScreenObject([l,l2])

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v2.addWidget(l2)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_listwid(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        l = QListWidget()
        l.addItems(["Değer 1","Değer 2","Değer 3","Değer 4"])
        self.object.SetScreenObject(l)

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_prb(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        l = QProgressBar()
        l.setValue(38)
        self.object.SetScreenObject(l)

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_grb(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        l = QGroupBox("Group box")
        self.object.SetScreenObject(l)

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_tbw(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        l = QTabWidget()
        self.object.SetScreenObject(l)

        t = QWidget()
        t2 = QWidget()
        t3 = QWidget()

        l.addTab(t,"Tab 1")
        l.addTab(t2,"Tab 2")
        l.addTab(t3,"Tab 3")

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_dcw(self):
        w = QWidget()
        ww = QMainWindow()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()

        l = QDockWidget("Dock Widget")
        self.object.SetScreenObject(l)

        ww.addDockWidget(Qt.LeftDockWidgetArea, l)

        v1.addWidget(QFrame())
        v2.addWidget(ww)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_menu(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()


        qmw = QMainWindow()
        l = qmw.menuBar()
        self.object.SetScreenObject(l)

        i = l.addMenu("Menu 1")
        j = l.addMenu("Menu 2")

        i.addAction(QAction("Sub Menu 1", self))
        i.addAction(QAction("Sub Menu 2", self))

        j.addAction(QAction("Sub Menu 1", self))
        j.addAction(QAction("Sub Menu 2", self))

        v1.addWidget(QFrame())
        v2.addWidget(qmw)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)


    def set_wid_scb(self):
        w = QWidget()

        hbox = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()

        l = QScrollBar(Qt.Vertical)



        l2 = QScrollBar(Qt.Horizontal)



        self.object.SetScreenObject([l,l2])

        v1.addWidget(QFrame())
        v2.addWidget(l)
        v2.addWidget(l2)
        v3.addWidget(QFrame())

        hbox.addLayout(v1)
        hbox.addLayout(v2)
        hbox.addLayout(v3)
        w.setLayout(hbox)

        self.setCentralWidget(w)
