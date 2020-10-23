from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

from data import Data
from widgets.about import About

class Toolbar():
    bool_tools = True
    bool_code = True
    bool_object = True

    def __init__(self,me):
        self.me = me
        self.setUI()

    def DefaultObject(self):
        NewObject(self.dock_tool, self.dock_object).DefaultObject()

    def SetNewsDock(self, tools, code, object):
        self.dock_tool = tools
        self.dock_code = code
        self.dock_object = object

    def setUI(self):
        menu = self.me.addToolBar("menu")

        new = QAction(QIcon("image/add.png"), "new", self.me)
        new.triggered.connect(self.new)
        menu.addAction(new)

        about = QAction(QIcon("image/about.png"), "about", self.me)
        about.triggered.connect(self.about)
        menu.addAction(about)

        dock = QToolBar()
        self.me.addToolBar(Qt.BottomToolBarArea , dock)

        self.tool = QAction(QIcon("image/tools_on.png"), "tools", self.me)
        self.tool.triggered.connect(self.tools_a)
        dock.addAction(self.tool)

        self.code = QAction(QIcon("image/code_on.png"), "code", self.me)
        self.code.triggered.connect(self.code_a)
        dock.addAction(self.code)

        self.object = QAction(QIcon("image/object_on.png"), "object", self.me)
        self.object.triggered.connect(self.object_a)
        dock.addAction(self.object)

    def tools_a(self):
        if self.bool_tools == True:
            self.tool.setIcon(QIcon("image/tools_off.png"))
            self.bool_tools = False
            self.dock_tool.setVisible(False)

        else:
            self.tool.setIcon(QIcon("image/tools_on.png"))
            self.bool_tools = True
            self.dock_tool.setVisible(True)

    def code_a(self):
        if self.bool_code == True:
            self.code.setIcon(QIcon("image/code_off.png"))
            self.bool_code = False
            self.dock_code.setVisible(False)

        else:
            self.code.setIcon(QIcon("image/code_on.png"))
            self.bool_code = True
            self.dock_code.setVisible(True)


    def object_a(self):
        if self.bool_object == True:
            self.object.setIcon(QIcon("image/object_off.png"))
            self.bool_object = False
            self.dock_object.setVisible(False)

        else:
            self.object.setIcon(QIcon("image/object_on.png"))
            self.bool_object = True
            self.dock_object.setVisible(True)

    def new(self):
        nobj = NewObject(self.dock_tool, self.dock_object)
        nobj.exec()


    def about(self):
        About()


    def set_main(self, main_widget):
        self.main_widget = main_widget


class NewObject(QDialog):
    obje = ""
    def __init__(self, tools, object):
        super().__init__()
        self.tool = tools
        self.object = object

        style = """#obje {
                      width: 200px;
                      height: 35px;
                      margin-top: 10px;
                      border-left: 12px solid #44bd32;
                      opacity: 0;
                    }
                    #obje::unchecked {
                      border: 1px solid #2C3A47;
                      border-left: 12px solid #44bd32;
                    }
                    #obje:checked {
                      background: green;
                      color: white;
                    }
                    #obje::indicator {
                      border: none;
                      width: 0px;
                      height: 0px;
                    }
                    #scroll {
                      min-width: 260px;
                      max-width: 260px;
                    }
                    QTabWidget, QDockWidget {
                      height: 200px;
                    }
                    #open_btn {
                       border-width: 1px;
                       border-style: solid;
                       border-color: #1289A7;
                       border-radius: 25;
                    }
                    #open_btn:hover {
                       background: #12CBC4;
                    }
                    #open_btn::pressed {
                    }
                    QLineEdit {
                       color: #2C3A47;
                       height: 32px;
                       font-size: 15px;
                       background: transparent;
                       border-width: 1px;
                       border-style: solid;
                       border-color: transparent;
                    }
                    QLineEdit:hover {
                       color: #2c2c54;
                       border-width: 1px;
                       border-style: solid;
                       border-color: #182C61;
                    }
                    """
        self.setWindowTitle("Yeni Obje")
        self.setStyleSheet(style)
        self.setMaximumSize(QSize(800,400))
        self.setMinimumSize(QSize(800,400))
        self.setWindowIcon(QIcon("image/logo.png"))
        self.setUI()

    def setUI(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        obj_frame = QFrame()
        screen_frame = QFrame()

        #--------- objeler ----------
        form = QFormLayout()

        label = QRadioButton("Label -- QLabel")
        pushbutton = QRadioButton("Button -- QPushButton")
        lineedit = QRadioButton("Line Edit -- QLineEdit")
        textedit = QRadioButton("Text Edit -- QTextEdit")
        radiobutton = QRadioButton("Radio Button -- QRadioButton")
        checkbox = QRadioButton("Check Box -- QCheckBox")
        combobox = QRadioButton("Combo Box -- QComboBox")
        spinbox = QRadioButton("Spin Box -- QSpinBox")
        slider = QRadioButton("Slider -- QSlider")
        listwid = QRadioButton("List View -- QListWidget")
        progressbar = QRadioButton("Progress Bar -- QProgressBar")
        groupbox = QRadioButton("Group Box -- QGroupBox")
        tabwidget = QRadioButton("Tab Widget -- QTabWidget")
        dockwidget = QRadioButton("Dock Widget -- QDockWidget")
        menu = QRadioButton("Menu Bar -- QMenu")
        scrollbar = QRadioButton("Scroll Bar -- QScrollBar")

        label.setObjectName("obje")
        pushbutton.setObjectName("obje")
        lineedit.setObjectName("obje")
        textedit.setObjectName("obje")
        radiobutton.setObjectName("obje")
        checkbox.setObjectName("obje")
        combobox.setObjectName("obje")
        spinbox.setObjectName("obje")
        slider.setObjectName("obje")
        listwid.setObjectName("obje")
        progressbar.setObjectName("obje")
        groupbox.setObjectName("obje")
        tabwidget.setObjectName("obje")
        dockwidget.setObjectName("obje")
        menu.setObjectName("obje")
        scrollbar.setObjectName("obje")


        label.clicked.connect(self.set_lbl)
        pushbutton.clicked.connect(self.set_pushbtn)
        lineedit.clicked.connect(self.set_lineedit)
        textedit.clicked.connect(self.set_textedit)
        radiobutton.clicked.connect(self.set_rbtn)
        checkbox.clicked.connect(self.set_chb)
        combobox.clicked.connect(self.set_cmb)
        spinbox.clicked.connect(self.set_spb)
        slider.clicked.connect(self.set_sld)
        listwid.clicked.connect(self.set_listwid)
        progressbar.clicked.connect(self.set_prb)
        groupbox.clicked.connect(self.set_grb)
        tabwidget.clicked.connect(self.set_tbw)
        dockwidget.clicked.connect(self.set_dcw)
        menu.clicked.connect(self.set_menu)
        scrollbar.clicked.connect(self.set_scb)


        form.addRow(label)
        form.addRow(pushbutton)
        form.addRow(lineedit)
        form.addRow(textedit)
        form.addRow(radiobutton)
        form.addRow(checkbox)
        form.addRow(combobox)
        form.addRow(spinbox)
        form.addRow(slider)
        form.addRow(listwid)
        form.addRow(progressbar)
        form.addRow(groupbox)
        form.addRow(tabwidget)
        form.addRow(dockwidget)
        form.addRow(menu)
        form.addRow(scrollbar)
        obj_frame.setLayout(form)

        scroll = QScrollArea()
        scroll.setWidget(obj_frame)
        scroll.setWidgetResizable(True)
        scroll.setObjectName("scroll")

        #------------ objeler end --------

        #------------- obje görünüm ---------------
        screen_main_vbox = QVBoxLayout()
        screen_hbox = QHBoxLayout()
        group = QGroupBox()
        self.frm = QFormLayout()
        self.frm.setObjectName("frm")
        group.setLayout(self.frm)
        screen_hbox.addWidget(group)

        btns_hbox = QHBoxLayout()


        self.name = QLineEdit()
        self.name.setPlaceholderText("Obje Adı")

        open_btn = QPushButton("")
        open_btn.setIcon(QIcon("image/create.png"))
        open_btn.setCursor(QCursor(Qt.PointingHandCursor))
        open_btn.setObjectName("open_btn")
        open_btn.setFixedSize(50,50)
        open_btn.setIconSize(QSize(30,30))
        open_btn.clicked.connect(self.open)


        btns_hbox.addWidget(self.name)
        btns_hbox.addWidget(open_btn)

        screen_main_vbox.addLayout(screen_hbox)
        screen_main_vbox.addLayout(btns_hbox)
        screen_frame.setLayout(screen_main_vbox)


        # ------------ obje end ------------

        sp = QSplitter()
        sp.addWidget(scroll)
        sp.addWidget(screen_frame)

        hbox.addWidget(sp)

        hbox.addLayout(vbox)
        self.setLayout(hbox)

    def DefaultObject(self):
        self.obje = "QLabel"
        self.name.setText("label")
        self.open()

    def set_lbl(self):
        self.obje = "QLabel"
        for i in range(5):
            self.frm.removeRow(i)
        l = QLabel("Label")
        l.setAlignment(Qt.AlignCenter)
        self.frm.addRow(l)

    def set_pushbtn(self):
        self.obje = "QPushButton"
        for i in range(5):
            self.frm.removeRow(i)
        l = QPushButton("Button")
        self.frm.addRow(l)

    def set_lineedit(self):
        self.obje = "QLineEdit"
        for i in range(5):
            self.frm.removeRow(i)
        l = QLineEdit("Line Edit")
        self.frm.addRow(l)

    def set_textedit(self):
        self.obje = "QTextEdit"
        for i in range(5):
            self.frm.removeRow(i)
        l = QTextEdit("Text Edit")
        self.frm.addRow(l)

    def set_rbtn(self):
        self.obje = "QRadioButton"
        for i in range(5):
            self.frm.removeRow(i)
        l = QRadioButton("Radio Button")
        self.frm.addRow(l)

    def set_chb(self):
        self.obje = "QCheckBox"
        for i in range(5):
            self.frm.removeRow(i)
        l = QCheckBox("Check Box")
        self.frm.addRow(l)

    def set_cmb(self):
        self.obje = "QComboBox"
        for i in range(5):
            self.frm.removeRow(i)
        l = QComboBox()
        l.addItems(["1","2","3","4"])
        self.frm.addRow(l)

    def set_spb(self):
        self.obje = "QSpinBox"
        for i in range(5):
            self.frm.removeRow(i)
        l = QSpinBox()
        self.frm.addRow(l)

    def set_sld(self):
        self.obje = "QSlider"
        for i in range(5):
            self.frm.removeRow(i)
        l = QSlider()
        self.frm.addRow(l)

    def set_listwid(self):
        self.obje = "QListWidget"
        for i in range(5):
            self.frm.removeRow(i)
        l = QListWidget()
        for i in range(10):
            item = QListWidgetItem("Item " + str(i))
            l.addItem(item)
        self.frm.addRow(l)

    def set_prb(self):
        self.obje = "QProgressBar"
        for i in range(5):
            self.frm.removeRow(i)
        l = QProgressBar()
        l.setValue(38)
        self.frm.addRow(l)

    def set_grb(self):
        self.obje = "QGroupBox"
        for i in range(5):
            self.frm.removeRow(i)
        l = QGroupBox("Group Box")
        l.setFixedHeight(200)
        self.frm.addRow(l)

    def set_tbw(self):
        self.obje = "QTabWidget"
        for i in range(5):
            self.frm.removeRow(i)
        l = QTabWidget()
        w1 = QWidget()
        w2 = QWidget()
        l.addTab(w1, "Tab 1")
        l.addTab(w2, "Tab 2")
        self.frm.addRow(l)

    def set_dcw(self):
        self.obje = "QDockWidget"
        for i in range(5):
            self.frm.removeRow(i)
        l = QDockWidget("Dock Widget")
        self.frm.addRow(l)

    def set_menu(self):
        self.obje = "QMenu"
        for i in range(5):
            self.frm.removeRow(i)
        qmw = QMainWindow()
        l = qmw.menuBar()

        i = l.addMenu("Menu 1")
        j = l.addMenu("Menu 2")

        i.addAction(QAction("Sub Menu 1", self))
        i.addAction(QAction("Sub Menu 2", self))

        j.addAction(QAction("Sub Menu 1", self))
        j.addAction(QAction("Sub Menu 2", self))

        self.frm.addRow(qmw)

    def set_scb(self):
        self.obje = "QScrollBar"
        for i in range(5):
            self.frm.removeRow(i)
        l = QScrollBar(Qt.Horizontal)
        l.setFixedHeight(20)
        self.frm.addRow(l)


    def open(self):
        if self.name.text() == "":
            msg = QMessageBox.warning(self, "Hata", "Obje ismi boş!")
            try:
                msg.setIcon(QMessageBox.Warning)
            except:
                pass
        else:
            self.tool.SetObject(self.obje, self.name.text())
            self.object.SetObject(self.obje, self.name.text())

            data = Data()

            self.tool.SetData(data)
            self.close()
