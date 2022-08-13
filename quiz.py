import pyinputplus as p
from random import randint
import time as t

punkty = 0

for pytanie in range(10):
    licznik1 = randint(0,9)
    licznik2 = randint(0,9)
    for i in range(3):
        try:
            odp = p.inputInt(f"Podaj wynik działania {licznik1}x{licznik2} : ",timeout=8)
        except p.TimeoutException:
            print("Konec czasu")
            break
        if odp == licznik1 * licznik2:
            punkty = punkty + 1
            print("Dobrze")
            t.sleep(1)
            break
        else:
            print("Źle")
if punkty < 10:
    print("Za mało punktów")
else:
    print("Gratulacje wygrałeś konkurs")
