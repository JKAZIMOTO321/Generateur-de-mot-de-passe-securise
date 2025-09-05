import os
import sys
import subprocess

#configuration
script_name="main.py"
onefile=True
windowed=True
clean_build=True
name=True

#configuration du terminal
cmd=[
    "pyinstaller",
    "--noconfirm",
]
if onefile: cmd.append("--onefile")
if windowed: cmd.append("--windowed")
if clean_build: cmd.append("--clean")

cmd.append(script_name)
print("Generation de l'executable")
try:
    subprocess.run(cmd, check=True)
    print("Generation de l'executable termine")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de la generation: {e}")
except FileNotFoundError:
    print(f"le fichier est introuvable")

