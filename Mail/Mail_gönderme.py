from PyQt5 import QtWidgets
from Mail.Mail_Arayuz import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox
#Mail Göndermek için Gerekli Kütüphaneler
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

class Mail_Arayuz(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton.clicked.connect(self.gonder)


    def gonder(self):
        mesaj=MIMEMultipart()

        mesaj["From"]=self.lineEdit_gonderici.text()
        mesaj["To"]=self.lineEdit_alan_adres.text()
        mesaj["Subject"]=self.lineEdit_mail_konu.text()


        content=self.lineEdit_Konu.text()


        mesaj_govdesi=MIMEText(content,"plain")
        mesaj.attach(mesaj_govdesi)

        try:
           if(self.lineEdit_gonderici.text().endswith("@gmail.com")):
               mail = smtplib.SMTP("Smtp.gmail.com", 587)
               mail.ehlo()
               mail.starttls()
               mail.login(self.lineEdit_gonderici.text(), self.lineEdit_gonderici_sifre.text())
               mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

           elif (self.lineEdit_gonderici.text().endswith("@outlook.com") or self.lineEdit_gonderici.text().endswith("@hotmail.com")):
               mail = smtplib.SMTP("smtp.outlook.com", 587)
               mail.ehlo()
               mail.starttls()
               mail.login(self.lineEdit_gonderici.text(), self.lineEdit_gonderici_sifre.text())
               mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
           if (self.lineEdit_gonderici.text().endswith("@yandex.com")):
               mail = smtplib.SMTP("smtp.yandex.com", 587)
               mail.ehlo()
               mail.starttls()
               mail.login(self.lineEdit_gonderici.text(), self.lineEdit_gonderici_sifre.text())
               mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())


        except:
            sys.stderr.write("Bir sorun oluştu")
            sys.stderr.flush()
        QMessageBox.information(self,"Bilgi Mesajı","Mailiniz Başarı ile Gönderildi",QMessageBox.Ok)




