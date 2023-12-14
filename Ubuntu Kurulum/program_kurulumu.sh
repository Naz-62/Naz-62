#!/bin/bash
echo "Sisilya Sistem Güncelleniyor... Şifre istediğinde Şifreni gir ve E/h yazdığında da sürekli E bas"

sudo apt update

echo "Sisilya Sistem Güncellenmeye başladı..."

sudo apt upgrade

echo "PyCharm Kuruluyor... "

sudo snap install pycharm-community --classic

echo "Visual Studio Code  Kuruluyor... "

sudo snap install code --classic

echo "jupyter notebook  Kuruluyor... "

sudo snap install jupyter

echo "Discord Kuruluyor... "

sudo snap install discord

echo "Meld Kuruluyor... "

sudo apt install meld

echo "VLC Kuruluyor... "

sudo snap install vlc

echo "GİT Kuruluyor... "

sudo apt install git

echo "Pip Yükseltiliyor..."

sudo -H pip install --upgrade pip

echo "HTOP Kuruluyor... "

sudo apt install htop

echo "PyQt5 Kuruluyor... "

pip install PyQt5

printf "\n\n\n\nKurulan Programlar : \n 1- Sistem Güncellendi \n2- Pycharm Kuruldu \n3- Cisual Studio Code Kuruldu \n4- Jupyter NoteBook Kuruldu 5- Discord Kuruldu \n6- Meld Kuruldu \n7- VLC Kuruldu \n8- git Kuruldu \n9- htop Kuruldu \n10-PyQt5 Kütüphanesi Kuruldu \n11- Pip son versiyona Güncellendi.\n\n\n"
echo "Şimdi Saygı Değer Sisilya Hanım Lütfen Rica Edersek  Bilgisayarınızı Yeniden Başlatırmısınız?"
