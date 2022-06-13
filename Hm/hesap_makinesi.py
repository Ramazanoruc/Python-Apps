from PyQt5 import QtWidgets
from Hesap_makinesi.Hm.arayüz import Ui_MainWindow

class Hm_Arayuz(QtWidgets.QMainWindow,Ui_MainWindow):
    ilksayi=None
    ikincisayi=False
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_0.clicked.connect(self.frakambasma)
        self.pushButton_1.clicked.connect(self.frakambasma)
        self.pushButton_2.clicked.connect(self.frakambasma)
        self.pushButton_3.clicked.connect(self.frakambasma)
        self.pushButton_4.clicked.connect(self.frakambasma)
        self.pushButton_5.clicked.connect(self.frakambasma)
        self.pushButton_6.clicked.connect(self.frakambasma)
        self.pushButton_7.clicked.connect(self.frakambasma)
        self.pushButton_8.clicked.connect(self.frakambasma)
        self.pushButton_9.clicked.connect(self.frakambasma)
        self.pushButton_nokta.clicked.connect(self.fondalik)
        self.pushButton_nokta.setCheckable(True)
        self.pushButton_silme.clicked.connect(self.ftemizle)

        self.pushButton_isaret.clicked.connect(self.fisareyuzde)

        self.pushButton_toplama.clicked.connect(self.faritmetik)
        self.pushButton_cikarma.clicked.connect(self.faritmetik)
        self.pushButton_carpma.clicked.connect(self.faritmetik)
        self.pushButton_bolme.clicked.connect(self.faritmetik)

        self.pushButton_toplama.setCheckable(True) #Butonlara tekrar basamamak için Kontrol ediyoruz
        self.pushButton_cikarma.setCheckable(True)
        self.pushButton_carpma.setCheckable(True)
        self.pushButton_bolme.setCheckable(True)

        self.pushButton_esit.clicked.connect(self.fsonuc)
        self.pushButton_esit.setCheckable(True)



    def frakambasma(self):
        buton=self.sender() #Fonksiyonu Çağıran butonu belirtir
        if ((self.ikincisayi)and(self.pushButton_esit.isChecked())):
            self.label.setText(format(float(buton.text()),'.15g'))
            self.ikincisayi=True

        elif((self.pushButton_toplama.isChecked()or self.pushButton_cikarma.isChecked()or self.pushButton_carpma.isChecked()or self.pushButton_bolme.isChecked())and (not self.ikincisayi)):
            self.label.setText(format(float(buton.text()), '.15g'))#Butonları Labela atıyor(Format ile bastaki 0 ı sildik)
            self.ikincisayi=True
        else:
            if (('.' in self.label.text())and buton.text()=="0"):
                self.label.setText(format(float(self.label.text() + buton.text()), '.15'))
            else:
                self.label.setText(format(float(self.label.text() + buton.text()), '.15g'))

        print(buton.text())


    def fondalik(self):
        self.label.setText(self.label.text()+".")
        buton=self.sender()
        buton.setChecked(True)
        #BURADA NOKTANIN 2 KERE BASILMASI İLE İLGİLİ İŞLEMLERİ YAPACAKSIN!

    def fisareyuzde(self):
        buton=self.sender()
        deger=float(self.label.text())

        if buton.text()=="+-":
            deger=deger*-1

        self.label.setText(str(deger))

    def faritmetik(self):
        buton=self.sender()#Hangi butona tıkladığını öğreniyoruz
        self.ilksayi=float(self.label.text())
        buton.setChecked(True)
        print(self.ilksayi)
    def fsonuc(self):
        ikincisayi=float(self.label.text())

        if self.pushButton_toplama.isChecked():
            yenideger=self.ilksayi+ikincisayi
            self.label.setText(format(float(yenideger), '.15g'))
            self.pushButton_toplama.setChecked(False)
        elif self.pushButton_cikarma.isChecked():
            yenideger=self.ilksayi-ikincisayi
            self.label.setText(format(float(yenideger), '.15g'))
            self.pushButton_toplama.setChecked(False)
        elif self.pushButton_carpma.isChecked():
            yenideger=self.ilksayi*ikincisayi
            self.label.setText(format(float(yenideger), '.15g'))
            self.pushButton_toplama.setChecked(False)
        elif self.pushButton_bolme.isChecked():
            yenideger=self.ilksayi/ikincisayi
            self.label.setText(format(float(yenideger), '.15g'))
            self.pushButton_toplama.setChecked(False)

        self.ilksayi=yenideger
        self.pushButton_esit.setChecked(True)

    def ftemizle(self):
        self.ilksayi=0
        self.ikincisayi=False
        self.label.setText("0")
        self.pushButton_toplama.setChecked(False)
        self.pushButton_cikarma.setChecked(False)
        self.pushButton_carpma.setChecked(False)
        self.pushButton_bolme.setChecked(False)



