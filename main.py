#Kütüphanelerimiz
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


#Ana Sınıfımız
class sisilya(QWidget):

def main():
    # Uygulama başlatılıyor
    app = QApplication(sys.argv)

    # Stil dosyasını okuyup uygulamaya uygulanıyorpip
    with open("Resources/style/style.qss", "r") as f:
        app.setStyleSheet(f.read())

    # Uygulama başlatılıyor ve kapatılıncaya kadar çalışıyor
    sys.exit(app.exec_())

# Eğer bu dosya ana dosya olarak çalıştırılıyorsa main fonksiyonunu çağır
if __name__ == "__main__":
    main()