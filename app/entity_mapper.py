# Map NER labels to desired output fields
NER_TO_OUTPUT = {
    "Sign_symptom": "Symptoms",
    "Therapeutic_procedure": "Treatment",
    "Medication": "Treatment",
    "Diagnosis": "Diagnosis"
}

def map_entities_to_fields(entities):
    result = {}
    for ner_label, terms in entities.items():
        output_key = NER_TO_OUTPUT.get(ner_label)
        if output_key:
            result.setdefault(output_key, []).extend(terms)
    # Deduplicate and sort
    for k in result:
        result[k] = sorted(set(result[k]))
    return result
