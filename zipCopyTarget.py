import os, zipfile as zf
from pathlib import Path
ścieżka = "D:\\jakub\\reddit"
ścieżka = os.path.abspath(ścieżka)
number = 0
while True:
    zip_name = f"{os.path.basename(ścieżka)}_ZipCopy_{number}.zip"
    if os.path.exists(zip_name) == False:
        break
    number = number + 1
backup_zip = zf.ZipFile(zip_name,'w')
for Folder_name, Podfoldery, Files in os.walk(ścieżka):
    if len(list(Path(Folder_name).glob("*.py"))) > 0 or len(list(Path(Folder_name).glob("*.txt"))) > 0:
        backup_zip.write(Folder_name,compress_type=zf.ZIP_DEFLATED)
    for plik in Files:
        if plik.endswith(".py") or plik.endswith(".txt"):
            backup_zip.write(f"{Folder_name}\\{plik}", compress_type=zf.ZIP_DEFLATED)
