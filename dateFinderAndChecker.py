import re

kalendarz = {"01" : "31", "02" : "28", "03" : "31", "04" : "30", "05" : "31", "06" : "30",
 "07" : "31", "08" : "31", "09" : "30", "10" : "31", "11" : "30", "12" : "31"}
daty = []

dateFinder = re.compile(r"""
    ([0-3]\d)#.......................dzień
    (/|\.|-)#..................separator
    ([0-1]\d)#...................miesiąć
    (/|\.|-)?#..................separator
    ([1-2]\d{3})?#.....................rok
""",re.VERBOSE)
moD = dateFinder.findall(input(": "))

for data in range(len(moD)):#.....................Krotka zaawierające nieprawidłowe dane dotyczące daty to ją usuń
    for element in range(len(moD[data])):
        if moD[data][element] == "":
            del moD[data]

def czy_przestepny(rok):#.......................................Czy rok jest przestępny
    if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
        return True
    else:
        return False

def dni_w_miesiącu(d,m,c):#.....................................Czy dany dzień w miesiącu istnieje
    if int(d) not in range(1, int(c[m]) + 1):
        return False
    else:
        return True
data = ""
for index in range(len(moD)):#......................Sprawdź czy data spełnia warunki logiczne 
    dzień = moD[index][0]
    miesiąc = moD[index][2]
    rok = moD[index][4]
    if czy_przestepny(int(rok)) == True:
        kalendarz["02"] = "29"
    if dni_w_miesiącu(dzień, miesiąc, kalendarz) == True:
        data = "".join(moD[index])
        daty.append(data)
    else:
        continue
    kalendarz["02"] = "28"

for data in daty:#...................................Ładnie wyświetl daty
    print(data)
