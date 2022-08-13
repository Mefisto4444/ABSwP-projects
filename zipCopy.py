import os, zipfile as zf
folder = "D:\\jakub\\reddit\\Important"
p = os.path.abspath(folder)
number = 0
while True:
    zip_name = os.path.basename(p) + "_" + str(number) + ".zip"
    if os.path.exists(zip_name) == False:
        break
    number = number + 1
backupZip = zf.ZipFile(zip_name,'w')
print(f"Utworzono archiwum zip {zip_name}...")
for folder_name, subfolders, files in os.walk(folder):
    print(f"Dodawanie folderu {folder_name}...")
    backupZip.write(folder_name, compress_type= zf.ZIP_DEFLATED)
    for file in files:
        print(f"Dodawanie plików z {folder_name} do archiwum...")
        backupZip.write(f"{folder_name}\\{file}", compress_type=zf.ZIP_DEFLATED)
        
