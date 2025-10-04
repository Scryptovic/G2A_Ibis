import numpy as np
import random

def one_hot_encode(seq):
    mapping = {'A':0,'C':1,'G':2,'T':3,'a':0,'c':1,'g':2,'t':3}
    one_hot = np.zeros((len(seq),4), dtype=np.int8)
    for i, nuc in enumerate(seq):
        if nuc in mapping:
            one_hot[i, mapping[nuc]] = 1
    return one_hot

def generate_random_sequence(length):
    return ''.join(random.choices('ACGT', k=length))

def generate_random_sequences(num_sequences, sequence_length):
    return [generate_random_sequence(sequence_length) for _ in range(num_sequences)]
