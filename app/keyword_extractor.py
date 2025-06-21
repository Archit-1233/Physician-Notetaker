from keybert import KeyBERT
kw_model = KeyBERT()

def extract_keywords(text, top_n=10):
    keywords = kw_model.extract_keywords(text, top_n=top_n, stop_words='english')
    return [kw[0] for kw in keywords]
