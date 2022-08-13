import shutil, os
from random import randint


folder = "D:\\jakub\\reddit\\sortowane"
def Create(number, path):
    for i in range(number):
        file = open(f"{path}\\spam{i+1}.txt",'w')
        file.write(f"Jestem {i+1}")
        file.close()

def Remove(path):
    for i in os.listdir(folder):
        os.unlink(f"{path}\\{i}")

Create(59, folder)
#Remove(folder)
