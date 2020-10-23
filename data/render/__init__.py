import data.render.label as lbl
import data.render.pushbutton as pbtn
import data.render.lineedit as le
import data.render.textedit as te
import data.render.radiobutton as rbtn
import data.render.checkbox as chb
import data.render.combobox as cbb
import data.render.spinbox as spb
import data.render.slider as sld
import data.render.listwidget as lw
import data.render.progressbar as pb
import data.render.groupbox as gb
import data.render.tabwidget as tbw
import data.render.dockwidget as dw
import data.render.menu as mn
import data.render.scrollbar as scl


class Render():

    def __init__(self, text, type, name, data):
        self.text = text
        self.type = type
        self.name = name
        self.data = data

        self.debug()

    def debug(self):
        if self.type == "QLabel":
            lbl.Label(self.text, self.data)
        elif self.type == "QPushButton":
            pbtn.PushButton(self.text, self.data)
        elif self.type == "QLineEdit":
            le.LineEdit(self.text, self.data)
        elif self.type == "QTextEdit":
            te.TextEdit(self.text, self.data)
        elif self.type == "QRadioButton":
            rbtn.RadioButton(self.text, self.data)
        elif self.type == "QCheckBox":
            chb.CheckBox(self.text, self.data)
        elif self.type == "QComboBox":
            cbb.ComboBox(self.text, self.data)
        elif self.type == "QSpinBox":
            spb.SpinBox(self.text, self.data)
        elif self.type == "QSlider":
            sld.Slider(self.text, self.data)
        elif self.type == "QListWidget":
            lw.ListWidget(self.text, self.data)
        elif self.type == "QProgressBar":
            pb.ProgressBar(self.text, self.data)
        elif self.type == "QGroupBox":
            gb.GroupBox(self.text, self.data)
        elif self.type == "QTabWidget":
            tbw.TabWidget(self.text, self.data)
        elif self.type == "QDockWidget":
            dw.DockWidget(self.text, self.data)
        elif self.type == "QMenu":
            mn.Menu(self.text, self.data)
        elif self.type == "QScrollBar":
            scl.ScrollBar(self.text, self.data)



class ObjectRender():

    def __init__(self, object):
        self.dock_object = object

        self.render()

        self.write()

    def render(self):
        f = open("b", "w")

        try:
            f.write(self.dock_object.n_object + " = " + self.dock_object.t_object + "()")
            f.write("\n")
        except:
            pass

        try:
            f.write(self.dock_object.n_object + '.setText("' + self.dock_object.s_text.text() + '")')
            f.write("\n")
        except:
            pass

        try:
            f.write(self.dock_object.n_object + ".setValue(" + self.dock_object.s_value.text() + ")")
            f.write("\n")
        except:
            pass

        try:
            if self.t_object == "QGroupBox":
                f.write(self.dock_object.n_object + '.setTitle("' + self.dock_object.s_title.text() + '")')
            else:
                f.write(self.dock_object.n_object + '.setWindowTitle("' + self.dock_object.s_title.text() + '")')
            f.write("\n")
        except:
            pass

        try:
            f.write(self.dock_object.n_object + '.setObjectName("' + self.dock_object.s_objectname.text() + '")')
            f.write("\n")
        except:
            pass


        try:
            f.write(self.dock_object.n_object + ".setFixedSize(" + self.dock_object.s_fixedsize.text() + ")")
            f.write("\n")
        except:
            pass

        try:
            f.write(self.dock_object.n_object + '.setIcon(QIcon("' + self.dock_object.s_icon.text() + '"))')
            f.write("\n")
        except:
            pass

        try:
            f.write(self.dock_object.n_object + ".setIconSize(QSize(" + self.dock_object.s_iconsize.text() + "))")
            f.write("\n")
        except:
            pass

        try:
            f.write(self.dock_object.n_object + ".setCursor(QCursor(Qt." + self.dock_object.s_cursor.currentText() + "))")
            f.write("\n")
        except:
            pass

        try:
            f.write(self.dock_object.n_object + ".setAlignment(Qt." + self.dock_object.s_align.currentText() + ")")
            f.write("\n")
        except:
            pass

        f.close()

    def write(self):
        f = open("b", "r")
        self.dock_object.obj_code.setText(f.read())
        f.close()
