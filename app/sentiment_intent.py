from transformers import pipeline
sentiment_model=pipeline("sentiment-analysis")

def classify_sentiment(text):
    if not text.strip():
        return "Neutral"
    label=sentiment_model(text)[0]['label']
    if label=="POSITIVE":
        return "Reassured"
    else:
        return "Anxious"
    
def detect_intent(text):
    text_lower=text.lower()
    if any(w in text_lower for w in ["worried","concern","anxious","nervous"]):
        return "Seeking Reassurance"
    elif any(w in text_lower for w in ["pain","hurt","symptom","discomfort","ache"]):
        return "Reporting symptoms"
    elif any(w in text_lower for w in ["thank","good","fine","better","relief"]):
        return "Reassurance acknowledged"
    return "Unknown"

