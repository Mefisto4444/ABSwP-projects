from cgi import test
import pyperclip, re

schowek = pyperclip.paste()
lista = []
text = ""

phoneNumberFinder = re.compile(r"""
    (\d{2,4}|\(\d{2,4}\)|\+\d{2,4})?#..........Numer kierunkowy
    (\s|-|\.)?#.........................Separator
    (\d{2,3})#..........................Pierwszy człon numeru
    (\s|-|\.)?#.........................Separator
    (\d{2,3})#..........................Drugi człon numeru
    (\s|-|\.)?#.........................Separator
    (\d{2,4})#..........................Trzeci człon numeru
""",re.VERBOSE)
moP = phoneNumberFinder.findall(schowek)


emailFinder = re.compile(r"""
    ([a-zA-Z1-9]+)#.................Pierwszy człon adresu
    (\.[a-zA-Z1-9]+)?#.............Drugi, opcjonalny człon adesu
    (@\w+\.)#...............Małpa, domena i kropka
    (\w+)#..................Końcówka
""",re.VERBOSE)
moE = emailFinder.findall(schowek)

#todo.........Sprawdzić czy w schowku występują ciągi spełniające wymagania wyrażenia phoneNumberFinder lub emailFinder,
#jeśli tak to dodać je do listy
lista = moP + moE
if len(lista) < 1:
    text = "Brak numerów telefonów oraz adresów email"
    pyperclip.copy(text)
    text = ""


#todo.........Sprawić, żebny dane z listy zostały ładnie wyświetlone w konsoli
for dopasowanie in range(len(lista)):
    for element in lista[dopasowanie]:
        text = text + element
    text = text + "\n"
pyperclip.copy(text)