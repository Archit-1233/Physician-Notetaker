import re
from transformers import pipeline

# Load biomedical NER model
ner_pipeline = pipeline("ner", model="d4data/biomedical-ner-all", aggregation_strategy="simple")

def extract_entities(text):
    entities = ner_pipeline(text)
    grouped = {
        "Symptoms": [],
        "Diagnosis": [],
        "Treatment": [],
        "Prognosis": []
    }

    replacements = {
        "painkill": "painkillers",
        "ph ys iotherapy": "physiotherapy",
        "physio therapy": "physiotherapy",
        "iotherapy": "physiotherapy",
        "stiff pain": "stiffness and pain",
        "ache pain": "body ache",
    }

    for ent in entities:
        word = ent["word"].replace("##", "").strip()
        label = ent["entity_group"].lower()

        # Clean non-alphabetic tokens
        word = re.sub(r"[^a-zA-Z\s\-]", "", word)
        word = re.sub(r"\s{2,}", " ", word).strip().lower()

        if len(word) < 2 or word in ["it", "ph", "ys", "tm"]:
            continue

        # Normalize common mis-splits
        if word in replacements:
            word = replacements[word]

        if "sign" in label or "symptom" in label:
            grouped["Symptoms"].append(word)
        elif "diagnosis" in label or "disease" in label or "condition" in label:
            grouped["Diagnosis"].append(word)
        elif "medication" in label or "procedure" in label or "therapy" in label:
            grouped["Treatment"].append(word)
        elif "prognosis" in label:
            grouped["Prognosis"].append(word)

    for key in grouped:
        grouped[key] = list(set(grouped[key]))

    return grouped
