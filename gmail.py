import  ezgmail
import  os, time

COMS={
    ".shutwar" : "shutdown /s /t ",
    ".shutnow" : "shutdown /p"
}

def check_if_new(mail:ezgmail.GmailMessage):
    components = []
    with open("DataB.txt",'r') as DataFile:
        components.append(DataFile.readline())
    if mail.sender.split(" ")[-1] == components[0].split(",")[0] and\
         mail.body.replace("\n","").replace("\r","") == components[0].split(",")[1] and\
            str(mail.timestamp) == components[0].split(",")[2]:
        return False
    else:
        return True

while True:
    unread_threads = ezgmail.recent()
    print("Wykrywanie nadawcy root.....")
    if len(unread_threads[0].messages[0].sender.split(" ")) == 2:
        email_label = unread_threads[0].messages[0].sender.split(" ")[1]
    else:
        email_label = unread_threads[0].messages[0].sender.split(" ")[2]
    print(unread_threads[0].messages[0].sender.split(" "))
    if check_if_new(unread_threads[0].messages[0]) != True:
        time.sleep(1)
        continue
    elif email_label == "<someemail>":
        break
    time.sleep(1)

with open("DataB.txt",'w') as DataFile:
    mail_body = unread_threads[0].messages[0].body.replace("\r","").replace("\n","")
    DataFile.write(f"{unread_threads[0].messages[0].sender.split(' ')[-1]},{mail_body},{unread_threads[0].messages[0].timestamp}")
if mail_body.startswith(".shutwar "):
    print(COMS[mail_body[:-2]]+f"{mail_body[-1]}")
else:
    print(COMS[mail_body])

