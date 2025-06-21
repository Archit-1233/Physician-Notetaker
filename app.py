import streamlit as st

from app.analyzer import analyze_medical_transcript

# Page config
st.set_page_config(page_title="Medical Transcript Analyzer", layout="wide")
st.title("🩺 Medical Transcript Analyzer")
st.markdown("Analyze doctor-patient conversations to extract structured insights.")

# Input section
uploaded_file = st.file_uploader("Upload a transcript (.txt)", type=["txt"])
text_input = st.text_area("Or paste transcript text here:", height=300)

# Button and result
if st.button("🔍 Analyze"):
    if uploaded_file is not None:
        transcript = uploaded_file.read().decode("utf-8")
    elif text_input.strip():
        transcript = text_input
    else:
        st.warning("Please upload or paste a transcript.")
        st.stop()

    with st.spinner("Analyzing transcript..."):
        result = analyze_medical_transcript(transcript)

    # Show results
    st.success("Analysis complete!")
    st.subheader("📝 Summary")
    st.write(result["Summary"])
    st.subheader("🩺 Extracted Info")
    st.write("**Patient Name:**", result["Patient_Name"])
    st.write("**Symptoms:**", ", ".join(result["Symptoms"]))
    st.write("**Diagnosis:**", ", ".join(result["Diagnosis"]))
    st.write("**Treatment:**", ", ".join(result["Treatment"]))
    st.write("**Current Status:**", result["Current_Status"])
    st.write("**Prognosis:**", result["Prognosis"])
    st.write("**Sentiment:**", result["Sentiment"])
    st.write("**Intent:**", result["Intent"])
    st.subheader("🗝️ Keywords")
    st.write(", ".join(result["Keywords"]))
    st.subheader("🧾 Full JSON")
    st.json(result)
