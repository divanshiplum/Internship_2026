import re
import streamlit as st
from PyPDF2 import PdfReader

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("📄 Resume Matcher")

st.write("Upload a resume and compare it with a job description.")

uploaded_file = st.file_uploader(
    "📤 Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "📝 Paste Job Description",
    height=200,
    placeholder="Paste the job description here..."
)

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\S+@\S+", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"\+?\d[\d\s-]{8,}\d", " ", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def match_resume(resume, job):
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(
        [resume, job]
    )

    score = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]

    words = vectorizer.get_feature_names_out()

    job_weights = vectors[1].toarray()[0]

    resume_words = set(
        resume.split()
    )

    missing_words = []

    for word, weight in zip(words, job_weights):
        if weight > 0.1 and word not in resume_words:
            missing_words.append(word)
    return score, missing_words

if st.button("🔍 Match Resume"):
    if uploaded_file is None:
        st.error("⚠️ Please upload a resume PDF.")
    elif job_description.strip() == "":
        st.error("⚠️ Please enter a job description.")
    else:
        with st.spinner("Reading resume..."):
            resume_text = extract_text(
                uploaded_file
            )

        clean_resume = clean_text(
            resume_text
        )

        clean_job = clean_text(
            job_description
        )

        with st.spinner("Matching resume with job..."):
            score, missing_words = match_resume(
                clean_resume,
                clean_job
            )

        st.divider()

        st.subheader("📊 Match Result")

        percentage = score * 100

        st.metric(
            "Resume Match Score",
            f"{percentage:.0f}%"
        )

        if score >= 0.70:
            st.success(
                "🎉 Excellent Match!"
            )
        elif score >= 0.50:
            st.warning(
                "👍 Good Match!"
            )
        else:
            st.error(
                "❌ Low Match"
            )

        st.subheader(
            "🔍 Missing Keywords"
        )

        if len(missing_words) > 0:
            st.write(
                ", ".join(missing_words)
            )
        else:
            st.success(
                "🎉 No important keywords missing!"
            )

        st.subheader(
            "📄 Resume Data"
        )

        with st.expander(
            "View Extracted Resume Text"
        ):

            st.write(
                resume_text
            )