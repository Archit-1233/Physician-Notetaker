import re
import os

def load_phrases(file_name):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, file_name)

    # 🔍 Debug print for Streamlit logs
    print(f"🔍 Attempting to read file: {path}")
    print(f"📁 Directory contents of {base_dir}: {os.listdir(base_dir)}")

    if not os.path.isfile(path):
        raise FileNotFoundError(f"❌ File not found at: {path}")

    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def build_regex_from_phrases(phrases):
    return re.compile("|".join([re.escape(p) for p in phrases]), re.IGNORECASE)

def extract_current_status(text):
    status_phrases = load_phrases("status_phrases.txt")
    pattern = build_regex_from_phrases(status_phrases)
    match = pattern.search(text)
    return match.group().strip() if match else "Not mentioned"

def extract_prognosis(text):
    prognosis_phrases = load_phrases("prognosis_phrase.txt")
    pattern = build_regex_from_phrases(prognosis_phrases)
    match = pattern.search(text)
    return match.group().strip() if match else "Not mentioned"
