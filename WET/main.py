from data_loader import download_data, load_pbm
from models import train_models, model_utils

pbm_data = load_pbm.load_pbm_files("train/PBM")
test_sequences = load_pbm.load_test_fasta("PBM_participants.fasta")
pos = [seq for seq in pbm_data['LEUTX']['PBM']['pbm_sequence']]
neg = model_utils.generate_random_sequences(len(pos)*3, len(pos[0]))
model = train_models.train_model(pos, neg)
