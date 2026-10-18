# Experimental Design and Reproducibility

## Data and target semantics

The instructor modified the Wisconsin Diagnostic Breast Cancer CSV. The labels `B` and `M` denote benign and malignant breast mass samples. They do not encode invasive and in-situ stages. The initial dataset has 569 records and 32 columns. There are 28 missing cells distributed across 26 rows. The course uses complete-case deletion and continues with 543 rows, 342 benign and 201 malignant.

## Classroom baseline

The course notebook reproduces the instructor's six-stage teaching sequence and three required algorithms. Its features follow the source classroom template, which includes administrative `id` as a numeric input. A seeded stratified 20% holdout contains 109 rows and a training partition contains 434 rows. Numeric features are scaled using the training data, and the same scaler transforms the holdout. The Decision Tree is fitted without scaling.

Because an ID number is not a biological measurement, the **research notebook separately excludes `id`**. This is an important methodological caveat. The two experiments must not be described as if they have exactly identical input specifications.

## Research-only evaluation

The research notebook builds pipelines that fit preprocessing **inside training folds** and evaluates KNN, SVM and Decision Tree using nested cross-validation on the development partition. Its four outer folds produce mean accuracies of 95.40%, 97.93% and 95.86%, respectively. Auxiliary five-fold comparisons, logistic regression, random forest, SVM feature-processing experiments and stability checks are optional research extensions. They do not replace the instructor's required three-model exercise.

The initial 109-row holdout had already been examined. Repeating model selection against those observations would increase the risk of optimistic reporting. Consequently, the 99.08% SVM holdout accuracy must never be presented as a fresh or independently generalizable prediction performance estimate.

## Scientific quality controls

- B means **benign**, and M means **malignant**.
- A false negative is a malignant sample that is predicted benign.
- `id` is excluded from the preferred research specification.
- Scaling, feature selection and hyperparameter fitting must remain inside training folds.
- Report negative or weaker outcomes alongside the strongest result.
- Avoid converting a favorable accuracy into a medical or clinical safety claim.
- Compare outcomes from the same experimental protocol, not from unrelated datasets.

## Data provenance

The CSV is retained byte-for-byte from the instructor's Project 1 Dependencies archive. The SHA-256 checksum is written in `data/SHA256.txt`. Reproducing the same split with a different dataset can change all model results.

## Deployment boundary

A responsible educational prototype could provide measured-feature entry, consistent preprocessing, model-version tracking, drift checks, access controls and clear limitations. Real clinical deployment is **not demonstrated or approved**. Independent patient cohorts, clinical validation, privacy protections and applicable regulatory review would be necessary before medical use.
