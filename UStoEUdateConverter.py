from pathlib import Path
import re, shutil, os
wzór = re.compile(r"""
    (.*)?
    ([0-1]\d)#....................miesiąc
    (\.|-)#................................separator
    ([0-3]\d)#..........................dzień
    (\.|-)#................................separator
    (\d\d\d\d)#....................................rok
    (.*)?
    """,re.VERBOSE)
poszukiwane_pliki = []
for element in os.listdir():
    znalezione = re.match(wzór, element)
    if znalezione == None:
        continue
    print("Wyszukiwanie pliku.....")
    nazwa = znalezione.groups()
    nazwa = list(nazwa)
    nazwa[1], nazwa[3] = nazwa[3], nazwa[1]
    print("Zmiana nazwy.....")
    shutil.move(Path.cwd() / "".join(znalezione.groups()),Path.cwd() / "".join(nazwa))
    print('gotowe....')
