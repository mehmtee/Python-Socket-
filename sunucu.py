# Baslangic
# -*- coding: utf-8 -*- 

print("""
	Burası sunucu tarafı. Bu bizim bilgisayarımızdaki verileri okuduğumuz kısım
	""")
import socket  
sunucuSoketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
host = ''  
port = 23455
Buffer_Boyutu = 1024
sunucuSoketi.bind((host, port))
sunucuSoketi.listen(5)
print  port, "portu acildi ve baglantilar dinleniyor" 
baglantiAdedi = 1


while True:
	print "\n" + "*******************************************" + "\n"
	baglanti, istemciIPAdresi = sunucuSoketi.accept() # Baglanti talebi olusturuldu
	print "istemciden gelen", baglantiAdedi, "nolu baglanti kabul edildi"
	print 'Baglanan istemci IP Adresi ve Portu:', istemciIPAdresi
	while True:
		istemcidenGelenMesaj = baglanti.recv(Buffer_Boyutu)
		if not istemcidenGelenMesaj:
			break
		print "Istemciden mesaj geldi: ", istemcidenGelenMesaj
		baglanti.send('Mesajın alındı. Teşekkür ederiz')
	baglanti.close()
	print baglantiAdedi, "nolu istemci ile baglanti kesildi."
	baglantiAdedi += 1

# Sonuc