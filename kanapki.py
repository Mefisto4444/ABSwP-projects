import pyinputplus as p

menu = {"":0,"pszenny":2, "biały":2.5, "na zakwasie":3, "kurczak":5, "indyk":7, "szynka":5, "cheddar":2,#............Zmienne
"szwajcarski":2, "mozzarella":3, "pomidor":3, "sałata":2, "majonez":1, "musztarda":1}
cena = 0
order = []

ilość = p.inputInt("Ilość kanapek: ")
for i in range(ilość):
    print(f"{i+1} zamówienie:\n")
    chleb = p.inputMenu(choices=["pszenny", "biały", "na zakwasie"], prompt="Podaj typ chleba:\n")#.............Składanie zamówienia
    mięso = p.inputMenu(choices=["kurczak", "indyk", "szynka"], prompt="Podaj rodzaj mięsa:\n")
    ser = p.inputYesNo("Dodać ser?: ", yesVal="tak", noVal="nie")
    ser_typ = ""
    if ser == "tak":
        ser_typ = p.inputMenu(["cheddar", "szwajcarski", "mozzarella"], prompt="Podaj rodzaj sera:\n")
    dodatek = p.inputYesNo("Dodać dodatek?: ", yesVal="tak", noVal="nie")
    dodatek_typ = ""
    if dodatek == "tak":
        dodatek_typ = p.inputMenu(["pomidor", "sałata", "majonez", "musztarda"],"Dodatek:\n")
    order = order + [chleb, mięso, ser_typ, dodatek_typ]



print(order)
for element in range(len(order[:-1])):#..................zliczenie ceny
    cena = cena + menu[order[element]]
print("Cena zamówienia:",cena,"zł")