from src.download import download_ibis, download_chromosomes
from src.fasta_utils import load_fasta_sequences
from src.preprocess import generate_random_sequences, data_loader
from src.train import build_cnn

def main():
    download_ibis()
    fasta_paths = download_chromosomes()
    
    chr_dict = load_fasta_sequences(fasta_paths)
    pos = generate_random_sequences(100, 300)
    neg = generate_random_sequences(100, 300)
    X_train, X_test, y_train, y_test = data_loader(pos, neg)

    model = build_cnn(X_train.shape[1:])
    model.fit(X_train, y_train, epochs=3, batch_size=16, validation_data=(X_test, y_test))

if __name__ == "__main__":
    main()
