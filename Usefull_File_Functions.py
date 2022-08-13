import os

def FindTheBigGuy(path):
    import os
    największy = 0
    dane = ""
    print(f"Trwa wyszukiwanie największego pliku w podanym katalogu ({path}).........")
    for Main_Folder, Podfoldery, Pliki in os.walk(path):
        for plik in Pliki:
            rozmiar = os.path.getsize(f"{Main_Folder}\\{plik}")
            if rozmiar > największy:
                największy = rozmiar
                dane = f"{Main_Folder}\\{plik}"
    print("Znaleziono największy plik:")
    print(f"{największy} B = {round(największy/1024,2)} KB = {round((największy/1024)/1024,2)} MB = {round(((największy/1024)/1024)/1024,2)} GB,\
     Lokalizacja ({dane})")
    return największy, dane

def FolderBiggerThanShouldBe(Files_num, path):
    import os
    zbyt_duże = []
    print(f"Szukanie folderów, które mają więcej plików niż {Files_num} plików..........")
    for Folder, Podfoldery, Pliki in os.walk(path):
        if len(os.listdir(Folder)) > Files_num:
            zbyt_duże.append(Folder)
    print("Zbyt duże foldery: ")
    for path in zbyt_duże:
        print(f"*{path} | {len(os.listdir(path))}")
    print("Zakończono proces")
    return zbyt_duże



def FileBiggerThanShouldBe(size:int, ścieżka:str):
    import os
    znalezione = []
    print(f"Wyszukiwanie plików większych niż {size} MB w {ścieżka}.......")
    for Main_Folder, Podfoldery, Pliki in os.walk(ścieżka):
        for Plik in Pliki:
            Current_File_Size = round((os.path.getsize(f"{Main_Folder}\\{Plik}")/1024)/1024,2)
            if Current_File_Size > size:
                znalezione.append((f"{Main_Folder}\\{Plik}",Current_File_Size))
                print(f"*{Main_Folder}\\{Plik} | {Current_File_Size} MB")
    print("Zakończono proces")
    return znalezione

def FindTheBigGuy2(path):
    import os 
    największy = 0
    dane = ""
    print(f"Szukanie największego katalogu w obszarze ({path}).............")
    for Main_folder, Subfolders, Files in os.walk(path):
       if len(os.listdir(Main_folder)) > największy:
        największy = len(os.listdir(Main_folder))
        dane = f"{Main_folder}"
    print(f"Znaleziono największy folder: {dane} | {największy} elementów")
    return dane, największy

choice = input(f"1 - Znajdź największy plik w danej ścieżce\n2 - Znajdź największy folder w danej ścieżce\n3 - Wyszukaj pliki we wskazanej ścieżce, które mają więcej niż x MB\n4 - Wyszukaj foldery we wskazanej ścieżce, które mają więcej niż x plików\n: ")
if choice == "1":
    FindTheBigGuy(input("Ścieżka: "))
if choice == "2":
    FindTheBigGuy2(input("Ścieżka: "))
if choice == '3':
    FileBiggerThanShouldBe(int(input("Rozmiar w MB:")),input("Ścieżka: "))
if choice == '4':
    FolderBiggerThanShouldBe(int(input("Ilość: ")),input("Ścieżka: "))
