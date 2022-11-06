#1.Hafta

#1-10 Arası Sayıların Toplamı

toplam=0
for i in range(0,11):
    toplam=toplam+i
print(toplam)


#1-10 Arası Tek Sayıların Toplamı

toplam=0
for i in range(0,11):
    if i%2==1:
        toplam=toplam+i
print(toplam)


#1-10 Arası Tek Sayıların Toplamı(While)

i=0
toplam=0
while i<11:
    toplam=toplam+i
    i=i+1
print(toplam)

#Faktoriyel Hesaplama 

sayi=int(input("Bir sayı girin"))
carpim=1
for i in range(1,sayi+1):
    carpim=carpim*i
print(carpim)

#Faktoriyel Hesaplama(While)

sayi=int(input("Bir sayı girin"))
carpim=1

while sayi>0:
    carpim=carpim*sayi
    sayi=sayi-1
print(carpim)
 
#Toplamda 10 sorunun sorulduğu bir sınavda her doğru cevap için 10 puan alınırken her yanlış cevap için -5 puan alınmaktadır.
#Tüm soruları cevaplayan bir kişinin doğru yanliş sayısı klavyeden girildiğinde toplam puanını ekrana yazan programın kodunu yazınız.

dogruSayisi=int(input("Doğru sayısını girin"))
yanlisSayisi=int(input("Yanlış sayısını girin"))

dogruPuan=0
yanlisPuan=0
toplamPuan=0

toplamSoru=dogruSayisi+yanlisSayisi

if toplamSoru==10:
    dogruPuan=dogruSayisi*10
    yanlisPuan=yanlisSayisi*-5
    toplamPuan=yanlisPuan+dogruPuan
    print("Toplam puanınız =",toplamPuan)
else:
    print("Soru sayılarını kontrol edin")
    







    

  
