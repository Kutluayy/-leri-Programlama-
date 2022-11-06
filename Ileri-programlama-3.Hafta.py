#3.Hafta

# Girilen Vize ve Final notu ortalamasını hesaplayan programı yazınız.
vize=int(input("Vize notunu girin"))
final=int(input("Final notunu girin"))

ortalama=(vize*0.4)+(final*0.6)
print(ortalama)
if ortalama>40:
    print("Geçtiniz")
else: print("Kaldınız")

#Klavyeden girilen taban ve üst değerine göre o sayının üssünü hesaplayan ve sonucunu ekrana yazdıran program.

taban=int(input("Tabanı girin"))
us=int(input("Üssü girin"))
carpim=1
for i in range(0,us):
    carpim=carpim*taban
 
print(taban,"'ın ",us,"inci kuvveti =",carpim)
print(taban**us)

#Sıfır girilene kadar klavyeden tam sayı değerleri alın,sayılardan en büyüğü ile en küçüğü bulan ve ekrana yazdıran program.

sifirMi=True
eb=0
ek=0
while sifirMi:
    
    sayi=int(input("Bir sayı girin"))
    if sayi==0:
        break
    else:
        if sayi>eb:
            eb=sayi
        elif sayi<ek:
            ek=sayi
            
print("En büyük",eb)
print("En küçük",ek)       
        
#Bir mülakatta İngilizce veya Fransızca biliyor mu yazdıran kod.

ad_soyad=input("Adınız ve soyadınızı girin")
yas=int(input("Yaşınızı girin"))
if yas>40:
    print("Yas sınırını aştınız.")
    print("Mülakat başarısız")
else:
    cevap=input("İngilizce ve ya Fransızca biliyor musunuz? E/H")
    if cevap=="H":
        print("Dil şartını sağlamıyorsunuz")
        print("Mülakat başarısız")
    elif cevap=="E":
        print("Tebrikler" , ad_soyad," Mülakat başarılı")
    else: print("Yanlış giriş")

#Klavyeden girilen ilk metin içinden ilk metin'de olan ama ikinci metinde olmayan ögeleri yazdıran kod
metin1=input("1. metni girin")
metin2=input("2. metni girin")

for i in metin1:
    if i not in metin2:
        print(i)













