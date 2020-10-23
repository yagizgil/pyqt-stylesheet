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

        self.text = QTextEdit()
        form.addRow(self.text)

        hbox = QHBoxLayout()

        btn = QPushButton("Send/Gönder")
        btn.setCursor(QCursor(Qt.PointingHandCursor))
        btn.clicked.connect(self.send)

        hbox.addStretch()
        hbox.addStretch()
        hbox.addWidget(btn)

        form.addRow(hbox)

        bynogame = QPushButton()
        bynogame.setIcon(QIcon("image/bynogame.png"))
        bynogame.setIconSize(QSize(200,85))
        bynogame.setCursor(QCursor(Qt.PointingHandCursor))
        bynogame.setStyleSheet("QPushButton { border: none;} QPushButton:hover { border: 1px solid #2ecc71;} QPushButton::pressed { background: #2ecc71;}")
        bynogame.clicked.connect(self.bynogame)

        form.addRow(QLabel("Donation link/Bağış Linki:"))
        form.addRow(bynogame)

        self.setLayout(form)


    def send(self):
        if self.text.toPlainText() == "":
            msg = QMessageBox.warning(self, "Error/Hata", "Textedit is blank/Textedit boş!")
        else:
            mail = smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("hackerroot587@gmail.com","Ayyildiz2002")
            mail.sendmail("hackerroot587@gmail.com","ali.baydur1991@gmail.com",self.text.toPlainText())


    def bynogame(self):
        webbrowser.open("https://www.bynogame.com/destekle/c4d3r")
