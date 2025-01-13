# Text Preprocessing Pipeline for Project Gutenberg

## Overview
This project automates the downloading, cleaning, and preprocessing of texts from Project Gutenberg for linguistic analysis. The pipeline extracts sentences, tokenizes, lemmatizes, and parses word order structures, enabling quantitative studies of grammatical innovation in multilingual contexts.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Workflow](#workflow)
- [Usage Examples](#usage-examples)
- [Output Format](#output-format)
- [Known Limitations](#known-limitations)

## Prerequisites

### System Requirements
- **Bash**: For running shell scripts (Linux/MacOS users)
- **Python 3.8+**: Core programming environment
- **Git**: For version control and project management
- **At least 2GB RAM**: For processing larger texts
- **Storage**: Minimum 1GB free space for text storage and processing

### Python Libraries
Required packages:
```bash
pip install -r requirements.txt
```

Contents of requirements.txt:
```
spacy>=3.5.0
pandas>=1.5.0
beautifulsoup4>=4.9.0
requests>=2.28.0
tqdm>=4.65.0
nltk>=3.8.0
```

Initialize spaCy model:
```bash
python -m spacy download en_core_web_sm
```

## Workflow

### Step 1: Project Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/gutenberg-preprocessing.git
cd gutenberg-preprocessing
```

2. Create virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
.\venv\Scripts\activate   # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Step 2: Prepare Text URLs
1. Create a text file named `text_urls.txt` with Project Gutenberg URLs:
```
https://www.gutenberg.org/files/1342/1342-0.txt
https://www.gutenberg.org/files/98/98-0.txt
```

2. Verify URL format:
```bash
python verify_urls.py text_urls.txt
```

### Step 3: Download and Clean Texts
Execute the preparation script:
```bash
chmod +x prepare_texts.sh  # Make script executable
./prepare_texts.sh text_urls.txt raw_texts/
```

The script performs:
- Downloads texts from provided URLs
- Removes Project Gutenberg headers and footers
- Cleans non-ASCII characters
- Normalizes whitespace and line endings

### Step 4: Preprocess Texts
Process the cleaned texts:
```bash
python preprocess_texts.py raw_texts/ processed_texts/
```

This step:
- Tokenizes sentences and words
- Performs lemmatization
- Generates dependency parses
- Exports structured JSON output

## Output Format
The preprocessing generates JSON files with the following structure:
```json
{
    "metadata": {
        "source_url": "https://www.gutenberg.org/files/1342/1342-0.txt",
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "processing_date": "2025-01-13",
        "word_count": 122204
    },
    "sentences": [
        {
            "sentence": "I have dreamed it.",
            "tokens": ["I", "have", "dreamed", "it", "."],
            "lemmas": ["I", "have", "dream", "it", "."],
            "parsed_order": "nsubj aux ROOT obj punct",
            "pos_tags": ["PRON", "AUX", "VERB", "PRON", "PUNCT"],
            "sentence_index": 1
        }
    ]
}
```

## Known Limitations

1. **OCR Quality**:
   - Project Gutenberg texts may contain scanning errors
   - Historical texts might use archaic spelling variants
   - Special characters may be inconsistently encoded

2. **Linguistic Processing**:
   - Dependency parsing accuracy varies with sentence complexity
   - Limited support for historical English variants
   - spaCy's English model may struggle with archaic constructions
   - Poetry and non-standard formatting may cause parsing errors

3. **Metadata Handling**:
   - Author and title extraction may be incomplete
   - Publication dates not automatically extracted
   - Genre classification requires manual input
   - Multiple editions not automatically differentiated

## Troubleshooting

### Common Issues
1. **URL Access Errors**:
   - Check internet connection
   - Verify Project Gutenberg server status
   - Ensure URL format is correct
   - Consider using a VPN if access is restricted

2. **Processing Errors**:
   - Increase memory allocation for large texts
   - Check disk space availability
   - Verify file permissions
   - Check Python version compatibility
