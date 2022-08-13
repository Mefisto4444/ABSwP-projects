import sys, webbrowser, requests, bs4
if len(sys.argv) < 2:
    print("Nie prowadzono żadnych argumentów Nastąpi zamknięcie apliakcji.")
    sys.exit()
site = "https://pypi.org"
searching_target = "/search/?q=" + sys.argv[1]
res = requests.get(site+searching_target)
try:
    res.raise_for_status()
except Exception as Ex:
    print(f"Wystąpił błąd: {Ex}. Wyłączenie aplikacji.")
    sys.exit()
print("Nawiązano połączenie.")
soup = bs4.BeautifulSoup(res.text,"html.parser")
print("Otwieranie kart przeglądarki...")
for i in range(5):
    webbrowser.open(site + soup.select(".package-snippet")[i].get("href"))
print("Zakończono działanie.")