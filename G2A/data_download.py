import os
import requests
import zipfile
import gzip
from src.config import RAW_DIR, IBIS_URL, IBIS_FILE, HG38_BASE, CHROMOSOMES

def download_file(url, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        print(f"Downloading {url}...")
        response = requests.get(url)
        with open(path, "wb") as f:
            f.write(response.content)
    else:
        print(f"File already exists: {path}")

def unzip_file(path, extract_to=None):
    extract_to = extract_to or os.path.dirname(path)
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def gunzip_file(path):
    out_path = path.replace(".gz", "")
    if os.path.exists(out_path):
        return out_path
    with gzip.open(path, "rb") as f_in, open(out_path, "wb") as f_out:
        f_out.write(f_in.read())
    return out_path

def download_ibis():
    download_file(IBIS_URL, IBIS_FILE)
    unzip_file(IBIS_FILE)

def download_chromosomes():
    fasta_paths = {}
    for chrom in CHROMOSOMES:
        url = f"{HG38_BASE}/{chrom}.fa.gz"
        gz_path = os.path.join(RAW_DIR, f"{chrom}.fa.gz")
        download_file(url, gz_path)
        fasta_paths[chrom] = gunzip_file(gz_path)
    return fasta_paths
