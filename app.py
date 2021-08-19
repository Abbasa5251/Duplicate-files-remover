import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror, showinfo, askyesno
from pathlib import Path
import os
import hashlib

try:
    root = tk.Tk()
    root.iconbitmap("duplicate_files_remover.ico")
    root.withdraw()
    _continue = askyesno(
        title="ADev - Duplicate files remover",
        message="Any duplicate files will be deleted. Do you want to continue?",
    )

    if _continue:
        path = askdirectory(title="Select folder")
        print(path)
        files_lists = os.listdir(path)
        unique = dict()
        for file in files_lists:
            file_name = Path(os.path.join(path, file))
            if file_name.is_file():
                fileHash = hashlib.md5(open(file_name, "rb").read()).hexdigest()
                if fileHash not in unique:
                    unique[fileHash] = file_name
                else:
                    os.remove(file_name)
                    print(f"Successfully removed {file_name}")

        showinfo(
            title="ADev - Duplicate files remover",
            message="Script has executed successfully!",
        )

except Exception as e:
    showerror(
        title="ADev - Duplicate files remover",
        message=f"There was some error. Try again later\n{e}",
    )

# Pyinstaller Command
# pyinstaller -w --icon=duplicate_files_remover.ico --clean --add-data "duplicate_files_remover.ico;." app.py
