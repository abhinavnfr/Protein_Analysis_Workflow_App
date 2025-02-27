# -*- coding: utf-8 -*-
"""fetch_FASTA_sequence.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UwdB5D-T7TTHxU8Cynx-OLjgPwaLoF3U
"""

!pip install biopython


from Bio import Entrez, SeqIO

def retrieve_fasta(accession):
    """
    Retrieves a FASTA sequence from the NCBI database.

    Parameters:
    accession (str): Accession number of the sequence.

    Returns:
    str: FASTA sequence.
    """
    Entrez.email = "abhinavrana18july@gmail.com"  # Replace with your email

    # Search for the accession in the NCBI database
    try:
        handle = Entrez.efetch(db="protein", id=accession, rettype="fasta", retmode="text")
        record = handle.read()
        handle.close()
        return record
    except Exception as e:
        return f"Failed to retrieve {accession}: {str(e)}"

def fetch_fasta_main():
    # Specify the file containing accession numbers
    file_path = input("Enter the path to the text file containing accession numbers: ")

    try:
        with open(file_path, 'r') as file:
            accessions = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("File not found. Please ensure the file path is correct.")
        return

    # Retrieve the FASTA sequences
    results = {}
    for accession in accessions:
        results[accession] = retrieve_fasta(accession)

    # Save the retrieved sequences to a file
    with open('sequences.fasta', 'w') as file:
        for accession, sequence in results.items():
            file.write(sequence + '\n')

    print("Sequences saved to sequences.fasta")

if __name__ == "__main__":
    fetch_fasta_main()
