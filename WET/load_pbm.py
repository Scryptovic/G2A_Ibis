import pandas as pd
from fasta_reader import read_fasta

def load_pbm_files(base_path):
    tf_dict = {}
    tf_names = ["GCM1","MKX","MSANTD1","MYPOP","SP140L","TPRX1","ZFTA"]
    for tf in tf_names:
        seq_file = f"{base_path}/{tf}/QNZS_{tf}.tsv"
        sd_file  = f"{base_path}/{tf}/SD_{tf}.tsv"
        tf_dict[tf] = {
            "PBM": pd.read_csv(seq_file, sep='\t'),
            "SD": pd.read_csv(sd_file, sep='\t')
        }
    return tf_dict

def load_test_fasta(path):
    return [item for item in read_fasta(path)]
