
import streamlit as st
import joblib
import numpy as np
import tensorflow as tf
import unicodedata
import re

from pathlib import Path
from tensorflow.keras.preprocessing.sequence import pad_sequences


# ==================================================
# 1. PROJECT CONFIGURATION
# ==================================================

PROJECT_DIR = Path(__file__).resolve().parents[1]
MODELS_DIR = PROJECT_DIR / "models"

MAX_LENGTH = 100

st.set_page_config(
    page_title="TruthLens | Global Information Intelligence",
    page_icon="🔎",
    layout="wide"
)


# ==================================================
# 2. PROFESSIONAL DARK THEME
# ==================================================

st.markdown("""
<style>

.stApp {
    background-color: #101827;
    color: #F1F5F9;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3, h4, p, label {
    color: #F1F5F9 !important;
}

textarea {
    background-color: #1E293B !important;
    color: #FFFFFF !important;
    border: 1px solid #475569 !important;
}

textarea::placeholder {
    color: #94A3B8 !important;
}

div[data-baseweb="select"] > div {
    background-color: #1E293B !important;
    color: #FFFFFF !important;
}

.stButton > button {
    background-color: #2563EB;
    color: white;
    border: none;
    border-radius: 9px;
    min-height: 48px;
    font-size: 16px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #1D4ED8;
    color: white;
}

hr {
    border-color: #334155;
}

[data-testid="stTable"] {
    background-color: #1E293B;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# 3. LOAD ALL MODELS
# ==================================================

@st.cache_resource
def load_all_models():

    ml_model = joblib.load(
        MODELS_DIR / "tuned_linear_svc.pkl"
    )

    vectorizer = joblib.load(
        MODELS_DIR / "tfidf_vectorizer.pkl"
    )

    encoder = joblib.load(
        MODELS_DIR / "label_encoder.pkl"
    )

    original_lstm = tf.keras.models.load_model(
        MODELS_DIR / "original_lstm.keras",
        compile=False
    )

    weighted_lstm = tf.keras.models.load_model(
        MODELS_DIR / "class_weighted_lstm.keras",
        compile=False
    )

    tokenizer = joblib.load(
        MODELS_DIR / "lstm_tokenizer.pkl"
    )

    return (
        ml_model,
        vectorizer,
        encoder,
        original_lstm,
        weighted_lstm,
        tokenizer
    )


# ==================================================
# 4. NORMALIZE CLAIM
# ==================================================

def normalize_claim(text):

    text = unicodedata.normalize("NFC", text)

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


# ==================================================
# 5. LINEAR SVC PREDICTION
# ==================================================

def predict_linear_svc(
    claim,
    model,
    vectorizer,
    encoder
):

    claim_vector = vectorizer.transform([claim])

    prediction = model.predict(claim_vector)

    return encoder.inverse_transform(prediction)[0]


# ==================================================
# 6. LSTM PREDICTION
# ==================================================

def predict_lstm(
    claim,
    model,
    tokenizer,
    encoder
):

    sequence = tokenizer.texts_to_sequences(
        [claim]
    )

    padded_sequence = pad_sequences(
        sequence,
        maxlen=MAX_LENGTH,
        padding="pre",
        truncating="pre"
    )

    probabilities = model.predict(
        padded_sequence,
        verbose=0
    )

    predicted_index = np.argmax(
        probabilities,
        axis=1
    )

    return encoder.inverse_transform(
        predicted_index
    )[0]


# ==================================================
# 7. HEADER
# ==================================================

st.title("🔎 TruthLens")

st.subheader("GLOBAL INFORMATION INTELLIGENCE")

st.write(
    "Explore experimental machine learning and "
    "deep learning classifications of multilingual claims."
)

st.divider()


# ==================================================
# 8. CLAIM INPUT
# ==================================================

st.header("Analyze a Claim")

claim = st.text_area(
    "Enter your claim",
    placeholder="Write or paste a claim here...",
    height=150
)

st.caption(
    "Enter a claim to compare predictions from all three models."
)

analyze_button = st.button(
    "Compare All Models",
    use_container_width=True
)


# ==================================================
# 9. MODEL COMPARISON
# ==================================================

if analyze_button:

    if not claim.strip():

        st.warning(
            "Please enter a claim before analysis."
        )

    else:

        clean_claim = normalize_claim(claim)

        try:

            with st.spinner(
                "Analyzing claim with all three models..."
            ):

                (
                    ml_model,
                    vectorizer,
                    encoder,
                    original_lstm,
                    weighted_lstm,
                    tokenizer
                ) = load_all_models()

                original_prediction = predict_lstm(
                    clean_claim,
                    original_lstm,
                    tokenizer,
                    encoder
                )

                weighted_prediction = predict_lstm(
                    clean_claim,
                    weighted_lstm,
                    tokenizer,
                    encoder
                )

                svc_prediction = predict_linear_svc(
                    clean_claim,
                    ml_model,
                    vectorizer,
                    encoder
                )

            st.success(
                "Analysis completed successfully."
            )

            st.divider()

            st.header("Model Comparison")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.subheader("Original Bidirectional LSTM")

                st.metric(
                    label="Predicted Category",
                    value=original_prediction
                )

            with col2:

                st.subheader("Class-Weighted Bidirectional LSTM")

                st.metric(
                    label="Predicted Category",
                    value=weighted_prediction
                )

            with col3:

                st.subheader("Tuned LinearSVC")

                st.metric(
                    label="Predicted Category",
                    value=svc_prediction
                )

            st.divider()

            st.header("Prediction Summary")

            results = [
                {
                    "Model": "Original Bidirectional LSTM",
                    "Predicted Category": original_prediction
                },
                {
                    "Model": "Class-Weighted Bidirectional LSTM",
                    "Predicted Category": weighted_prediction
                },
                {
                    "Model": "Tuned LinearSVC",
                    "Predicted Category": svc_prediction
                }
            ]

            st.table(results)

        except Exception as error:

            st.error(
                "An error occurred while analyzing the claim."
            )

            st.exception(error)


# ==================================================
# 10. IMPORTANT NOTICE
# ==================================================

st.divider()

st.header("Important Notice")

st.info(
    "TruthLens provides experimental machine learning "
    "classifications. Its predictions do not establish "
    "whether a claim is factually true or false. Always "
    "consult reliable evidence and independent fact-checking sources."
)


# ==================================================
# 11. FOOTER
# ==================================================

st.divider()

st.subheader(
    "TruthLens | Global Information Intelligence"
)

st.markdown(
    "**_Created by Afifa Fatima_**"
)

st.caption(
    "Data Science Portfolio Project · 2026"
)
