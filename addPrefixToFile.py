import shutil, os
from pathlib import Path
working_dir = Path.cwd() / "prefiksy"
prefiks = input("Podaj prefiks, który zostanie doklejony na początku nazwy pliku: ")
for file in os.listdir(working_dir):
    shutil.move(working_dir / file, working_dir / (prefiks+file))


