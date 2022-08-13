from pathlib import Path
import os
import shelve
import pprint

# print(Path.cwd())
# print(Path.home())
# print(Path.cwd().is_absolute())
# print(Path("D:\\jakub\\reddit\\gówno.txt").is_absolute())
# print(Path(".\\gówno.txt").is_absolute())
# print(os.path.abspath(".\\gówno.txt"))
# print(os.path.relpath("D:\\jakub\\reddit\\sraka.txt","reddit"))
p = Path.cwd()
# print(p)
# print(p.drive)
# print(p.anchor)
# print(p.parent)
# print(p.name)
# print(p.suffix)
# print(p.stem)
# print(p.parents[0])
# print(p.parents[1])
# print(os.path.dirname(p))
# print(os.path.basename(p))
# print(os.path.split(p))
#print(os.path.getsize("D:\\jakub\\reddit\\kanapki.py"))
#print(os.listdir(p))

p = Path("spam.txt")
p.write_text("Litwo ojczyzno moja! ty jesteś jak zdrowie;\nIle cię trzeba cenić, ten tylko się dowie,\nKto cię stracił.\
Dziś piękność twą w całej ozdobie\nWidzę i opisuję, bo tęsknię po tobie")
file = open("D:\\jakub\\reddit\\spam.txt","a")
file.write("\nAutor: Adam Mickiewicz")
file.close()
# file = open("D:\\jakub\\reddit\\spam.txt","r")
# print(file.read())
# file.close()
koty = [{"Imie":"Filemon", "Rodzaj":"Ulany"},{"Imie":"Marcysia","Rodzaj":"Puszysty"}]
file = open("D:\\jakub\\reddit\\spam.txt",'a')
file.write("\n\n"+pprint.pformat(koty))
file.close()
# file = open("D:\\jakub\\reddit\\spam.txt")
# print(file.read())
# file.close()
def kwadrat(a):
    return a**2
