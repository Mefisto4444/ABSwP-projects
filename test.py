import os
def Cr(path:str):
    hFile = open(f"{path}\\ukryty.txt",'w')
    hFile.write("Test ukrytego pliku.")
    os.system("attrib +h ukryty.txt")
    hFile.close()
    print(hFile.name)
Cr("D:\\jakub\\reddit")
def Op(path:str):
    hFile = open(f"{path}",'r+')
    print(hFile.read())