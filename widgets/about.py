from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import smtplib
import webbrowser



class About(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("İletişim")
        self.setMaximumSize(QSize(650,380))
        self.setMinimumSize(QSize(650,380))
        self.setWindowIcon(QIcon("image/logo.png"))

        self.setUI()
        self.exec()

    def setUI(self):
        form = QFormLayout()

        form.addRow(QLabel("Uygulamadaki eksiklikler için önerileriniz ve karşılaştığınız hatalar için iletişime geçin."))
        form.addRow(QLabel("Cevap almak için e-mail adresinizi yazmayı unutmayın."))
        form.addRow(QLabel("Contact us for your suggestions for shortcomings in the application and for errors you encounter."))
        form.addRow(QLabel("Do not forget to write your e-mail address to get a reply."))

        frm = QFrame()
        frm.setFrameShape(QFrame.HLine)
        form.addRow(frm)


        self.mail = QLineEdit()
        form.addRow(QLabel("Mail: "), self.mail)

        self.passwd = QLineEdit()
        self.passwd.setEchoMode(QLineEdit.Password)
        form.addRow(QLabel("Parola / Password: "), self.passwd)

        self.text = QTextEdit()
        form.addRow(self.text)

        form.addRow(QLabel("To: ali.baydur1991@gmail.com"))

        hbox = QHBoxLayout()

        btn = QPushButton("Send/Gönder")
        btn.setCursor(QCursor(Qt.PointingHandCursor))
        btn.clicked.connect(self.send)

        hbox.addStretch()
        hbox.addStretch()
        hbox.addWidget(btn)

        form.addRow(hbox)

        self.setLayout(form)


    def send(self):
        if self.text.toPlainText() == "":
            msg = QMessageBox.warning(self, "Error/Hata", "Textedit is blank/Textedit boş!")
        else:
            try:
                mail = smtplib.SMTP("smtp.gmail.com",587)
                mail.ehlo()
                mail.starttls()
                mail.login(self.mail.text(), self.passwd.text())
                mail.sendmail(sel.mail.text(),"ali.baydur1991@gmail.com",self.text.toPlainText())
            except Exception as ex:
                msg = QMessageBox.warning(self, "Error/Hata", str(ex))
