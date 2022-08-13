import bs4, shutil, requests, sys, os,threading

pominięte = []
print("Przygotowywanie katalogu...")
try:
    os.mkdir("D:\\jakub\\reddit\\zdjęcia")
except FileExistsError:
    shutil.rmtree("D:\\jakub\\reddit\\zdjęcia")
    os.mkdir("D:\\jakub\\reddit\\zdjęcia")

def downloader(startComic:int,endComic:int,miss:list):
    for urlNumber in range(startComic, endComic):
        print(f'Łączenie ze stroną https://xkcd.com/{urlNumber}....')
        res = requests.get(f"https://xkcd.com/{urlNumber}")
        try:
            res.raise_for_status()
        except Exception as Ex:
            print("Nastąpił błąd:",Ex,"\nProgram zostanie zakończony.")
            sys.exit()

        soup = bs4.BeautifulSoup(res.text,'html.parser')

        Pic_Url = soup.select('#comic img ')
        if len(Pic_Url) == 0:
            print("Pominięcto stronę. Nie znaleziono zdjęcja.")
            miss.append(f"https://xkcd/.com/{urlNumber}")
            continue
        Pic_Url = soup.select('#comic img ')[0].get("src")
        try:
            res = requests.get("https:"+str(Pic_Url))
        except:
            print("Nie udało się pobrać strony...")
            miss.append(f"https://xkcd.com/{urlNumber}")
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

downloadThreads = []
for i in range(1,1600,200):
    start = i
    end = i + 199
    downloadThread = threading.Thread(target=downloader,args=(start,end,pominięte))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for thread in downloadThreads:
    thread.join()
print(pominięte)
print("Zakończono działaniue programu")
