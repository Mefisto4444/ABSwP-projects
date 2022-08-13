import re
kalendarz = {"01" : "31", "02" : "28", "03" : "31", "04" : "30", "05" : "31", "06" : "30",
 "07" : "31", "08" : "31", "09" : "30", "10" : "31", "11" : "30", "12" : "31"}
daty = []

dataWzór = re.compile(r"""
(\d{1,2}|\d{4})#......................Pierwszy człon daty (dzień, miesiąc lub rok)
(\.|-|\s|/)#............................Separator
(\d{1}|\d{2})#......................Drugi człon daty (dzień lub miesiąc)
(\.|-|\s|/)#............................Separator
(\d{4}|\d{1,2})#........................Trzeci człon daty (dzień, miesiąc lub rok)
""",re.X)
moD = dataWzór.findall(input(": "))

def przestępny(r, c):#.........................................Sprawdź czy dany rok jest przestępny
    if r % 4 == 0 and r % 100 != 0 or r % 400 == 0:
        c["02"] = "29"
        return True
    else:
        c["02"] = "28"
        return False


def which_is_which(part1, part2, part3):#.............Przypisz do odpowiednich części daty dzień, miesiąc i rok
    global dzień, miesiąc, rok
    if len(part1) == 4:
        rok = part1
        dzień = part2
        miesiąc = part3
    if len(part3) == 4:
        rok = part3
        dzień = part1
        miesiąc = part2


def In_month(d,m,c):#..................Sprawdza czy dzień istnieje w miesiącu
    try:
        if int(d) not in range(1, int(c[m]) + 1):
            return False
        else:
            return True
    except KeyError:
        return False

for data in range(len(moD)):#..........................Pętla główna
    moD[data] = list(moD[data])
    for element in range(len(moD[data])):
        if (moD[data][element] != "." and moD[data][element] != "-" and moD[data][element] != r"\s" and moD[data][element] != "/")\
        and (len(moD[data][element]) < 2):
            moD[data][element] = "0"+ moD[data][element]
    p1 = moD[data][0]
    p2 = moD[data][2]
    p3 = moD[data][4]
    which_is_which(p1,p2,p3)
    przestępny(int(rok), kalendarz)
    if In_month(dzień, miesiąc, kalendarz) == True:
        date = dzień, miesiąc, rok
        daty.append(".".join(date))
    else:
        continue

for data in daty:
    print(data)