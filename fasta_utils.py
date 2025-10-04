from fasta_reader import read_fasta

def load_fasta_sequences(fasta_paths):
    chr_dict = {}
    for chrom, path in fasta_paths.items():
        chr_dict[chrom] = [item for item in read_fasta(path)]
    return chr_dict
