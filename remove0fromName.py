import shutil, os, re
from pathlib import Path



working_dir = Path("D:\\jakub\\reddit\\zera")
print(os.listdir(working_dir))
wzór = re.compile(r".*[0]+.*\..*")
for File_name in os.listdir(working_dir):
    if re.search(wzór, File_name) != None:
        newFile_name = re.split(r"[0]+", File_name, 1)
        newFile_name = "".join(newFile_name)
        shutil.move(working_dir / File_name, working_dir/newFile_name)
