# Reference: 
# https://fr.wikipedia.org/wiki/Variant_Call_Format#/media/Fichier:Binary_BCF_versus_VCF_format.png
# https://github.com/ScienceComputing/Python_Programming/blob/main/Utilities/NumPy/Create_Reshape_Array.py

import numpy as np

gene_expression = np.loadtxt("gene_expression.csv", delimiter=",", skiprows=1)
dna_sequence = np.loadtxt("dna_sequences.fasta", dtype="str")
vcf = np.loadtxt("variants.vcf", dtype="str", skiprows=7, usecols=range(9), delimiter="\t")
