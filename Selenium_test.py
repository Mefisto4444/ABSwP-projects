from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyinputplus import inputPassword
import sys, time, requests,bs4
if len(sys.argv) < 6:
    email = input("Podaj email: ")
    password = inputPassword("Podaj hasło: ")
    nadawca = input("Adresat: ")
    temat = input("Temat: ")
    treść = input("Treść: ")
else:
    email = sys.argv[1]
    password = sys.argv[2]
    nadawca = sys.argv[3]
    temat = sys.argv[4]
    treść = sys.argv[5]
driver = Service("C:\Program Files (x86)\chromedriver.exe")
browser = webdriver.Chrome(service=driver)
browser.get("https://www.google.com/intl/pl/gmail/about/")
time.sleep(2)
try:
    find_logIn = browser.find_element(By.LINK_TEXT,"Zaloguj się")
except:
    print("Nie udało się znaleźć elementu.")
    browser.quit()
    sys.exit()
browser.get(find_logIn.get_attribute("href"))

find_Ident = browser.find_element(By.ID,"identifierId")
find_Ident.send_keys(email)
find_Ident.send_keys(Keys.ENTER)
time.sleep(0.4)
browser.get(browser.current_url)
try:
    find_Passw = browser.find_element(By.NAME,"password")
except:
    print("Nie znaleziono elemenu hasła'")
    browser.quit()
time.sleep(0.4)
find_Passw.send_keys(password)
find_Passw.send_keys(Keys.ENTER)
time.sleep(5)
# print(browser.current_url)
# try:
#     create = browser.find_element(By.CSS_SELECTOR,"#\:2p > div > div")
# except:
#     print("Nie ma ")
#     browser.quit()
#     sys.exit()
# print("Jest")
# create.click()
# time.sleep(2)
html_elem = browser.find_element(By.TAG_NAME,'html')
html_elem.send_keys('c')
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(nadawca)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(temat)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(treść)
html_elem.send_keys(Keys.ENTER)
time.sleep(10)
browser.quit()
sys.exit()