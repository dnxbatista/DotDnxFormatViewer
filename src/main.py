import sys
import os
from utils.dotdnxconverter import *
import tkinter as tk
from tkinter import filedialog

def ConvertFileToDNX():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png, *.jpg, *.jpeg")])
    if file_path:
        #File Name get the file_path and remove the .png file extasion
        file_path_without_ext = os.path.splitext(file_path)[0]
        SaveFileAsDNX(file_path, file_path_without_ext + ".dnx")
    else:
        print("No file selected.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        OpenDNXFile(sys.argv[1])
    else:
        ConvertFileToDNX()

