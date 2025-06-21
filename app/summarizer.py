from transformers import pipeline

summarizer=pipeline("summarization",model="facebook/bart-large-cnn")

def generate_summary(text):
    result=summarizer(text,max_length=150, min_length=40, do_sample=False)
    return result[0]['summary_text']
