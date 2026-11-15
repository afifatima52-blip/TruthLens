# TruthLens — Deep Learning Evaluation

## 1. Overview

This experiment evaluates Bidirectional LSTM neural networks for multilingual fact-check claim classification using the X-FACT dataset.

The dataset contains 19,079 claims across 13 languages and 7 fact-check labels.

## 2. Data Preparation

- Training records: 15,263
- Testing records: 3,816
- Number of classes: 7
- Tokenization: Character-level
- Vocabulary size: 375
- Maximum sequence length: 100 characters

A group-safe stratified train/test split was used to reduce duplicate-claim leakage.

## 3. Model Architecture

A Bidirectional LSTM neural network was developed using TensorFlow and Keras.

The architecture includes:

- Embedding layer with 64 dimensions
- Bidirectional LSTM with 64 units
- Dropout layers
- Dense layer with ReLU activation
- Softmax output layer with 7 classes

The model was trained using the Adam optimizer and sparse categorical cross-entropy loss.

## 4. Original LSTM Results

| Metric | Score |
| --- | ---: |
| Accuracy | 45.05% |
| Balanced Accuracy | 25.63% |
| Macro F1 | 24.46% |

The original model achieved 45.05% accuracy but failed to predict three minority classes.

## 5. Class-Weighted LSTM

Class weights were introduced to address class imbalance during training.

### Performance

| Metric | Score |
| --- | ---: |
| Accuracy | 27.02% |
| Balanced Accuracy | 40.92% |
| Macro F1 | 25.70% |

The class-weighted model successfully predicted all seven classes.

However, its overall accuracy decreased.

## 6. Model Comparison

| Metric | Original LSTM | Class-Weighted LSTM |
| --- | ---: | ---: |
| Accuracy | 45.05% | 27.02% |
| Balanced Accuracy | 25.63% | 40.92% |
| Macro F1 | 24.46% | 25.70% |

Class weighting improved balanced accuracy by 15.29 percentage points and Macro F1 by 1.24 percentage points.

This demonstrates a trade-off between overall accuracy and performance across different classes.

## 7. Comparison with Machine Learning Models

The best traditional machine learning baseline was Tuned LinearSVC.

| Model | Accuracy | Macro F1 |
| --- | ---: | ---: |
| Tuned LinearSVC | 43.74% | 36.58% |
| Original LSTM | 45.05% | 24.46% |
| Class-Weighted LSTM | 27.02% | 25.70% |

Tuned LinearSVC achieved the highest Macro F1 score among these three models.

## 8. Limitations

- Character-level sequences may lose important contextual information.
- The maximum sequence length of 100 may truncate longer claims.
- Class imbalance affects classification performance.
- The model does not independently verify the evidence behind claims.
- The dataset does not include Urdu.
- Further experiments are needed to improve multilingual semantic understanding.

## 9. Conclusion

The Bidirectional LSTM experiments demonstrate that deep learning can provide a useful comparison against traditional machine learning approaches.

Class weighting improved performance across minority classes, although overall accuracy decreased.

Tuned LinearSVC remains the stronger model based on Macro
