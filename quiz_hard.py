import time as ti
from random import randint

def timeLimit(limit_czasu):#....................................Odlicz czas od wprowadzenia danych
    check = True 
    t1 = ti.time()
    global odp
    while True:#................................Dane zawsze muszą być rodzaju int
        try:
            odp = int(input(": "))
            if isinstance(odp,int):
                break
        except ValueError:
            print("Błędne dane. Wprowadź odpowiedź jeszcze raz!")
            continue
    t2 = ti.time()
    t = t2 - t1
    if t > limit_czasu:
        check = False
        return check

    if check == True:
        return check


punkty = 0
for pytanie in range(10):#......................10 pytań
    licznik1 = randint(0,9)
    licznik2 = randint(0,9)
    for próba in range(3):#........................................3 szanse na odpowiedź
        print(f"Podaj wynik działania {licznik1}x{licznik2}", end = "")
        if timeLimit(8) == True:
            if odp == licznik1 * licznik2:
                punkty = punkty + 1
                print("Dobrze")
                ti.sleep(1)
                break
            else:
                print("Źle")
        else:
            print("Koniec czasu")

if punkty < 10:#.................................podsumowanie konkursu
    print("Niestety nie wygrałeś konkursu")
else:
    print("Gratulacje, wygrałeś konkurs!!!")