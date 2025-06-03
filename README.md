# Peptide Identification with Custom Database

This project aims to identify peptides from a mass spectrometry (MS) sample using a **custom protein database**, constructed based on MS data itself by running one of the provided pipeline notebooks.

---

## Environment Setup

Install the required Python packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

**Minimum Python version:** 3.8+

**Required packages include:**

- pandas
- biopython
- numpy
- matplotlib
- seaborn
- requests
- tqdm
- ipython

Make sure your Python environment is active before running any scripts or notebooks.

---

## De novo peptide sequences 

Before running any pipeline you need to make sure that you have a csv file in this project folder with the de novo peptide sequences (e.g. de_novo_garmerwolde.csv). You can download the de_novo_garmerwolde and de_novo_sihumix_s05 dataframes with this link: https://drive.google.com/drive/u/0/folders/1wQ6kc7DY8mFSQwUB_uR8ttttQjqStv-S

## Before Running the DIAMOND Pipeline

Follow these steps to prepare your system for using the DIAMOND alignment tool:

1. **Disk Space**  
   Ensure **at least 500 GB of free disk space**:  
   - ~250 GB for `uniref100.fasta`  
   - ~250 GB for `uniref100.dmnd`

2. **Download DIAMOND**  
   Download the latest DIAMOND binary for Windows from:  
   [diamond-windows.zip](https://github.com/bbuchfink/diamond/releases/latest/download/diamond-windows.zip)  
   Extract `diamond.exe` into the root of this project folder.

3. **(Optional) PAM Matrix**  
   The PAM70 matrix can be downloaded automatically by running the pipeline, but if needed manually:  
   [PAM70.mat](https://raw.githubusercontent.com/hbckleikamp/NovoLign/main/PAM70.mat)

4. **Download UniRef100 Database**  
   Go to: [UniProt Download Help](https://www.uniprot.org/help/downloads)  
   Download: `uniref100.fasta.gz`  
   Decompress to get: `uniref100.fasta`  
   The download is large (~250 GB) and may take a few hours.

5. **Build the DIAMOND Database**  
   You can create the `.dmnd` file manually:
   ```bash
   diamond makedb --in uniref100.fasta -d uniref100
   ```
   Or run the provided Python script:
   ```bash
   python convert_uniref100_to_dmnd.py
   ```
   > Ensure `diamond.exe` is present in the same directory before executing this script.

---

## Running the DIAMOND Pipeline

Once you've completed the steps above you can run the DIAMOND-based peptide identification and clustering pipelines:

Notebooks:
- `pipeline_diamond.ipynb`
- `pipeline_diamond_proteomes.ipynb`
- `pipeline_diamond_improved.ipynb`
- `diamond_clustering.ipynb`

Each notebook contains step-by-step documentation to guide you through the process.

---

## Clustering with MMseqs2

You can cluster your protein FASTA databases using **MMseqs2**, which allows efficient identity-based clustering.

### Prerequisites

1. **Install WSL (Windows Subsystem for Linux)**  
   Follow the official guide:  
   [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

2. **Install MMseqs2 inside WSL**  
   Open your WSL terminal (e.g., Ubuntu) and run:
   ```bash
   sudo apt update
   sudo apt install mmseqs2
   ```

3. **Ensure FASTA input is accessible via Windows paths**  
   Example: `C:/Users/YourName/Documents/input.fasta`  
   This will be automatically converted to a WSL path in the script.

4. **Install Python packages**  
   Already handled via `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

---

### Running the MMseqs2 Clustering Pipeline

Open the notebook `mmseq_clustering.ipynb` and follow these steps:

1. **Set the path to your input FASTA file (Windows path):**
   ```python
   input_fasta_win = r"C:\Path\To\Your\input.fasta"
   ```

2. **Adjust the identity threshold (optional):**
   ```python
   identity_threshold = 50  # clustering threshold in %
   ```

3. **Run all notebook cells**  
   The notebook performs:
   - FASTA path conversion to WSL format
   - MMseqs2 clustering
   - Generation of cluster representatives
   - Header enrichment with cluster info
   - Output of final clustered FASTA file

4. **Output File Example:**
   ```
   input_clustered50_with_metadata.fasta
   ```
   Each sequence header will contain cluster ID, member list, and original metadata.

---

## Troubleshooting

If you encounter errors:

- Double-check that all file paths are correct
- Ensure WSL is installed and that `mmseqs` runs correctly in a WSL terminal
- Make sure `diamond.exe` is located in the project folder when using DIAMOND
- Use raw strings for Windows paths in Python (`r"C:\Path\..."`)

---

