# 🔎 **TruthLens**

## **Global Information Intelligence**

**TruthLens** is a multilingual claim classification project that explores how Machine Learning and Deep Learning models classify online claims into fact-checking categories.

The project uses Natural Language Processing (NLP), text preprocessing, model training, evaluation, and an interactive Streamlit dashboard.

> **Important:** TruthLens provides experimental machine learning classifications. Its predictions do not establish whether a claim is factually true or false. Always consult reliable evidence and independent fact-checking sources.

---

## **Project Overview**

The goal of TruthLens is to explore multilingual claim classification using different machine learning approaches and compare their performance.

The project includes:

- Dataset exploration and preprocessing
- Exploratory Data Analysis (EDA)
- Natural Language Processing
- Text feature engineering
- Machine Learning classification
- Deep Learning with Bidirectional LSTM
- Model evaluation and error analysis
- Interactive Streamlit dashboard
- Three-model prediction comparison

## **Dataset**

TruthLens uses the **X-FACT dataset**.

- Total records: 19,079
- Total original columns: 17
- Languages: 13
- Classification categories: 7

**Languages:** Portuguese, Indonesian, Arabic, Georgian, Polish, Tamil, Spanish, Italian, Turkish, Hindi, German, Romanian, and Serbian.

**Dataset source:** [X-FACT on Hugging Face](https://huggingface.co/datasets/utahnlp/x-fact)

## **Classification Categories**

The dataset contains seven categories:

1. False
2. Partly true / misleading
3. True
4. Mostly true
5. Mostly false
6. Complicated / hard to categorise
7. Other

## **Technologies Used**

| Area | Technologies |
| :--- | :--- |
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Machine Learning | Scikit-learn |
| Deep Learning | TensorFlow, Keras |
| NLP | TF-IDF, Character-level Tokenization |
| Dashboard | Streamlit |
| Model Storage | Joblib |
| Development | VS Code, Jupyter Notebook |
| Environment | Conda |

## **Machine Learning Models**

The following models were evaluated:

- Logistic Regression
- Linear Support Vector Classifier (LinearSVC)
- Tuned LinearSVC

### **Machine Learning Results**

| Model | Accuracy | Balanced Accuracy | Macro F1 |
| :--- | ---: | ---: | ---: |
| Logistic Regression | 36.92% | 44.75% | 32.24% |
| LinearSVC | 43.40% | 38.34% | 36.14% |
| Tuned LinearSVC | 43.74% | 44.62% | 36.58% |

**Best Macro F1:** Tuned LinearSVC — 36.58%.

## **Deep Learning Models**

Two Bidirectional LSTM experiments were developed:

- Original Bidirectional LSTM
- Class-Weighted Bidirectional LSTM

### **Deep Learning Results**

| Model | Accuracy | Balanced Accuracy | Macro F1 |
| :--- | ---: | ---: | ---: |
| Original Bidirectional LSTM | 45.05% | 25.63% | 24.46% |
| Class-Weighted Bidirectional LSTM | 27.02% | 40.92% | 25.70% |

Class weighting improved balanced accuracy and Macro F1, but reduced overall accuracy.

## **Model Comparison Dashboard**

TruthLens includes an interactive Streamlit dashboard that compares predictions from three models:

1. Original Bidirectional LSTM
2. Class-Weighted Bidirectional LSTM
3. Tuned LinearSVC

Users can enter a claim and view all three model predictions together.

## **Project Structure**

```text
TruthLens/
│
├── data/
│   └── xfact_train.csv
│
├── notebooks/
│   ├── 01_dataset_loading.ipynb
│   ├── 02_nlp_feature_engineering.ipynb
│   ├── 03_machine_learning.ipynb
│   └── 04_deep_learning.ipynb
│
├── src/
│
├── models/
│
├── dashboard/
│   └── app.py
│
├── reports/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## **How to Run the Dashboard**

Activate the project environment:

```bash
conda activate truthlens_env
```

Run the Streamlit application from the project root:

```bash
python -m streamlit run dashboard/app.py
```

## **Limitations**

- Model performance is limited and varies across classification categories.
- The dataset contains an imbalanced distribution of labels.
- Multilingual text classification presents language-specific challenges.
- Predictions may be incorrect, even for scientifically established claims.
- Model outputs should not be treated as verified facts.

TruthLens is an experimental learning and portfolio project, not an independent fact-checking authority.

## **Project Reports**

Detailed evaluation and analysis reports are maintained in the `reports/` directory.

## **Author**

**Afifa Fatima**
Data Science Portfolio Project · 2026
