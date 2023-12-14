#Kütüphanelerimiz
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


#Ana Sınıfımız
class sisilya(QMainWindow):
    #Builtin Fonksiyonumuz
    def __init__(self):
        super().__init__()
        self.TasarimFonksiyonu()
        #Sayfa Başlığımızı Ekliyoruz
        self.setWindowTitle("Bizim Birlikte ilk Projemiz")
        self.show()
    #Tasarımların Yer Alacağı Fonksiyonumuz
    def TasarimFonksiyonu(self):
        pass
# Eğer bu dosya ana dosya olarak çalıştırılıyorsa main fonksiyonunu çağır
if __name__ == "__main__":
    # Uygulama başlatılıyor
    app = QApplication(sys.argv)
    window = sisilya()
    # Stil dosyasını okuyup uygulamaya uygulanıyorpip
    with open("Resources/style/style.qss", "r") as f:
        app.setStyleSheet(f.read())
    # Uygulama başlatılıyor ve kapatılıncaya kadar çalışıyor
    sys.exit(app.exec_())