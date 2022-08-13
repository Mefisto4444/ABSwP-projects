def autokorekta(string):
    import re
    licznik = 0
    koniec = 0
    nstr = ""
    for litera in range(len(string)):
        if (string[litera] == " " or string[litera] == "!") and string[litera] == string[litera-1]:
            continue
        nstr = nstr + string[litera]
    wzór= re.compile(r"(.+)(?=\1)")
    nstr = re.sub(wzór,"",nstr)
    return nstr

print(autokorekta(input(": ")))