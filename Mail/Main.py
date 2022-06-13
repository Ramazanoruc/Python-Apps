import sys
from PyQt5.QtWidgets import QApplication
from Mail.Mail_gönderme import Mail_Arayuz

uygulama=QApplication(sys.argv)

mail_gonderici= Mail_Arayuz()

sys.exit(uygulama.exec_())