#!/usr/bin/env python3
"""
Download HyperspectralVectors dataset from Hugging Face
Works on Windows, Mac, and Linux
"""

import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

def download_dataset():
    """Download dataset files from Hugging Face"""
    
    DATA_DIR = "data"
    REPO_URL = "https://huggingface.co/datasets/alfiwillianz/HyperspectralVectors/resolve/main"
    
    # Files to download
    files = [
        "df_field_b.csv",
        "df_field_g.csv",
        "df_screenh_b.csv",
        "df_screenh_g.csv"
    ]
    
    # Create directory if not exists
    Path(DATA_DIR).mkdir(exist_ok=True)
    
    print("📡 Downloading HyperspectralVectors dataset from Hugging Face...")
    print()
    
    failed_files = []
    
    for file in files:
        file_url = f"{REPO_URL}/{file}"
        file_path = os.path.join(DATA_DIR, file)
        
        try:
            print(f"⬇️  Downloading {file}...", end=" ", flush=True)
            urllib.request.urlretrieve(file_url, file_path)
            file_size = os.path.getsize(file_path) / (1024 * 1024)  # Size in MB
            print(f"✅ ({file_size:.2f} MB)")
        except urllib.error.URLError as e:
            print(f"❌ Failed")
            failed_files.append((file, str(e)))
        except Exception as e:
            print(f"❌ Error")
            failed_files.append((file, str(e)))
    
    print()
    
    if failed_files:
        print("❌ Some files failed to download:")
        for file, error in failed_files:
            print(f"  - {file}: {error}")
        return False
    else:
        data_path = os.path.abspath(DATA_DIR)
        print(f"✅ All files downloaded successfully to: {data_path}")
        print()
        
        # List downloaded files
        print("📂 Downloaded files:")
        for file in os.listdir(DATA_DIR):
            file_path = os.path.join(DATA_DIR, file)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path) / (1024 * 1024)
                print(f"  ✓ {file} ({size:.2f} MB)")
        return True

if __name__ == "__main__":
    try:
        success = download_dataset()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Download cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
