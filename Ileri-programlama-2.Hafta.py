#2.Hafta 


#Klavyeden 0 girilene kadar pozitif ve negatif sayıların girildiği kod
#Girilen sayıların kaçı negatif? kaçı pozitif? Sayıların ortalamasını bulan kod

sifirMi=True
negaSayac=0
pozSayac=0
toplam=0
while sifirMi:
    sayi=int(input("Bir sayı girin"))
    if sayi ==0:
        sifirMi=False
    elif sayi<0:
        toplam+=toplam+sayi
        negaSayac=negaSayac+1
    else:
        toplam=toplam+sayi
        pozSayac=pozSayac+1
        
ort=toplam/(pozSayac+negaSayac)
print("Ortalama ",ort)

# 3 Basamaklı Sayıların Toplamını bulan kod

Sayi=int(input("3 basamaklı bir sayı girin"))
birler=Sayi%10
yuzler=(int)(Sayi/100)
onlar1=int(Sayi/10)
onlar=onlar1%10

print("Yüzler", yuzler," Onlar ",onlar,"Birler ",birler)
toplam=yuzler+onlar+birler
print("Toplam =",toplam)

# Toplamda 3 cevap hakkı verilen bir sayı tahmin oyununu kodu

import random

sayi=random.randint(0,100)

for i in range(0,3):
    tahmin=int(input("Tahmin girin"))
    if sayi==tahmin:
        print("Tebrikler bildiniz")
        break
    else:
        print("Bi daha deneyin")

#Klavyeden bir sayının asal olup olmadığını bulan programı yazınız

sayi=int(input("Bir sayı girin"))

for i in range(2,sayi):
    if sayi%i==0:
        print("Asal değildir")
        break
    else:
        print("Sayı asaldır")
    
#Klavyeden girilen bir kelime içindekı sesli harfleri bulan kod

kelime="Klavyeden girilen bir kelime içindeki sesli harfleri bulma"

sayac=0
harf=input("aranacak harfi girin")
for i in kelime:
    if i==harf:
        sayac=sayac+1
        
print(harf," harfi cümle içinde",sayac," tane var")

#Klavyeden girilen bir kelime içindekı sesli  ve sessiz harfleri bulan kod
 
cumle="Klavyeden girilen bir kelime içindeki sesli harfleri bulan kodu yazınız."
sesli="aeiıouüö"
sessiz="qwrtypğsdghjklşzxcvbnmç"  
harfler_sesli=" "
harfler_sessiz=" "   

for i in  cumle:
    if i in sesli:
        harfler_sesli=harfler_sesli+i
    elif i in sessiz:
        harfler_sessiz=harfler_sessiz+i
        
print("Sesli harfler ",harfler_sesli)
print("Sessiz harfler ",harfler_sessiz)

  
