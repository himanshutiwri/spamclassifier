import nltk
import os

# Folder to store NLTK datasets
nltk_data_dir = os.path.join(os.path.dirname(__file__), "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

# Read datasets from nltk.txt
with open("nltk.txt") as f:
    datasets = f.read().splitlines()

# Download each dataset
for dataset in datasets:
    try:
        nltk.download(dataset, download_dir=nltk_data_dir)
        print(f"Downloaded: {dataset}")
    except:
        print(f"Failed to download: {dataset}")
