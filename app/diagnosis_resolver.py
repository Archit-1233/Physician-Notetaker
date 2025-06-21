def load_diagnosis_terms(file_path="app/diagnosis_terms.txt"):
    with open(file_path, "r") as f:
        return [line.strip().lower() for line in f if line.strip()]

def extract_diagnosis(text, ner_entities, diagnosis_vocab, keywords=None):
    diagnosis_set = set()

    # 1. Extract from NER if present
    ner_diagnosis = ner_entities.get("Diagnosis", [])
    if ner_diagnosis:
        diagnosis_set.update([d.title() for d in ner_diagnosis])

    # 2. Use keyword matching if provided
    if keywords:
        for kw in keywords:
            if kw.lower() in diagnosis_vocab:
                diagnosis_set.add(kw.title())

    # 3. Fallback: Scan full text using diagnosis term list
    if not diagnosis_set:
        for term in diagnosis_vocab:
            if term in text.lower():
                diagnosis_set.add(term.title())

    return list(diagnosis_set) if diagnosis_set else ["Not mentioned"]
