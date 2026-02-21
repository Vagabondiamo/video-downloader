# Script per creare .exe per Windows
# Eseguire su Windows: pip install pyinstaller && python build_exe.py

import subprocess
import sys
import os
import shutil

print("📦 Installo PyInstaller...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller", "-q"])

print("\n🚀 Creo l'eseguibile Windows...")

# Cancella vecchie build
if os.path.exists("build"):
    shutil.rmtree("build")
if os.path.exists("dist"):
    shutil.rmtree("dist")

# Comando PyInstaller
cmd = [
    "pyinstaller",
    "--onefile",           
    "--windowed",          
    "--name", "VideoDownloader",
    "--clean",
    "--add-data", "vddownloader;vddownloader",
    "--hidden-import=tkinter",
    "--hidden-import=yt_dlp",
    "vddownloader/app.py"
]

subprocess.check_call(cmd)

print("\n" + "="*50)
print("✅ Fatto!")
print("="*50)
print("Il file .exe si trova in: dist/VideoDownloader.exe")
