import bs4, shutil, requests, sys, os

pominięte = []

Url = "https://xkcd.com"
print("Przygotowywanie katalogu....")
try:
    os.mkdir("D:\\jakub\\reddit\\zdjęcia")
except FileExistsError:
    shutil.rmtree("D:\\jakub\\reddit\\zdjęcia")
    os.mkdir("D:\\jakub\\reddit\\zdjęcia")
while Url.endswith("1500/") == False:
    print(f'Łączenie ze stroną {Url}....')
    res = requests.get(Url)
    try:
        res.raise_for_status()
    except Exception as Ex:
        print("Nastąpił błąd:",Ex,"\nProgram zostanie zakończony.")
        sys.exit()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    Pic_Url = soup.select('#comic img ')
    if len(Pic_Url) == 0:
        print("Pominięcto stronę. Nie znaleziono zdjęcja.")
        pominięte.append(Url)
        Prev_Link = soup.select("a[rel='prev']")[0].get("href")
        Url = "https://xkcd.com"+str(Prev_Link)
        continue
    Pic_Url = soup.select('#comic img ')[0].get("src")
    Prev_Link = soup.select("a[rel='prev']")[0].get("href")
    try:
        res = requests.get("https:"+str(Pic_Url))
    except:
        print("Nie udało się pobrać strony...")
        pominięte.append(Url)
        Url = "https://xkcd.com"+str(Prev_Link)
        continue
    try:
        res.raise_for_status()
    except Exception as Ex:
        print("Wystąpił błąd:",Ex)
    print(f"Pobieranie zdjęcia {Pic_Url}....")
    File = open("D:\\jakub\\reddit\\zdjęcia\\"+os.path.basename(str(Pic_Url)),'wb')
    for chunk in res.iter_content(100000):
        File.write(chunk)
    File.close()
    Prev_Link = soup.select("a[rel='prev']")[0].get("href")
    Url = "https://xkcd.com"+str(Prev_Link)
print(pominięte)
print("Zakończono działaniue programu")
