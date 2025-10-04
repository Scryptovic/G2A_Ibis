import requests
import os
import zipfile
import gzip
import shutil

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    with open(save_path, 'wb') as f:
        shutil.copyfileobj(response.raw, f)
    print(f"Downloaded {save_path}")
    return save_path

def unzip_file(zip_path, extract_to='.'):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Unzipped {zip_path} to {extract_to}")

def gunzip_file(gz_path, extract_to=None):
    if extract_to is None:
        extract_to = gz_path.replace('.gz','')
    with gzip.open(gz_path, 'rb') as f_in:
        with open(extract_to, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Extracted {gz_path} to {extract_to}")
