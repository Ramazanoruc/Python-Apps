from PyQt5 import QtWidgets
from YT.Arayüz import Ui_MainWindow
from pytube import YouTube

class youtube_arayuz(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton.clicked.connect(self.fdownload)


    def fdownload(self):
        url=self.lineEdit.text()
        YouTube(url).streams.first().download()
        self.lineEdit.setPlaceholderText("https://www.youtube.com/watch?v=kJQP7kiw5Fk")



