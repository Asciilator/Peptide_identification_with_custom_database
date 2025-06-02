import os
import subprocess

# CHANGE THIS LINE ONLY to switch input FASTA file
fasta_input = "uniref100.fasta"  # Make sure this file exists in the same directory

# Define DIAMOND database name (remove extension)
dmnd_output = os.path.splitext(fasta_input)[0]  # e.g., "uniref100"

# Path to diamond executable
diamond_exe = "diamond.exe"  # Adjust if it's in a different directory

# Check if DIAMOND database already exists
if os.path.exists(f"{dmnd_output}.dmnd"):
    print(f"DIAMOND database '{dmnd_output}.dmnd' already exists")
else:
    print(f"Building DIAMOND database from '{fasta_input}'...")
    
    try:
        subprocess.run(
            [diamond_exe, "makedb", "--in", fasta_input, "-d", dmnd_output],
            check=True
        )
        print(f"DIAMOND database '{dmnd_output}.dmnd' created successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error during DIAMOND database creation: {e}")
    except FileNotFoundError:
        print("diamond.exe not found — make sure it is in your project directory or update the path.")