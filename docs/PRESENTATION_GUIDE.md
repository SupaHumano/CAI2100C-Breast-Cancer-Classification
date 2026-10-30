# Oral Presentation and Technical Q&A

**Project 1 | Breast Cancer Classification**  
**Juan Luna Santibanez**  
Miami Dade College · CAI2100C-2267-6908 · Machine Learning Foundations  
Professor Beth Muturi · October 2026

## 1. Problem and Objective

**Research question:** How accurately can K-Nearest Neighbors (KNN), Support Vector Machine (SVM), and Decision Tree classify labeled breast mass measurements as benign or malignant, and what do their mistakes reveal about reliability?

My objective is to compare three supervised classifiers on the same classroom dataset and test partition. I examine accuracy, class-specific recall, and confusion matrices rather than evaluating performance by a single number. I also investigate generalization with separate nested cross-validation experiments.

**Scope:** This is a reproducible educational analysis, not a medical diagnosis, screening, or treatment system.

## 2. Proposed Solution

I follow six stages of the machine learning project cycle:

| Stage | Implementation | Outcome |
|---|---|---|
| Problem scoping | Define a binary supervised classification objective | Predict the recorded `diagnosis` label |
| Data acquisition | Load the course-provided diagnostic CSV | 569 original observations |
| Data exploration | Check completeness, encode labels, visualize correlations | 543 complete observations |
| Modeling | Train KNN, SVM, and Decision Tree | Three classroom classifiers |
| Evaluation | Analyze accuracy, recall, and confusion matrices | Error-aware comparison on 109 test cases |
| Deployment | Present a reproducible educational visualization | No clinical predictions or patient data |

![Machine learning project cycle](../assets/workflow.svg)

## 3. Dataset and Preprocessing

The supplied dataset contains **569 rows and 32 columns**: the `id` identifier, the `diagnosis` target, and 30 numerical diagnostic features. There are **28 missing cells across 26 different rows**. After complete-case deletion, the dataset contains **543 records**, with **342 benign (B)** and **201 malignant (M)** labels.

I encode **B = 0** and **M = 1**, then create a seeded, stratified **434-row development / 109-row test** split. The test partition contains 69 benign and 40 malignant observations. The classroom approach keeps the input specification of the supplied course notebook. My separate research pipelines exclude administrative `id`, because it is not a biological measurement.

I fit scaling parameters using training data only for scale-sensitive models. The research notebook places preprocessing inside cross-validation pipelines to limit data leakage. I use correlations to explore patterns, not to claim causality.

![Dataset integrity](../assets/dataset-integrity.svg)

## 4. Methods

**KNN:** Compares a new observation with labeled neighbors in feature space. Distance and scaling influence the outcome. The classroom baseline uses two neighbors.

**SVM:** Learns a separating boundary with a margin-based objective. Standardized feature values help avoid undue influence from different measurement scales.

**Decision Tree:** Learns recursive feature-based splitting rules. Trees are interpretable but can overfit training samples; unpruned complexity must be checked against held-out performance.

I use a consistent classroom test set for all three classifiers, then distinguish the additional research design from the original classroom specification.

## 5. Results and Model Selection

### Classroom test: 109 cases

| Metric | KNN | SVM | Decision Tree |
|---|---:|---:|---:|
| Correct classifications | 104 | **108** | 101 |
| Test accuracy | 95.41% | **99.08%** | 92.66% |
| True negatives (TN) | 69 | 69 | 65 |
| False positives (FP) | 0 | 0 | 4 |
| False negatives (FN) | 5 | **1** | 4 |
| True positives (TP) | 35 | **39** | 36 |
| Malignant recall | 87.50% | **97.50%** | 90.00% |

In each confusion matrix, **rows are actual labels and columns are predicted labels**, ordered `[B, M]`. Thus `[[TN, FP], [FN, TP]]`. Here a false negative means an observation labeled malignant was predicted benign.

![Confusion matrices](../assets/confusion-matrices.svg)

### Development-only nested cross-validation

| Model | Mean accuracy | Mean malignant recall |
|---|---:|---:|
| KNN | 95.40% | 90.69% |
| **SVM** | **97.93%** | **95.05%** |
| Decision Tree | 95.86% | 92.56% |

Nested validation separates inner hyperparameter selection from four outer evaluation folds on the **434 development records**. This research specification excludes `id`. The 109-row holdout had already been examined; neither its 99.08% score nor the nested estimate represents prospective external clinical validation. These protocols should not be described as identical experiments.

![Nested validation](../assets/nested-cv.svg)

**Model selection:** SVM is the strongest of the three required candidates in the evaluated classroom split and has the highest mean nested accuracy in the additional research. I still report its false negative, the variability across validation folds, and the limitations of the dataset.

## 6. Technical Q&A

### Problem and data

**Q01. What problem am I solving?**  
I classify recorded breast mass measurements as benign or malignant and compare the reliability and errors of three supervised algorithms.

**Q02. Why is this supervised learning?**  
I use supervised learning because each training sample has numerical measurements and a known diagnosis label. I train the models to learn from these labeled examples.

**Q03. What is the target variable?**  
I predict the original `diagnosis` column, which I encode as benign `B = 0` and malignant `M = 1`. I use malignant as the positive class for recall and false negatives.

**Q04. Does malignant mean invasive breast cancer?**  
No. I use the dataset's benign and malignant labels; I cannot infer invasive status, disease stage or a complete clinical diagnosis from them.

**Q05. How much data did I start with?**  
I start with 569 records and 32 columns: 30 measurements, one administrative identifier and one diagnosis label.

**Q06. How much data remains after cleaning?**  
After removing 26 incomplete rows, I retain 543 observations: 342 benign and 201 malignant.

**Q07. Why were there 28 missing values but 26 removed rows?**  
I count 28 missing cells across 26 different rows because some rows contain more than one missing value.

**Q08. Why did I remove incomplete rows instead of imputing?**  
I remove incomplete rows to follow the classroom procedure and keep my baseline reproducible. I recognize that this discards information; if I test imputation separately, I must fit it on training folds only.

**Q09. Is the dataset balanced?**  
No. I have more benign than malignant observations, so I examine class-level recall and confusion matrices as well as accuracy.

**Q10. What does the correlation heatmap show?**  
I use the correlation heatmap to inspect statistical relationships among measurements. I do not interpret correlation as causation or clinical significance.

### Algorithms and training

**Q11. How is the data split?**  
I use a stratified 80/20 split with `random_state = 42`: 434 development observations and 109 held-out test observations.

**Q12. Why stratify?**  
I stratify the split to approximately preserve the benign/malignant proportions and reduce accidental differences in class distribution.

**Q13. Why keep a test set?**  
I keep a test partition separate from model fitting so I can evaluate predictions on held-out data. I recognize that repeated test-based selection would weaken that estimate.

**Q14. What is data leakage?**  
I understand data leakage as evaluation information influencing training or model selection. For example, I avoid fitting a scaler on all records before splitting.

**Q15. Why use StandardScaler?**  
I use StandardScaler because distances in KNN and optimization in SVM depend on feature scale. I fit the scaler on training data and transform the held-out data with the same parameters.

**Q16. How does KNN work?**  
I use KNN to assign a class based on nearby labeled training examples. My classroom baseline has `n_neighbors = 2`.

**Q17. How does SVM work?**  
I use SVM to learn a margin-based decision boundary between classes. I understand that observations near the boundary help determine the fitted classifier.

**Q18. How does Decision Tree work?**  
I use a Decision Tree to learn successive feature-based splitting rules. I check for overfitting because unrestricted trees can fit training patterns too closely.

**Q19. Why these three algorithms?**  
I compare these three algorithms because they represent distance-based, margin-based and rule-based approaches under the same classroom conditions.

**Q20. What are hyperparameters?**  
I understand hyperparameters as settings I choose before fitting, such as KNN neighbor count, SVM kernel and regularization, or tree depth. I distinguish them from parameters learned from the data.

**Q21. Why remove `id` from the research features?**  
I recognize `id` as an administrative identifier, not a biological measurement. I retain it only in the instructor-compatible classroom baseline and exclude it from my separate research experiments.

**Q22. What is a preprocessing pipeline?**  
I use a preprocessing pipeline to fit transformations together with the classifier. During cross-validation, I keep each fold's preprocessing inside its training partition to prevent leakage.

### Evaluation and interpretation

**Q23. What is accuracy?**  
I calculate accuracy as correct predictions divided by total predictions. My classroom SVM gets **108 / 109 = 99.08%**.

**Q24. What is a confusion matrix?**  
I read confusion matrices with actual classes as rows and predicted classes as columns. My classroom SVM matrix, ordered benign then malignant, is `[[69, 0], [1, 39]]`.

**Q25. What is a false negative?**  
I count a false negative when a malignant sample is predicted benign. In my test split, KNN has **5**, SVM has **1**, and Decision Tree has **4**.

**Q26. What is a false positive?**  
I count a false positive when a benign sample is predicted malignant. My test counts are **0 for KNN**, **0 for SVM**, and **4 for Decision Tree**.

**Q27. What is malignant recall?**  
I compute malignant recall as `TP / (TP + FN)`, the fraction of observed malignant samples found correctly. My results are **87.50% for KNN**, **97.50% for SVM** and **90.00% for Decision Tree**.

**Q28. What is precision?**  
I compute malignant precision as `TP / (TP + FP)`, the proportion of predicted malignant samples that really carry a malignant label.

**Q29. What is F1-score?**  
I use the F1-score, the harmonic mean of precision and recall, to summarize their balance. I still examine individual errors instead of relying on that score alone.

**Q30. Which model performed best?**  
I select SVM as the strongest of my three classroom models because it has the highest held-out accuracy and the fewest missed malignant cases. It also has the highest mean nested accuracy in my separate research analysis.

**Q31. Why not promise 99% accuracy?**  
I report 99.08% only for the particular 109-case classroom test set that I already examined. I do not promise the same accuracy on different data or in clinical practice.

**Q32. What is overfitting?**  
I describe overfitting as learning patterns that do not generalize well. My classroom Decision Tree reaches **100% training accuracy** but **92.66% test accuracy**, so I investigate that gap.

**Q33. What is cross-validation?**  
I use cross-validation to rotate training and validation folds on development data and examine how results vary across partitions.

**Q34. What is nested cross-validation?**  
I use inner folds to select hyperparameters and outer folds to evaluate that selection process. My optional research analysis uses four outer folds.

**Q35. Why are classroom and nested results different?**  
I distinguish the experiments because they use different model specifications and partitions. In my research notebook I remove `id` and use fold-contained preprocessing and tuning, so I do not treat the nested and classroom scores as interchangeable.

**Q36. What are the nested accuracy estimates?**  
On my 434-row development partition, I obtain mean nested accuracies of **95.40% for KNN**, **97.93% for SVM**, and **95.86% for Decision Tree** under the recorded research procedure.

### Extensions, limitations and deployment

**Q37. Which optional models did I examine?**  
I examine Logistic Regression and Random Forest as optional research comparisons. I do not present them as replacements for the three models required by Professor Muturi.

**Q38. Which additional transformations did I test?**  
I test robust scaling, the Yeo–Johnson power transformation, PCA, and SelectKBest. I compare them within my separate research validation protocol.

**Q39. Did every transformation improve the results?**  
No. In my research, the Yeo–Johnson SVM variant averages **98.16% nested accuracy**, while the SelectKBest variant averages approximately **94.47%**. I report both findings.

**Q40. Why not select a model using the already examined holdout?**  
I avoid repeated parameter selection using the already examined holdout because it would introduce selection bias and make the score look more optimistic.

**Q41. Why are false negatives important?**  
I pay attention to false negatives because they are malignant observations predicted benign. I cannot infer the medical consequences of these errors without separate clinical evidence.

**Q42. Can I claim this is a medical diagnostic device?**  
No. I present this project as an educational classification experiment, not a medical diagnostic device. I have not conducted external clinical validation or obtained approval for patient use.

**Q43. How would I deploy the educational system?**  
I would deploy an educational demonstration with a versioned notebook, a read-only interactive visualization, the documented preprocessing recipe and clearly stated limits. I would not use patient data or make live medical decisions.

**Q44. What would clinical deployment require?**  
Before any clinical use, I would require independent clinical cohorts, prospective validation, privacy safeguards, subgroup error analysis, clinical oversight, monitoring and applicable regulatory review.

**Q45. How is the work reproducible?**  
I make my work reproducible by preserving the original CSV and its SHA-256 checksum, my model settings, executed notebooks, result files, dependencies and the distinction between classroom and research evaluations.

## 7. Closing Statement

I compared three distinct supervised learning methods using a common educational dataset. SVM achieved the strongest classroom and nested-validation results among the assigned models. My main conclusion is that a credible machine learning result depends not only on accuracy, but also on correct data preparation, error analysis, evaluation design, and a clear boundary between classroom evidence and clinical use.

## Project Materials

[Academic Notebook](../academic/Project_1_Course_Submission.ipynb) · [Research Notebook](../notebooks/Project_1_Research_Validation.ipynb) · [Methodology](METHODOLOGY.md) · [Requirements](REQUIREMENTS.md) · [Interactive Presentation](../index.html)
