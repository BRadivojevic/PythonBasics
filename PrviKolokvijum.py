import math
import os
import random
import time
#Ceo program se pokrece u command promptu C:\Users\Stefan\PycharmProjects\ProbniKolokvijum1>py PrviKolokvijum.py trazio je tako!
#odnosno putanja do naziva vaseg py fajla , pa onda py PrviPokolkvijum.py
#zadatak1
N = 10000
brojac = 0
for i in range(N):
    Xpom = random.uniform(0, 1)
    Ypom = random.uniform(0, 1)
    if math.sqrt(Xpom) > Ypom and Xpom ** 2 < Ypom:
        brojac += 1
# print(brojac) #provera da li je dobro
Povrsina = 1#u zadatku na slici graf je imao Xmax=1 i Ymax=1
print("Povrsina je : ", Povrsina * brojac / N)
#zadatak2
Rec = "N^MZC"#mozda na kolokvijumu da input
for i in range(5, 15, 1):
    Sifra = ""
    for y in range(len(Rec)):
        Sifra += chr(ord(Rec[y]) ^ i)
    print(Sifra)
Input=input("Unesite nesteo")#da bi stopirali aplikaciju, tako je trazio
#zadatak3 animacija
Matrica = [[" " for x in range(10)] for y in range(10)]
for red in Matrica:
    print("".join(red))
brojac = 0
while True:
    if brojac == 0:
        for x in range(10):
            for i in range(10):
                for y in range(10):
                    if i == brojac or y == brojac:
                        Matrica[brojac][y] = "@"
                        Matrica[i][brojac] = "@"
            brojac += 1
            for red in Matrica:
                print("".join(red))
            Matrica = [[" " for x in range(10)] for y in range(10)]
            time.sleep(0.1)
            os.system("cls")
    if brojac == 10:
        for x in range(10):
            for i in range(10):
                for y in range(10):
                    if i == brojac or y == brojac:
                        Matrica[brojac][y] = "@"
                        Matrica[i][brojac] = "@"
            brojac -= 1
            for red in Matrica:
                print("".join(red))
            Matrica = [[" " for x in range(10)] for y in range(10)]
            time.sleep(0.1)
            os.system("cls")
