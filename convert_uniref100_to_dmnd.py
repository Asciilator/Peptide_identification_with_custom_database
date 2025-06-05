# Before running this script, ensure you have downloaded the UniRef100 FASTA file
# and saved it as 'uniref100.fasta.gz' or 'uniref100.fasta' in the same directory as this script.

import os
import subprocess
import gzip
import shutil

# === CONFIG ===
compressed_fasta = "uniref100.fasta.gz"  # Downloaded file
fasta_input = "uniref100.fasta"          # Expected uncompressed file
dmnd_output = os.path.splitext(fasta_input)[0]
diamond_exe = "diamond.exe"              # Path to diamond binary

# === STEP 1: Decompress if needed ===
if not os.path.exists(fasta_input):
    if os.path.exists(compressed_fasta):
        print(f"Decompressing '{compressed_fasta}'...")
        with gzip.open(compressed_fasta, "rb") as f_in, open(fasta_input, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
        print(f"Decompressed to '{fasta_input}'")
    else:
        print(f"Neither '{fasta_input}' nor '{compressed_fasta}' found.")
        exit(1)

# === STEP 2: Build DIAMOND database ===
if os.path.exists(f"{dmnd_output}.dmnd"):
    print(f"DIAMOND database '{dmnd_output}.dmnd' already exists.")
else:
    print(f"Building DIAMOND database from '{fasta_input}'...")
    try:
        subprocess.run(
            [diamond_exe, "makedb", "--in", fasta_input, "-d", dmnd_output],
            check=True
        )
        print(f"DIAMOND database '{dmnd_output}.dmnd' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during DIAMOND database creation: {e}")
    except FileNotFoundError:
        print("diamond.exe not found — check path or filename.")
