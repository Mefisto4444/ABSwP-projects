import sys
from random import randint

plansza = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",}

def plansza_wyś(plansza): #............................................wyświetl planszę
    print(plansza[1],"|",plansza[2],"|",plansza[3])
    print("-" * 2 + "|" + "-" * 3 + "|" + "-" * 2)
    print(plansza[4],"|",plansza[5],"|",plansza[6])
    print("-" * 2 + "|" + "-" * 3 + "|" + "-" * 2)
    print(plansza[7],"|",plansza[8],"|",plansza[9])
    print()

def sprawdzenie(plansza):
    if plansza[1] == plansza[2] == plansza[3]:#..............Sprawdzanie w wierszach
        print("Wygrał gracz:",plansza[1])
        plansza_wyś(plansza)
        sys.exit()
    elif plansza[4] == plansza[5] == plansza[6]:
        print("Wygrał gracz:",plansza[4])
        plansza_wyś(plansza)
        sys.exit()
    elif plansza[7] == plansza[8] == plansza[9]:
        print("Wygrał gracz:",plansza[7])
        plansza_wyś(plansza)
        sys.exit()
    if plansza[1] == plansza[4] == plansza[7]:#.................Sprawdzanie w kolumnach
        print("Wygrał gracz:",plansza[1])
        plansza_wyś(plansza)
        sys.exit()
    elif plansza[2] == plansza[5] == plansza[8]:
        print("Wygrał gracz:",plansza[2])
        plansza_wyś(plansza)
        sys.exit()
    elif plansza[3] == plansza[6] == plansza[9]:
        print("Wygrał gracz:",plansza[3])
        plansza_wyś(plansza)
        sys.exit()
    if plansza[1] == plansza[5] == plansza[9]:#...............Sprawdzanie po skosie
        print("Wygrał gracz:",plansza[1])
        plansza_wyś(plansza)
        sys.exit()
    elif plansza[3] == plansza[5] == plansza[7]:
        print("Wygrał gracz:",plansza[3])
        plansza_wyś(plansza)
        sys.exit()


def czy_wolne(plansza, p):#...........................................Sprawdzenie czy pole na planszy jest wolne
    if plansza[p] == "O" or plansza[p] == "X":
        return False
    else:
        return True


def ruch_pc(plansza):
    ruch = randint(1,9)
    return plansza[ruch] 


while True:#..............................................................Wybór: kółko czy krzyżyk
    kolej = input("Wybierz chcesz być O czy X: ").upper()
    if kolej == "O" or kolej == "X":
        break
plansza_wyś(plansza)
for i in range(9):
    while True:
        pole = int(input(f"Kolejka gracza {kolej}. Na którym polu: "))
        if czy_wolne(plansza,pole) == True:    
            plansza[pole] = kolej
            if kolej == "O":
                kolej = "X"
            else:
                kolej = "O"
        else:
            print("Pole zajęte")
            continue
        sprawdzenie(plansza)
        plansza_wyś(plansza)
print(ruch_pc)


def ruch_gracza(ruch,plansza):
    ruch = input("Podaj pole: ")
    return plansza[ruch]
