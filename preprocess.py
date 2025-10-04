import numpy as np
import random
from sklearn.model_selection import train_test_split

def one_hot_encode(seq):
    mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3,
               'a': 0, 'c': 1, 'g': 2, 't': 3}
    one_hot = np.zeros((len(seq), 4), dtype=np.int8)
    for i, nucleotide in enumerate(seq):
        if nucleotide in mapping:
            one_hot[i, mapping[nucleotide]] = 1
    return one_hot

def data_loader(pos, neg):
    labels = [1] * len(pos) + [0] * len(neg)
    sequences = pos + neg
    encoded = np.array([one_hot_encode(s) for s in sequences])
    return train_test_split(encoded, labels, test_size=0.2, random_state=42)

def generate_random_sequences(n, length):
    return [''.join(random.choices('ACGT', k=length)) for _ in range(n)]
