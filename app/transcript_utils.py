import re

def extract_patient_name(text):
    match = re.search(r'(Ms\.|Mr\.|Mrs\.)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', text)
    return match.group(2) if match else "Unknown"

def extract_patient_lines(text):
    return " ".join(re.findall(r'Patient:\s*(.*)', text))
