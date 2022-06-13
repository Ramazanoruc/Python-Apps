import sys
from PyQt5.QtWidgets import QApplication
from Hesap_makinesi.Hm.hesap_makinesi import Hm_Arayuz
uygulama=QApplication(sys.argv)
hesap_makinesi = Hm_Arayuz()

sys.exit(uygulama.exec_())