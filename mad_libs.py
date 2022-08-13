import re
file = open("D:\\jakub\\reddit\\mad_libs.txt",'r')
text = file.read()
file.close()
wzór = re.compile(r"RZECZOWNIK|CZASOWNIK|PRZYMIOTNIK")
tablica = re.findall(wzór, text)
for znalezione in range(len(tablica)):
    text = re.sub(wzór, input(f"Podaj {str(tablica[znalezione]).capitalize()}\n"), text, 1)
print(text)
file = open("D:\\jakub\\reddit\\mad_libs.txt",'w')
file.write(text)
file.close()