# Reference: https://github.com/zqfang/GSEApy

import pandas as pd
import gseapy as gp
from gseapy import Msigdb
from multiprocessing import Pool
import os

def run_gsea(input_file, output_file):
    data = pd.read_csv(input_file, index_col=0)   
    genes_of_interest = list(data.index)  
    pathway_database = Msigdb().get_gmt(category='mh.all', dbver="2023.1.Mm") # Mouse hallmark gene sets
    gsea_results = gp.gsea(data=genes_of_interest,
                           gene_sets=pathway_database,
                           permutation_num=1000,
                           outdir=output_file_dir,
                           no_plot=True,
                           method='s2n', # signal_to_noise
                          )
    gsea_results.res2d.to_csv(output_file, sep='\t')

data_dir = '/Users/your_name/scRNAseq/data/'
result_dir = '/Users/your_name/scRNAseq/result/'

data_files = [data_dir + filename for filename in os.listdir(data_dir)]
result_files = [result_dir + "out_" + filename for filename in os.listdir(data_dir)]

# Parallel processing:
with Pool(16) as p:
    results = p.map(process_file, zip(data_files, result_files))
