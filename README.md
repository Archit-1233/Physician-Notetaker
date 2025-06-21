# 🩺 Physician Notetaker AI App
This project is an AI-powered tool designed to extract structured medical notes (like symptoms, diagnosis, treatment, etc.) from unstructured physician-patient conversation transcripts. Built for the AI Engineer Intern assignment.

# 🌐 Live App
👉 Click here to try the live app
https://archit-1233-physician-notetaker-app-do9eqn.streamlit.app/

# 🧠 Features
Automatically extracts:

✅ Patient Name

✅ Symptoms

✅ Diagnosis

✅ Treatment

✅ Prognosis & Current Status

✅ Sentiment & Intent

✅ Summary & Keywords

Utilizes transformer-based NLP models for biomedical text understanding.

# 🖥️ How to Run Locally
1️⃣ Clone the repo

git clone https://github.com/your-username/Physician-Notetaker.git


2️⃣ Create a virtual environment

python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run the app

streamlit run app.py

# 📸 Sample Output
Here are some screenshots of the app in action:

![Screenshot 2025-06-21 220841](https://github.com/user-attachments/assets/146beca3-2689-4249-9881-ecfecf3bbb05)
![Screenshot 2025-06-21 220904](https://github.com/user-attachments/assets/a07da3b6-a0da-42c3-bf53-c6e642e94560)
![Screenshot 2025-06-21 220925](https://github.com/user-attachments/assets/1ead2bef-6337-4091-9695-fa9ed090b330)
![Screenshot 2025-06-21 220940](https://github.com/user-attachments/assets/ba73f775-8a5a-4ea9-b0ba-404563f58958)

# 🛠️ Tech Stack Used
Python

Streamlit – for the UI

Transformers (HuggingFace) – for NER, summarization, and sentiment

KeyBERT – for keyword extraction

Regex – for pattern extraction

# 🧩 Methodology
NER: Extracts medical entities like symptoms, treatment, diagnosis.

Summarization: Converts full transcript to concise summary.

Custom Regex + Keyword Matching: Enhances accuracy of structured field extraction.

Sentiment & Intent Detection: Determines emotional tone and intent using AI.








