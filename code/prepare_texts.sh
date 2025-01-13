#!/bin/bash
# Script to download and prepare texts from Project Gutenberg
# Usage: ./prepare_texts.sh text_urls.txt output_directory/

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 text_urls.txt output_directory/"
  exit 1
fi

URLS_FILE=$1
OUTPUT_DIR=$2

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Download and clean texts
while IFS= read -r url; do
  echo "Downloading: $url"
  filename=$(basename "$url")
  wget -q "$url" -O "$OUTPUT_DIR/$filename"
  
  echo "Cleaning: $filename"
  # Remove Gutenberg header/footer and non-ASCII characters
  sed -n '/\*\*\* START OF/,/\*\*\* END OF/p' "$OUTPUT_DIR/$filename" \
    | tr -cd '\11\12\15\40-\176' > "$OUTPUT_DIR/cleaned_$filename"
  rm "$OUTPUT_DIR/$filename"
done < "$URLS_FILE"

echo "Texts downloaded and cleaned in $OUTPUT_DIR"

