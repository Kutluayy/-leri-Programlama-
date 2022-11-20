
#5.Hafta

#Eleman sayısını klavyeden girilen program
liste=[]

elemansayisi=int(input("Elememan sayısını girin"))

for i in range(0,elemansayisi):
    eleman=input(i,"elemanı girin")
    liste.append(eleman)

print("Liste =",liste)


--------------------------------------------------------------------------------------------
#Eleman sayısını klavyeden girilen program ve elemanların toplamını bulan program.
liste=[]

elemansayisi=int(input("Elememan sayısını girin"))
toplam=0
for i in range(0,elemansayisi):
    eleman=int(input("elemanı girin"))
    liste.append(eleman)
    toplam=toplam+eleman

print("Liste =",liste)
print("Eleman Toplamı",toplam)

--------------------------------------------------------------------------------------------------------------
# 0 ile 100 arasında rastgele olacak şekilde 10 oluşurup bu sayıları bir liste içerisine aktaran ve yine bu liste içerisindeki sayılarınkaç tanesinin 50'den küçük olduğunu yazdıran Python kodunu yazınız.

import random 

liste=[]

for i in range(0,10)
     sayi=random.randint(0,100)
     liste.append(sayi)

for i in range(0,10):
    if liste[1]<50:
        count=count+1

print("50'den küçük eleman sayısı =",count)
print(liste)            