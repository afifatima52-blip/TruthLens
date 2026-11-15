# TruthLens — Machine Learning Evaluation

## 1. Models Evaluated

The following three machine learning models were evaluated:

- Logistic Regression
- LinearSVC
- Tuned LinearSVC

## 2. Model Performance

| Model | Accuracy | Balanced Accuracy | Macro F1 |
| --- | ---: | ---: | ---: |
| Logistic Regression | 36.92% | 44.75% | 32.24% |
| LinearSVC | 43.40% | 38.34% | 36.14% |
| Tuned LinearSVC | 43.74% | 44.62% | 36.58% |

## 3. Hyperparameter Tuning

GridSearchCV was used to optimize the LinearSVC model.

The best parameters were:

- Best C: 0.1
- Cross-validation Macro F1: 33.42%

The tuned model achieved a higher Macro F1 score than the original LinearSVC model.

## 4. Error Analysis

The tuned LinearSVC model was evaluated on 3,816 test records.

- Total test records: 3,816
- Correct predictions: 1,669
- Incorrect predictions: 2,147
- Error rate: 56.26%

### Most Common Classification Errors

| Actual | Predicted | Count |
| --- | --- | ---: |
| False | Partly true/misleading | 220 |
| Partly true/misleading | False | 198 |
| True | False | 190 |
| False | True | 167 |
| True | Mostly true | 138 |

## 5. Key Findings

- Tuned LinearSVC achieved the highest Macro F1 score among the three evaluated models.
- The model struggles to distinguish between false, true, and partly true/misleading claims.
- Some minority classes have relatively low precision and recall.
- Class imbalance and multilingual text characteristics may affect model performance.

## 6. Limitations

- The dataset contains 13 languages and does not include Urdu.
- The model uses character-level TF-IDF features rather than deeper semantic representations.
- Classification results should not be treated as independent verification of real-world claims.
- Further experiments are required to improve reliability and generalization.

## 7. Conclusion

Tuned LinearSVC is the current best-performing baseline based on Macro F1 and accuracy.

However, its performance is not sufficient for reliable real-world claim verification. Further model development and evaluation are necessary before building the final TruthLens system.
