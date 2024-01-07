# Reference: https://fr.wikipedia.org/wiki/Variant_Call_Format#/media/Fichier:Binary_BCF_versus_VCF_format.png

import numpy as np

gene_expression_data = np.loadtxt("gene_expression.csv", delimiter=",", skiprows=1)
dna_sequences = np.loadtxt("dna_sequences.fasta", dtype="str")
vcf_data = np.loadtxt("variants.vcf", dtype="str", skiprows=7, usecols=range(9), delimiter="\t")
