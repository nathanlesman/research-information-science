# Text Preprocessing Pipeline for Project Gutenberg

## Overview

This project automates the downloading, cleaning, and preprocessing of texts from Project Gutenberg for linguistic analysis. The pipeline extracts sentences, tokenizes, lemmatizes, and parses word order structures, enabling quantitative studies of grammatical innovation in multilingual contexts.

---

## Workflow

### Step 1: Setup Environment
Before starting, ensure you have the necessary tools and dependencies installed:

#### System Requirements
- **Bash**: To run shell scripts (Linux/MacOS users).
- **Python 3.8+**: Install Python if it's not already available.

#### Python Libraries
Install the required Python libraries:
```bash
pip install spacy


### Step 2: Prepare Text URLs
Create a text file named text_urls.txt with URLs of the Project Gutenberg texts you want to process. Wach URL should be on a new line

### Step 3: Download and clean texts
Run the prepare_texts.sh script to download the texts and clean them by removing Project Gutenberg headers, footers and non ASCII characters

with the command: ./prepare_texts.sh text_urls.txt raw_texts/


### Step 4: Preprocess Texts
Run the preprocess_texts.py script to tokenize, lemmatize, and parse cleaned texts

command: python preprocess_texts.py raw_texts/ processed_texts/

example output: [
    {
        "sentence": "I have dreamed it.",
        "tokens": ["I", "have", "dreamed", "it", "."],
        "lemmas": ["I", "have", "dream", "it", "."],
        "parsed_order": "nsubj aux ROOT obj punct"
    },
    {
        "sentence": "She gave me the diamond.",
        "tokens": ["She", "gave", "me", "the", "diamond", "."],
        "lemmas": ["she", "give", "I", "the", "diamond", "."],
        "parsed_order": "nsubj ROOT obj det pobj punct"
    }
]

### Step 5: Analyze Results
Once the data is preprocessed load the JSON files into your statistical analysis tools or python scripts for further analysis. It is recommended to use python libraries like pandas, scikit-learn or matplotlib for visualization and modeling

### Limitations: 
1. OCR Errors: Text from Project Gutenberg may contain scanning or formatting erros.
2. Parsing Accuracy: Dependency parsing relies on spaCy's English model, which might not handle complex or archaic sentence structures effectively
3. Metadata: Additional metadata is not automatically extracted and must be provided seperately

