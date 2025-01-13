import os
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(file_path, output_dir):
    """Preprocess text by tokenizing, lemmatizing, and parsing word order."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    doc = nlp(text)
    processed_lines = []

    for sent in doc.sents:
        tokens = [token.text for token in sent]
        lemmas = [token.lemma_ for token in sent]
        parsed_order = " ".join([token.dep_ for token in sent])
        processed_lines.append({
            "sentence": sent.text,
            "tokens": tokens,
            "lemmas": lemmas,
            "parsed_order": parsed_order
        })

    output_path = os.path.join(output_dir, os.path.basename(file_path) + "_processed.json")
    with open(output_path, 'w', encoding='utf-8') as out_file:
        import json
        json.dump(processed_lines, out_file, indent=4)

    print(f"Processed text saved to: {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Preprocess Gutenberg texts.")
    parser.add_argument("input_dir", help="Directory containing cleaned texts.")
    parser.add_argument("output_dir", help="Directory to save processed files.")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    for filename in os.listdir(args.input_dir):
        if filename.startswith("cleaned_"):
            file_path = os.path.join(args.input_dir, filename)
            preprocess_text(file_path, args.output_dir)

