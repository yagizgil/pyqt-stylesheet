from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

import widgets.tools as t
import widgets.screen as s
import widgets.codes as c
import widgets.object as o


class Widget(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setUI()

    def setUI(self):
        self.tools = t.Tools()
        self.tools.visibilityChanged.connect(self.toolbar_tools_on_off)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.tools)

        self.object = o.Object()
        self.object.visibilityChanged.connect(self.toolbar_object_on_off)
        self.addDockWidget(Qt.RightDockWidgetArea, self.object)

        self.scr = s.ObjectScreen("", self.object)
        self.codes = c.Codes()
        self.codes.visibilityChanged.connect(self.toolbar_code_on_off)
        self.scr.addDockWidget(Qt.BottomDockWidgetArea, self.codes)

        self.tools.SetCodes(self.codes)
        self.tools.SetScreen(self.scr)
        self.object.SetCodes(self.codes)

        self.setCentralWidget(self.scr)

    def set_toolbar(self, toolbar):
        self.toolbar = toolbar

    def toolbar_tools_on_off(self):
        if self.tools.isVisible():
            self.toolbar.tool.setIcon(QIcon("image/tools_on.png"))
            self.toolbar.bool_tools = True
        else:
            self.toolbar.tool.setIcon(QIcon("image/tools_off.png"))
            self.toolbar.bool_tools = False

    def toolbar_object_on_off(self):
        if self.object.isVisible():
            self.toolbar.object.setIcon(QIcon("image/object_on.png"))
            self.toolbar.bool_object = True
        else:
            self.toolbar.object.setIcon(QIcon("image/object_off.png"))
            self.toolbar.bool_object = False

    def toolbar_code_on_off(self):
        if self.codes.isVisible():
            self.toolbar.code.setIcon(QIcon("image/code_on.png"))
            self.toolbar.bool_code = True
        else:
            self.toolbar.code.setIcon(QIcon("image/code_off.png"))
            self.toolbar.bool_code = False
