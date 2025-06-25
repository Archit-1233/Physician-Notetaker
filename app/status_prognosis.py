import re
import os

def load_phrases(file_name):
    path = os.path.join(os.path.dirname(__file__), file_name)
    with open(path, 'r') as f:
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
