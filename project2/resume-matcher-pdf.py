import r
import streamlit as st
from PyPDF2 import PdfReader

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------------
# PAGE TITLE
# -----------------------------------

st.title("📄 Resume Matcher")

st.write("Upload a resume and compare it with a job description.")


# -----------------------------------
# RESUME UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(
    "📤 Upload Resume PDF",
    type=["pdf"]
)


# -----------------------------------
# JOB DESCRIPTION
# -----------------------------------

job_description = st.text_area(
    "📝 Paste Job Description",
    height=200,
    placeholder="Paste the job description here..."
)


# -----------------------------------
# FUNCTION 1: EXTRACT PDF TEXT
# -----------------------------------

def extract_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


# -----------------------------------
# FUNCTION 2: CLEAN TEXT
# -----------------------------------

def clean_text(text):

    text = text.lower()

    # Remove email
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove URLs
    text = re.sub(r"https?://\S+", " ", text)

    # Remove phone numbers
    text = re.sub(r"\+?\d[\d\s-]{8,}\d", " ", text)

    # Remove punctuation
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# -----------------------------------
# FUNCTION 3: MATCH RESUME
# -----------------------------------

def match_resume(resume, job):

    # Convert text into TF-IDF vectors
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(
        [resume, job]
    )

    # Calculate similarity
    score = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]

    # Get all words
    words = vectorizer.get_feature_names_out()

    # Get job description word weights
    job_weights = vectors[1].toarray()[0]

    # Words present in resume
    resume_words = set(
        resume.split()
    )

    # Find missing keywords
    missing_words = []

    for word, weight in zip(words, job_weights):

        if weight > 0.1 and word not in resume_words:

            missing_words.append(word)

    return score, missing_words


# -----------------------------------
# MATCH BUTTON
# -----------------------------------

if st.button("🔍 Match Resume"):

    # Check inputs
    if uploaded_file is None:

        st.error("⚠️ Please upload a resume PDF.")

    elif job_description.strip() == "":

        st.error("⚠️ Please enter a job description.")

    else:

        # -----------------------------------
        # EXTRACT RESUME
        # -----------------------------------

        with st.spinner("Reading resume..."):

            resume_text = extract_text(
                uploaded_file
            )


        # -----------------------------------
        # CLEAN TEXT
        # -----------------------------------

        clean_resume = clean_text(
            resume_text
        )

        clean_job = clean_text(
            job_description
        )


        # -----------------------------------
        # MATCH RESUME
        # -----------------------------------

        with st.spinner("Matching resume with job..."):

            score, missing_words = match_resume(
                clean_resume,
                clean_job
            )


        # -----------------------------------
        # RESULT
        # -----------------------------------

        st.divider()

        st.subheader("📊 Match Result")


        # Convert score to percentage
        percentage = score * 100


        # Show score
        st.metric(
            "Resume Match Score",
            f"{percentage:.0f}%"
        )


        # -----------------------------------
        # MATCH STATUS
        # -----------------------------------

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


        # -----------------------------------
        # MISSING KEYWORDS
        # -----------------------------------

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


        # -----------------------------------
        # RESUME TEXT
        # -----------------------------------

        st.subheader(
            "📄 Resume Data"
        )

        with st.expander(
            "View Extracted Resume Text"
        ):

            st.write(
                resume_text
            )
