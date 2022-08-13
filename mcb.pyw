#! python3
import sys,shelve, pyperclip as pc
mcbShelve = shelve.open("mcb")

if len(sys.argv) < 2:#..................................komendy główne
    print("Wprowadź słowo klucz")
if sys.argv[1] == "save" and len(sys.argv) == 3:
    mcbShelve[sys.argv[2]] = input("Podaj wiadomość słowa klucz: ")
if sys.argv[1] == "save" and len(sys.argv) == 3:
    sys.exit()
elif sys.argv[1] in mcbShelve.keys():
    pc.copy(mcbShelve[sys.argv[1]])
if sys.argv[1] == "list":
    for klucz in mcbShelve.keys():
        print(f"* {klucz} : {mcbShelve[klucz]}")

if sys.argv[1] == "delete" and len(sys.argv) == 2:#.......................komendy usuwania
    mcbShelve.clear()
elif sys.argv[1] == "delete" and sys.argv[2] not in mcbShelve.keys() and len(sys.argv) > 2:
        print("Podany klucz nie istnieje")
elif sys.argv[1] == "delete" and sys.argv[2] in mcbShelve.keys() and len(sys.argv) > 2:
        del mcbShelve[sys.argv[2]]

mcbShelve.close()
sys.exit()
