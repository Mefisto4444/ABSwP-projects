import os, shutil
Folder_path = "D:\\jakub\\reddit\\kopiowanie_selektywne"
try:
    os.mkdir(Folder_path)
except FileExistsError:
    print("Podany folder już istnieje")
File_Type = input("Podaj rodzaj pliku: ")
print(f"Dodawanie plików o ({File_Type})......")
for Folder, Podfoldery, Pliki in os.walk("D:\\jakub"):
    for Plik in Pliki:
        if Plik.endswith(File_Type):
            try:
                shutil.copy(f"{Folder}\\{Plik}", f"{Folder_path}")
            except shutil.SameFileError:
                continue
