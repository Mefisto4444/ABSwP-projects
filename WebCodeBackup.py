import requests, bs4, os, re
url_home = "https://ekonomik.gniezno.pl"
path = "D:\\jakub\\reddit\\WebBackup"
res = requests.get(url_home)
signs = re.compile(r'[\\/:\"\?&<>\|\*]*')
backupFolder = os.mkdir(path)
try:
    res.raise_for_status()
except Exception as Ex:
    print("Wystąpił błąd:",Ex)
soup = bs4.BeautifulSoup(res.text, "html.parser")

elements = soup.select('a[href]')
Urls = []
for url in elements:
    Urls.append(url.get("href"))

url = url_home
for i in range(len(Urls)):
    if str(url).startswith(f"{url_home}") == False and str(url).startswith(f"/") == False:
        print(f"Pominięto {url}....")
    else:
        if url.startswith(f"{url_home}") == False:
            url = url_home + url
        print(f"Łączenie ze stroną {url}......")
        temp_res = requests.get(url)
        try:
            temp_res.raise_for_status()
        except Exception as Ex:
            print("Wystąpił błąd:",Ex)
        if url.endswith(".pdf") or url.endswith("g"):
            url = Urls[i]
            continue
        temp_soup = bs4.BeautifulSoup(temp_res.text,"html.parser")
        title = temp_soup.find("title").get_text().replace(' ','_')
        search = re.search(signs, url).groups()
        if search != None:
            signs.sub("",str(search))
            try:
                pageCodeFile = open(path + f"\\{title}.txt",'wb')
            except:
                title = url.split("/")[-2]
                pageCodeFile = open(path + f"\\{title}.txt",'wb')
        print("Pobieranie strony...")
        for chunk in temp_res.iter_content(10000):
            pageCodeFile.write(chunk)
        pageCodeFile.close()
    url = Urls[i]
print("Ukończono procedurę pobierania kodu strony")
    