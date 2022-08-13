import re, shutil, os
from pathlib import Path
p = "D:\\jakub\\reddit\\sortowane"
def Find_Files(ścieżka):
    File_list = []
    Original_File_List = []
    wzór = re.compile(r"([a-zA-Z0]*)([1-9]*0*)(.*)")
    nowy_numer = ""
    for Plik in os.listdir(ścieżka):
        szukaj = re.match(wzór, Plik)
        if szukaj != None:
            if len(szukaj.group(2)) == 1:
                nowy_numer = "0"+str(szukaj.group(2))
                File_list.append((szukaj.group(1), nowy_numer, szukaj.group(3)))
            else:
                File_list.append(tuple(szukaj.groups()))
            Original_File_List.append(szukaj.groups())
    File_list.sort()
    Original_File_List.sort()
    return File_list, Original_File_List


def FillGaps(ścieżka):
    File_list = Find_Files(p)[0]
    Original_File_List = Find_Files(p)[1]
    ToJoin = ""
    start = int(File_list[0][1])
    końcówka = start
    for File in range(len(File_list)):
        File_num = int(File_list[File][1])
        nFileName = f"{File_list[File][0]}{końcówka}{File_list[File][2]}"
        #print(f"{File} {File_num} {końcówka} --> {nFileName}")
        #print("".join(File),f"--> {nFileName}")
        if File_num != końcówka:
            print("".join(File_list[File]),f"--> {nFileName}")
            #print("".join(Original_File_List[File]),f"--> {nFileName}")#...............Jeśli podany plik istnieje to zmień nazwę na nFileName, jeśli plik ma w numeratorze 0 to je usuń
            if Path(f"{ścieżka}//{ToJoin.join(File_list[File])}").exists() == False:
                shutil.move(f"{ścieżka}\\{File_list[File][0]}{File_list[File][1][1]}{File_list[File][2]}",f"{ścieżka}\\{nFileName}" )
            else:
                shutil.move(f"{ścieżka}\\{ToJoin.join(File_list[File])}",f"{ścieżka}\\{nFileName}")    

        końcówka = końcówka + 1
FillGaps(p)
