import random
def train_extractor(seqs, chr_dict, window=30):
    data = []
    for chr_name in chr_dict:
        for row in seqs.itertuples():
            if row[1] == chr_name:
                seq = chr_dict[chr_name][0].sequence
                center = int(row[4])
                data.append(seq[center - window:center + window])
    return data
def shades_extractor(seqs, chr_dict, window=150):
    data = []
    for chr_name in chr_dict:
        for row in seqs.itertuples():
            if row[1] == chr_name:
                seq = chr_dict[chr_name][0].sequence
                center = int(row[4])
                offset = random.randint(1, 10) * 100
                data.append(seq[(center - window*3) - offset:(center - window) - offset + 1])
                data.append(seq[(center + window) + offset:(center + window*3) + offset + 1])
    return data
