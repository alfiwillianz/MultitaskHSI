#!/usr/bin/env bash
# ==============================================
# Download HyperspectralVectors dataset from HF
# ==============================================

set -e  # stop if any command fails

DATA_DIR="./data"
REPO_URL="https://huggingface.co/datasets/alfiwillianz/HyperspectralVectors/resolve/main"

# create dir if not exists
mkdir -p "$DATA_DIR"
cd "$DATA_DIR"

echo "📡 Downloading HyperspectralVectors dataset from Hugging Face..."

# CSV files
for file in \
  "df_field_b.csv" \
  "df_field_g.csv" \
  "df_screenh_b.csv" \
  "df_screenh_g.csv"
do
  echo "⬇️  Downloading $file ..."
  curl -L -O "${REPO_URL}/${file}"
done

echo "✅ All files downloaded to: $(pwd)"
