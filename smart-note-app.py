import re
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

MIN_SENTENCES = 3
MAX_SENTENCES = 10
DEFAULT_SENTENCES = 5

TOP_TERMS = 10
WORDS_PER_MINUTE = 200

st.set_page_config(
    page_title="Smart Notes Summarizer",
    page_icon="📝",
    layout="wide"
)

st.markdown("""
<style>
    .stApp {
        background-color: #DDEBDD;
    }

    .main {
        background-color: #DDEBDD;
    }

    .stApp,
    .stApp p,
    .stApp span,
    .stApp label,
    .stApp div {
        color: #243B2A;
    }

    h1 {
        color: #234D2B !important;
        text-align: center;
        font-weight: 700;
    }

    h2 {
        color: #2F5D38 !important;
        font-weight: 650;
    }

    h3 {
        color: #356640 !important;
        font-weight: 600;
    }

    textarea {
        background-color: #F5FAF5 !important;
        color: #203326 !important;
        border: 2px solid #9CBD9F !important;
        border-radius: 12px !important;
        font-size: 16px !important;
    }

    textarea::placeholder {
        color: #718374 !important;
        opacity: 1 !important;
    }

    textarea:focus {
        border: 2px solid #6F9D75 !important;
        box-shadow: 0 0 6px #AFCDB2 !important;
    }

    [data-testid="stFileUploader"] {
        background-color: #CFE3D1;
        border: 2px dashed #7FA786;
        border-radius: 15px;
        padding: 18px;
    }

    [data-testid="stFileUploader"] label {
        color: #284A30 !important;
    }

    [data-testid="stSlider"] {
        background-color: #CFE3D1;
        padding: 12px 15px;
        border-radius: 12px;
    }

    [data-testid="stSlider"] label {
        color: #284A30 !important;
    }

    [data-testid="stMetric"] {
        background-color: #C8DFC9;
        padding: 18px;
        border-radius: 15px;
        border: 1px solid #9CBD9F;
    }

    [data-testid="stMetricLabel"] {
        color: #426348 !important;
    }

    [data-testid="stMetricValue"] {
        color: #234D2B !important;
        font-weight: 700;
    }

    [data-testid="stMetricDelta"] {
        color: #426348 !important;
    }

    [data-testid="stMarkdownContainer"] p {
        color: #243B2A !important;
        line-height: 1.6;
    }

    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    [data-testid="stAlert"][kind="info"] {
        background-color: #C9DFCC;
    }

    [data-testid="stAlert"][kind="success"] {
        background-color: #BFDDBF;
    }

    [data-testid="stAlert"][kind="warning"] {
        background-color: #E8E5BC;
    }

    [data-testid="stAlert"][kind="error"] {
        background-color: #E7C8C8;
    }

    [data-testid="stDataFrame"] {
        background-color: #F5FAF5;
        border-radius: 12px;
    }

    button {
        background-color: #9CBD9F !important;
        color: #1F3925 !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
    }

    button:hover {
        background-color: #7FA786 !important;
        color: #FFFFFF !important;
    }

    [data-testid="stFileUploader"] button {
        background-color: #8FB596 !important;
        color: white !important;
    }
    
    [data-testid="stFileUploader"] span{
        color: white !important;
    }
    
    [data-testid="stFileUploader"] small{
        color: white !important;
    }

    [data-testid="stFileUploader"] button:hover {
        background-color: #6F9D75 !important;
    }

    [data-testid="stVegaLiteChart"] {
        background-color: #CFE3D1;
        border-radius: 15px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

def get_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [
        sentence.strip()
        for sentence in sentences
        if len(sentence.strip()) >= 10
    ]
    return sentences

def get_scores(sentences):
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )
    matrix = vectorizer.fit_transform(sentences)
    scores = np.asarray(
        matrix.sum(axis=1)
    ).flatten()
    return scores, vectorizer, matrix

def make_summary(sentences, scores, number):
    important = np.argsort(scores)[::-1][:number]
    important = sorted(important)
    return [
        sentences[i]
        for i in important
    ]

def get_keywords(vectorizer, matrix):
    words = vectorizer.get_feature_names_out()
    scores = np.asarray(
        matrix.sum(axis=0)
    ).flatten()
    indexes = np.argsort(scores)[::-1][:TOP_TERMS]
    data = []
    for i in indexes:
        data.append({
            "Word": words[i],
            "Score": round(
                float(scores[i]),
                2
            )
        })
    return pd.DataFrame(data)

def get_stats(text, sentences):
    words = len(text.split())
    reading_time = max(
        1,
        round(
            words / WORDS_PER_MINUTE
        )
    )
    return (
        words,
        reading_time,
        len(sentences)
    )

st.title("📝 Smart Notes Summarizer")

st.write(
    "Upload a text file or paste your notes "
    "to generate a summary."
)

st.subheader("📂 Upload Your Notes")

uploaded_file = st.file_uploader(
    "Choose a .txt file",
    type=["txt"]
)

st.subheader("✏️ Or Paste Your Notes")

pasted_text = st.text_area(
    "Paste your notes here:",
    height=200,
    placeholder="Paste your lecture notes here..."
)

if uploaded_file is not None:
    try:
        text = uploaded_file.read().decode(
            "utf-8"
        )
        st.success(
            f"File uploaded successfully: "
            f"{uploaded_file.name}"
        )
    except UnicodeDecodeError:
        st.error(
            "Unable to read this file. "
            "Please upload a UTF-8 text file."
        )
        text = ""
else:
    text = pasted_text

number = st.slider(
    "📏 How many sentences should "
    "the summary contain?",
    MIN_SENTENCES,
    MAX_SENTENCES,
    DEFAULT_SENTENCES
)

if text.strip() == "":
    st.info(
        "Please upload a text file "
        "or enter your notes."
    )
else:
    sentences = get_sentences(text)
    if len(sentences) < 2:
        st.warning(
            "Please enter a longer text "
            "to create a summary."
        )
    else:
        st.write(
            f"📄 Total sentences: "
            f"{len(sentences)}"
        )
        try:
            scores, vectorizer, matrix = (
                get_scores(sentences)
            )
            summary = make_summary(
                sentences,
                scores,
                number
            )

            st.subheader("📌 Summary")
            
            for i, sentence in enumerate(
                summary,
                1
            ):
                st.write(
                    f"**{i}.** {sentence}"
                )

            keywords = get_keywords(
                vectorizer,
                matrix
            )

            st.subheader(
                "🔑 Important Words"
            )

            st.dataframe(
                keywords,
                use_container_width=True,
                hide_index=True
            )

            words, reading_time, total_sentences = (
                get_stats(
                    text,
                    sentences
                )
            )

            st.subheader(
                "📊 Statistics"
            )

            col1, col2, col3 = st.columns(3)
            col1.metric(
                "Words",
                words
            )
            col2.metric(
                "Reading Time",
                f"{reading_time} min"
            )
            col3.metric(
                "Sentences",
                total_sentences
            )
            st.subheader(
                "📈 Word Importance"
            )
            st.bar_chart(
                keywords.set_index(
                    "Word"
                )["Score"]
            )
        except ValueError:
            st.error(
                "Please enter more meaningful text to generate a summary."
            )