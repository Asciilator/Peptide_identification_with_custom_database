# Peptide_identification_with_custom_database
This project aims to identify peptides from a mass spectrometry (MS) sample using a self made database, which is constructed based on the MS data itself. 
You can download the folder with the fasta files for the top 5 taxa and the file with the resulting custom database with this link: https://drive.google.com/drive/u/0/folders/1Uh7Fbm5oxUXjPZbeHBl6Yped3VVmJdNf 

Before running the diamond pipeline, follow these steps (if not done already):
1. Make sure you have at least 500 GB of disk space, since you need around 250 GB for the uniref100.fasta and 250 GB for the uniref100.dmnd.
2. You can choose to download the newest release of the software tool Diamond via this link: https://github.com/bbuchfink/diamond/releases/latest/download/diamond-windows.zip and extract the diamond.exe file to the project folder. You can also download the PAM70.mat file with this link: https://raw.githubusercontent.com/hbckleikamp/NovoLign/main/PAM70.mat. However, this will also be done for you while running the diamond pipeline.
3. Download the uniref100 database (containing all sequences in the UniProt knowlegdebase) in fasta format. You can do so using the following link: https://www.uniprot.org/help/downloads  
4. Decompress the uniref100.fasta.gz file and convert the uniref100.fasta file to a uniref100.dmnd file. You can do this manually using a command prompt or terminal. You can also run the code in the convert_uniref100_to_dmnd.py file in this project folder, but make sure you have diamond.exe in your project folder before running this code.   


Before clustering any of your databases, follow these steps (if not done already):
