from pathlib import Path
import re

p = Path("D:\\jakub\\reddit\\files")
pliki = list(p.glob("*.txt"))
zapytanie = input("Czy ignorować wielkość znaków?\n").lower()
if zapytanie == "tak":
    wzór = re.compile(input(r"wzór: "),re.I)
if zapytanie == "nie":
    wzór = re.compile(input(r"wzór: "))
znalezione = {}
for plik in pliki:
    cf = open(plik)
    linie = cf.readlines()
    for linia in range(len(linie)):
        find = re.findall(wzór, linie[linia])
        if len(find) != 0:
            pomoc = {}#.................................TODO stworzyć słownik pomocniczy, który przechowuje jako klucz numer linii i jako wartość zawartość linii
            if str(plik).split("\\")[-1] not in znalezione.keys():
                znalezione[str(plik).split("\\")[-1]] = ((linia+1, linie[linia]),)
            else:
                znalezione[str(plik).split("\\")[-1]] = znalezione[str(plik).split("\\")[-1]] + ((linia+1, linie[linia]),)
    cf.close()
for klucz in znalezione.keys():
    print("_"*20, f"plik: {klucz}", "_"*20)
    for krotka in znalezione[klucz]:
        print(f"* linia: {krotka[0]}, zawartość: {krotka[1]}")

