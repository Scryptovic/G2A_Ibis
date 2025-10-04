import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")

IBIS_URL = "https://ibis.autosome.org/IBIS_data/IBIS.train_data.Final.v1.zip"
IBIS_FILE = os.path.join(RAW_DIR, "IBIS.train_data.Final.v1.zip")

CHROMOSOMES = [
    "chr1", "chr3", "chr5", "chr7", "chr9",
    "chr11", "chr13", "chr15", "chr17", "chr19", "chr21"
]

HG38_BASE = "https://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes"
