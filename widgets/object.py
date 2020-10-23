from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
from data import CursorData as CD
from data import AlignData as AD

from data.render import ObjectRender


class Object(QDockWidget):

    def __init__(self, ):
        super().__init__()

        self.setWindowTitle("Obje")
        self.t_object = "QLabel"
        self.n_object = "label"
        self.setUI()

    def SetObject(self, object_type, object_name):
        self.t_object = object_type
        self.n_object = object_name

        self.dock_code.SetScreenObject(self.screen_object)
        self.dock_code.SetCodes(object_type, object_name)

        self.setUI()

    def SetScreenObject(self, obj):
        self.screen_object = obj


    def SetCodes(self, codes):
        self.dock_code = codes

    def setUI(self):
        self.widget = QMainWindow()

        scroll = QScrollArea()
        scroll.setWidget(self.widget)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setObjectName("scroll")

        self.setWidget(scroll)

        w = QWidget()
        self.form = QFormLayout()

        self.object_header = QLabel(self.t_object)
        self.object_header.setObjectName("object_header")

        self.form.addRow(self.object_header)

        self.set_object_code()

        self.obj_code = QTextEdit()
        self.form.addRow(self.obj_code)

        w.setLayout(self.form)
        self.widget.setCentralWidget(w)

    def set_object_code(self):
        if self.t_object == "QLabel":
            self.s_text = QLineEdit("Label")
            self.s_text.textChanged.connect(self.change_text)
            self.form.addRow(QLabel("setText: "), self.s_text)

            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)

            self.s_align = QComboBox()
            self.s_align.addItems(AD.aligns)
            self.s_align.currentIndexChanged.connect(self.change_align)
            self.form.addRow(QLabel("setAlignment: "), self.s_align)





        elif self.t_object == "QPushButton":
            self.s_text = QLineEdit("Button")
            self.s_text.textChanged.connect(self.change_text)
            self.form.addRow(QLabel("setText: "), self.s_text)

            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_icon = QLineEdit()
            self.s_icon.textChanged.connect(self.change_icon)
            self.form.addRow(QLabel("setIcon: "), self.s_icon)

            self.s_iconsize = QLineEdit()
            self.s_iconsize.textChanged.connect(self.change_icon_size)
            self.form.addRow(QLabel("setIconSize: "), self.s_iconsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)

        elif self.t_object == "QLineEdit":
            self.s_text = QLineEdit("Line Edit")
            self.s_text.textChanged.connect(self.change_text)
            self.form.addRow(QLabel("setText: "), self.s_text)

            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)

            self.s_align = QComboBox()
            self.s_align.addItems(AD.aligns)
            self.s_align.currentIndexChanged.connect(self.change_align)
            self.form.addRow(QLabel("setAlignment: "), self.s_align)

        elif self.t_object == "QTextEdit":
            self.s_text = QLineEdit("Text Edit")
            self.s_text.textChanged.connect(self.change_text)
            self.form.addRow(QLabel("setText: "), self.s_text)

            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)

            self.s_align = QComboBox()
            self.s_align.addItems(AD.aligns)
            self.s_align.currentIndexChanged.connect(self.change_align)
            self.form.addRow(QLabel("setAlignment: "), self.s_align)

        elif self.t_object == "QRadioButton":
            self.s_text = QLineEdit("Radio Button")
            self.s_text.textChanged.connect(self.change_text)
            self.form.addRow(QLabel("setText: "), self.s_text)

            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_icon = QLineEdit()
            self.s_icon.textChanged.connect(self.change_icon)
            self.form.addRow(QLabel("setIcon: "), self.s_icon)

            self.s_iconsize = QLineEdit()
            self.s_iconsize.textChanged.connect(self.change_icon_size)
            self.form.addRow(QLabel("setIconSize: "), self.s_iconsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)


        elif self.t_object == "QCheckBox":
            self.s_text = QLineEdit("Check Box")
            self.s_text.textChanged.connect(self.change_text)
            self.form.addRow(QLabel("setText: "), self.s_text)

            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_icon = QLineEdit()
            self.s_icon.textChanged.connect(self.change_icon)
            self.form.addRow(QLabel("setIcon: "), self.s_icon)

            self.s_iconsize = QLineEdit()
            self.s_iconsize.textChanged.connect(self.change_icon_size)
            self.form.addRow(QLabel("setIconSize: "), self.s_iconsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)


        elif self.t_object == "QComboBox":
            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)


        elif self.t_object == "QSpinBox":
            self.s_value = QLineEdit("0")
            self.s_value.textChanged.connect(self.change_value)
            self.form.addRow(QLabel("setValue: "), self.s_value)

            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)

            self.s_align = QComboBox()
            self.s_align.addItems(AD.aligns)
            self.s_align.currentIndexChanged.connect(self.change_align)
            self.form.addRow(QLabel("setAlignment: "), self.s_align)

        elif self.t_object == "QSlider":
            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)


        elif self.t_object == "QListWidget":
            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)


        elif self.t_object == "QProgressBar":
            self.s_value = QLineEdit("30")
            self.s_value.textChanged.connect(self.change_value)
            self.form.addRow(QLabel("setValue: "), self.s_value)

            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)

            self.s_align = QComboBox()
            self.s_align.addItems(AD.aligns)
            self.s_align.currentIndexChanged.connect(self.change_align)
            self.form.addRow(QLabel("setAlignment: "), self.s_align)

        elif self.t_object == "QGroupBox":
            self.s_title = QLineEdit("Group Box")
            self.s_title.textChanged.connect(self.change_title)
            self.form.addRow(QLabel("setWindowTitle: "), self.s_title)

            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)

            self.s_align = QComboBox()
            self.s_align.addItems(AD.aligns)
            self.s_align.currentIndexChanged.connect(self.change_align)
            self.form.addRow(QLabel("setAlignment: "), self.s_align)

        elif self.t_object == "QTabWidget":
            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_icon = QLineEdit()
            self.s_icon.textChanged.connect(self.change_icon)
            self.form.addRow(QLabel("setTabIcon: "), self.s_icon)

            self.s_iconsize = QLineEdit()
            self.s_iconsize.textChanged.connect(self.change_icon_size)
            self.form.addRow(QLabel("setIconSize: "), self.s_iconsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)


        elif self.t_object == "QDockWidget":
            self.s_title = QLineEdit("Dock Widget")
            self.s_title.textChanged.connect(self.change_title)
            self.form.addRow(QLabel("setWindowTitle: "), self.s_title)

            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)


        elif self.t_object == "QMenu":
            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            self.s_fixedsize = QLineEdit()
            self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)


        elif self.t_object == "QScrollBar":
            self.s_objectname = QLineEdit(self.n_object)
            self.s_objectname.textChanged.connect(self.change_object_name)
            self.form.addRow(QLabel("setObjectName: "), self.s_objectname)

            #self.s_fixedsize = QLineEdit()
            #self.s_fixedsize.textChanged.connect(self.change_fixed_size)
            #self.form.addRow(QLabel("setFixedSize: "), self.s_fixedsize)

            self.s_cursor = QComboBox()
            self.s_cursor.addItems(CD.cursors)
            self.s_cursor.currentIndexChanged.connect(self.change_cursor)
            self.form.addRow(QLabel("setCursor: "), self.s_cursor)





    def change_text(self):
        self.screen_object.setText(self.s_text.text())
        ObjectRender(self)

    def change_value(self):
        try:
            self.screen_object.setValue(int(self.s_value.text()))
            ObjectRender(self)
        except Exception as ex:
            print(ex)

    def change_title(self):
        if self.t_object == "QGroupBox":
            self.screen_object.setTitle(self.s_title.text())
            ObjectRender(self)
        else:
            self.screen_object.setWindowTitle(self.s_title.text())
            ObjectRender(self)

    def change_object_name(self):
        if self.t_object == "QSlider" or self.t_object == "QScrollBar":
            self.screen_object[0].setObjectName(self.s_objectname.text())
            self.screen_object[1].setObjectName(self.s_objectname.text())
            ObjectRender(self)
        else:
            self.screen_object.setObjectName(self.s_objectname.text())
            ObjectRender(self)

        self.dock_code.header.clear()
        self.dock_code.header.addItems([self.t_object, "#"+self.s_objectname.text()])

    def change_fixed_size(self):
        try:
            i= self.s_fixedsize.text().partition(",")
            if self.t_object == "QSlider" or self.t_object == "QScrollBar":
                self.screen_object[0].setFixedSize(int(i[0]), int(i[2]))
                self.screen_object[1].setFixedSize(int(i[0]), int(i[2]))
                ObjectRender(self)
            else:
                self.screen_object.setFixedSize(int(i[0]), int(i[2]))
                ObjectRender(self)
        except Exception as ex:
            print(ex)

    def change_icon(self):
        try:
            if self.t_object == "QTabWidget":
                self.screen_object.setTabIcon(0, QIcon(self.s_icon.text()))
                self.screen_object.setTabIcon(1, QIcon(self.s_icon.text()))
                ObjectRender(self)
            else:
                self.screen_object.setIcon(QIcon(self.s_icon.text()))
                ObjectRender(self)
        except Exception as ex:
            print(ex)

    def change_icon_size(self):
        try:
            i= self.s_iconsize.text().partition(",")
            self.screen_object.setIconSize(QSize(int(i[0]), int(i[2])))
            ObjectRender(self)
        except Exception as ex:
            print(ex)

    def change_cursor(self, crs):
        try:
            if self.t_object == "QSlider" or self.t_object == "QScrollBar":
                self.screen_object[0].setCursor(CD.qt_cursors[self.s_cursor.currentText()])
                self.screen_object[1].setCursor(CD.qt_cursors[self.s_cursor.currentText()])
                ObjectRender(self)
            else:
                self.screen_object.setCursor(CD.qt_cursors[self.s_cursor.currentText()])
                ObjectRender(self)
        except Exception as ex:
            print(ex)

    def change_align(self, alg):
        try:
            if self.t_object == "QSlider" or self.t_object == "QScrollBar":
                self.screen_object[0].setAlignment(AD.qt_aligns[self.s_align.currentText()])
                self.screen_object[1].setAlignment(AD.qt_aligns[self.s_align.currentText()])
                ObjectRender(self)
            else:
                self.screen_object.setAlignment(AD.qt_aligns[self.s_align.currentText()])
                ObjectRender(self)
        except Exception as ex:
            print(ex)
