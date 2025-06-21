from .entity_extractor import extract_entities
from .diagnosis_resolver import load_diagnosis_terms, extract_diagnosis
from .summarizer import generate_summary
from .keyword_extractor import extract_keywords
from .sentiment_intent import classify_sentiment, detect_intent
from .status_prognosis import extract_current_status, extract_prognosis
from .transcript_utils import extract_patient_name, extract_patient_lines

def analyze_medical_transcript(transcript):
    diagnosis_vocab = load_diagnosis_terms()
    patient_name = extract_patient_name(transcript)
    entities = extract_entities(transcript)
    keywords = extract_keywords(transcript)
    summary_text = generate_summary(transcript)
    patient_text = extract_patient_lines(transcript)

    result = {
        "Patient_Name": patient_name,
        "Symptoms": entities["Symptoms"],
        "Diagnosis": extract_diagnosis(transcript, entities, diagnosis_vocab, keywords),
        "Treatment": entities["Treatment"],
        "Current_Status": extract_current_status(transcript),
        "Prognosis": extract_prognosis(transcript),
        "Summary": summary_text,
        "Keywords": keywords,
        "Sentiment": classify_sentiment(patient_text),
        "Intent": detect_intent(patient_text)
    }
    return result