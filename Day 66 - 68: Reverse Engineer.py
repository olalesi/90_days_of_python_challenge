## pip install pyinstxtractor uncompyle6

import os
import sys
import subprocess
from pathlib import Path

def extract_exe(exe_file):
    """Extracts the contents of a PyInstaller-packed EXE using pyinstxtractor"""
    print("[+] Extracting EXE file...")
    subprocess.run(["python", "-m", "pyinstxtractor", exe_file])

def find_main_pyc(extracted_folder):
    """Finds the main Python bytecode file in the extracted folder"""
    extracted_path = Path(extracted_folder)
    for file in extracted_path.glob("**/*.pyc"):
        if "main" in file.name.lower():  # Look for the main script
            return file
    return None

def decompile_pyc(pyc_file):
    """Decompiles the .pyc file into a readable .py file using uncompyle6"""
    print(f"[+] Decompiling {pyc_file} ...")
    decompiled_file = pyc_file.with_suffix(".py")  # Change .pyc to .py
    subprocess.run(["uncompyle6", "-o", str(decompiled_file.parent), str(pyc_file)])
    return decompiled_file

def main():
    if len(sys.argv) != 2:
        print("Usage: python reverse_engineer.py <target.exe>")
        sys.exit(1)

    exe_file = sys.argv[1]
    if not Path(exe_file).exists():
        print("[-] EXE file not found!")
        sys.exit(1)

    # Step 1: Extract EXE
    extract_exe(exe_file)

    # Extracted folder name (Pyinstxtractor names it <exe_name>_extracted)
    extracted_folder = f"{exe_file}_extracted"
    
    # Step 2: Find the main PYC file
    main_pyc = find_main_pyc(extracted_folder)
    if main_pyc:
        print(f"[+] Found main PYC file: {main_pyc}")
        
        # Step 3: Decompile the .pyc file
        decompiled_py = decompile_pyc(main_pyc)
        print(f"[+] Decompiled Python file saved as: {decompiled_py}")
    else:
        print("[-] No main Python script found in extracted files.")

if __name__ == "__main__":
    main()
## Run: python reverse_engineer.py target.exe
