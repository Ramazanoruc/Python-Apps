import sys
from PyQt5.QtWidgets import QApplication
from YT.indirici import youtube_arayuz

uygulama=QApplication(sys.argv)
dowloader=youtube_arayuz()
sys.exit(uygulama.exec_())