import webbrowser, sys
if len(sys.argv) == 1:
    import pyperclip
    adres = pyperclip.paste()
else:
    adres = " ".join(sys.argv[1:])
webbrowser.open("https://www.google.pl/maps/place/"+ adres)