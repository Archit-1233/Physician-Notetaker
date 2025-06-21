from app.analyzer import analyze_medical_transcript

def read_transcript(file_path=r"C:\Users\agraw\OneDrive\Desktop\Physician_project\transcript.txt"):
    with open(file_path, "r") as f:
        return f.read()

if __name__ == "__main__":
    transcript = read_transcript()
    result = analyze_medical_transcript(transcript)

    import json
    print(json.dumps(result, indent=2))
