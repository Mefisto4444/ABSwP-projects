import datetime, os, bs4, requests, re

PATH = r"C:\Users\PC\OneDrive\Pulpit\komiksy"

try:
    os.mkdir(PATH)
except FileExistsError:
    pass

with open("last_check.txt",'r') as FileR:
    if len(FileR.readlines()) == 0:
        FileR.close
        with open("last_check.txt",'w') as FileW:
            FileW.write(str(datetime.datetime.now()))

def newComic(string:str):
    days = ["Monday","Thursday", "Wednesday", "Thursady", "Friday", "Saturday", "Sunday"]

    if string.split(" ")[0] in days:
        m, d, y = string.split(" ")[1], string.split(" ")[2], string.split(" ")[3]
    else:
        m, d, y = string.split(" ")[0], string.split(" ")[1], string.split(" ")[2]
    d = re.sub(re.compile(r"[a-zA-Z]+"),"",d)
    date = datetime.datetime.strptime(f"{d} {m} {y}", "%d %B %Y")

    with open("last_check.txt") as check_file:
        last_date = check_file.readline()
        check_file.close()

    last_date = last_date.replace("-"," ").replace(":"," ").split(" ")
    ldy , ldm, ldd, ldh, ldM, lds = last_date[0], last_date[1], last_date[2], last_date[3], last_date[4], last_date[5]
    lds = str(round(float(lds)))
    last_date = datetime.datetime.strptime(f"{ldy} {ldm} {ldd} {ldh} {ldM} {lds}","%Y %m %d %H %M %S")
    return last_date < date

def Butter_safe(path):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64"}
    res = requests.get("https://www.buttersafe.com/",headers=headers)
    try:
        res.raise_for_status()
    except Exception as Ex:
        print("Wystąpił błąd:",Ex)
    
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    img_url = soup.select('#comic img')[0].get('src')
    publish_date = soup.select('#headernav-date')[0].get_text().replace("\n","")\
    .replace("\t","").replace(",", "")

    img_res = requests.get(img_url, headers=headers)
    try:
        img_res.raise_for_status()
    except Exception as Ex:
        print("Wystąpił błąd:",Ex)
    
    if newComic(publish_date) == True:
        file_name = img_url.split("/")[-1]
        for chunk in img_res.iter_content(10000):
            with open(f"{path}\\{file_name}",'wb') as ImgF:
                ImgF.write(chunk)


def s_chickens(path):
    res = requests.get("https://www.savagechickens.com")
    try:
        res.raise_for_status()
    except Exception as Ex:
        print('Błąd:',Ex)
    
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    img_url = soup.select('.entry_content img')[0].get('src')
    publish_date = soup.select('span[class="date time published"]')[0].get_text().replace(",","")
    
    img_res = requests.get(img_url)
    try:
        img_res.raise_for_status()
    except Exception as Ex:
        print("Wystąpił błąd:",Ex)

    if newComic(publish_date) == True:
        file_name = img_url.split("/")[-1]
        for chunk in img_res.iter_content(10000):
            with open(f"{path}\\{file_name}",'wb') as ImgF:
                ImgF.write(chunk)

def l_baboon(path):
    res = requests.get("http://www.lunarbaboon.com")
    try:
        res.raise_for_status()
    except Exception as Ex:
        print("Wystąpił błąd:",Ex)
    
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    img_url = soup.select('div[class="body"] img')[0].get('src')
    publish_date = soup.select('span[class="posted-on"]')[0].get_text().strip(" ").replace(",","").split(" ")[1:4]
    publish_date = " ".join(publish_date)
    img_res = requests.get("http://www.lunarbaboon.com"+img_url)
    try:
        img_res.raise_for_status()
    except Exception as Ex:
        print("Wystapił błąd:",Ex)

    if newComic(publish_date) == True:
        file_name = img_url.split("/")[-1]
        for chunk in img_res.iter_content(10000):
            with open(f"{path}\\{file_name}",'wb') as ImgF:
                ImgF.write(chunk)        

def Moonbread(path):
    hreaders = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64"}
    res = requests.get("https://moonbeard.com",headers = hreaders)
    try:
        res.raise_for_status()
    except Exception as Ex:
        print("Wystapił błąd:",Ex)

    soup = bs4.BeautifulSoup(res.text,"html.parser")
    img_url = soup.select('#comic img')[0].get('src')
    publish_date = soup.select('span[class="post-date"]')[0].get_text().replace(",","")
    
    img_res = requests.get(img_url)
    try:
        img_res
    except Exception as Ex:
        print("Wystąpił błąd:",Ex)

    if newComic(publish_date) == True:
        file_name = img_url.split("/")[-1]
        for chunk in img_res.iter_content(10000):
            with open(f"{path}\\{file_name}",'wb') as ImgF:
                ImgF.write(chunk)




Butter_safe(PATH)
s_chickens(PATH)
l_baboon(PATH)
Moonbread(PATH)
with open("last_check.txt",'w') as last_check:
    last_check.write(str(datetime.datetime.now()))