
# TruthLens — Exploratory Data Analysis Findings

## 1. Project Overview

TruthLens analyzes fact-checking claims across multiple languages to explore patterns in fact-check labels, languages, claimants, and review timelines.

## 2. Dataset Overview

- Total records: 19,079
- Original columns: 17
- Languages: 13
- Unique claimants: 4,673
- Dataset: X-FACT

## 3. Fact-Check Label Distribution

The dataset contains seven fact-check labels:

- False: 7,515
- Partly true/misleading: 4,359
- True: 4,080
- Mostly true: 1,380
- Mostly false: 848
- Complicated/hard to categorise: 540
- Other: 357

The distribution is imbalanced, with the False category having the highest number of records.

## 4. Missing Values and Data Quality

- Total missing cells: 1,485
- Missing-value percentage: approximately 0.458%
- Most missing values occur in evidence columns.
- Two claimant values are missing.
- The text value "none" appeared in date columns and was converted to missing datetime values.

## 5. Date Analysis

- Claim dates range from 18 October 2005 to 3 December 2108.
- Review dates range from 27 July 2009 to 26 November 2020.
- One suspicious future claim date was identified.
- 67 records have review dates earlier than their claim dates.

These records were flagged as date anomalies rather than automatically deleted.

## 6. Review Delay Analysis

The review delay was calculated using claim and review dates.

- Available delay records: 11,658
- Mean delay: approximately 6.10 days
- Median delay: 0 days
- Minimum: -32,870 days
- Maximum: 2,582 days

Negative values indicate date inconsistencies and require cautious interpretation.

## 7. Language Analysis

The dataset contains claims in 13 languages. Portuguese has the highest record count, followed by Indonesian and Arabic.

Language-level label distributions were explored using a heatmap, radar chart, and Sankey diagram.

## 8. Claimant Analysis

The top 15 named claimant entries were examined after excluding generic social-media entries.

The analysis shows that some claimant entries appear much more frequently than others.

## 9. Time-Based Patterns

Claim-year trends were explored for 2015–2020. Review activity was also examined across months and years.

## 10. Correlation Analysis

A correlation heatmap was created for selected numerical features.

Correlation indicates statistical association, not causation.

## 11. Key Limitations

- The dataset does not contain Urdu claims.
- Some evidence and date information is missing.
- The dataset has imbalanced labels.
- Date anomalies may affect timeline analysis.
- The dataset represents the available fact-check records, not every claim published online.
- Multilingual text processing requires language-aware methods.

## 12. Conclusion

The exploratory analysis reveals differences in fact-check label distributions, language representation, claimant activity, and review timelines.

These findings provide a foundation for the next stages of TruthLens: multilingual NLP, feature engineering, and machine learning.
