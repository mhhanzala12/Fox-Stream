import subprocess
import os

print("Installing pyinstaller...")
subprocess.run(["python", "-m", "pip", "install", "pyinstaller"], check=True)

print("Building with PyInstaller...")
cmd = [
    "python", "-m", "PyInstaller",
    "--noconfirm",
    "--onefile",
    "--windowed",
    "--name", "Fox-Stream",
    "--icon", "icon.ico",
    "--add-data", "icon.ico;.",
    "--collect-all", "customtkinter",
    "main.py"
]
subprocess.run(cmd, check=True)
print("Build complete! Executable is at dist/Fox-Stream.exe")