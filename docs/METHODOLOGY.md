# My Experimental Design and Reproducibility

**Juan Luna Santibanez** · Miami Dade College · CAI2100C · Professor Beth Muturi

## My data and target

I use the instructor-modified Wisconsin Diagnostic Breast Cancer CSV, without substituting the unmodified online dataset. I interpret `B` as **benign** and `M` as **malignant** breast mass samples; these are not labels for invasive versus in-situ stages.

I start with **569 records and 32 columns**. I find **28 missing cells across 26 records**. Following the course notebook's complete-case approach, I retain **543 records**: **342 benign** and **201 malignant**.

## My required classroom baseline

I keep the **six original teaching stages** and train the **three required models: KNN, SVM and Decision Tree**. I preserve the instructor's classroom input specification, including the administrative `id` column, to maintain consistency with that teaching baseline. I do not treat `id` as a biological measurement.

I create a seeded, stratified 80/20 split: **434 development records** and **109 held-out test records**. I fit the scaler only on the training data and use it to transform the test data. I train the Decision Tree on the unscaled numeric features. I compare the models using the same test records, class-level metrics and confusion matrices.

| My classroom model | Held-out accuracy | Missed malignant samples |
|---|---:|---:|
| KNN | 95.41% | 5 |
| SVM | **99.08%** | **1** |
| Decision Tree | 92.66% | 4 |

I select **SVM** as the strongest of these three classroom baselines on the documented split. I do not interpret its 99.08% as a clinical performance guarantee.

## My separate research evaluation

In my optional research notebook, I remove the non-clinical `id` and fit preprocessing and hyperparameters **inside training folds**. I run nested cross-validation on the development partition and obtain mean accuracies of **95.40% (KNN)**, **97.93% (SVM)** and **95.86% (Decision Tree)**. I also document optional logistic regression, random forest, feature-processing tests and stability checks.

I had already examined the original 109-case holdout when preparing the classroom baseline. I therefore avoid selecting or repeatedly tuning a research model on those held-out cases; I report the holdout and development-only experiments separately.

## My scientific quality controls

- I use the original dataset's `B` (benign) and `M` (malignant) labels, with `M` as the positive class.
- I count a false negative when the model predicts benign for an observed malignant sample.
- I keep `id` in the classroom baseline for fidelity to the worksheet, but exclude it from the research specification.
- I fit preprocessing, feature selection and hyperparameters on training folds, not on their validation folds.
- I disclose weaker results alongside stronger ones and compare only equivalent evaluation protocols.
- I make no medical diagnosis, screening or clinical-safety claim.

## My data provenance

I retain the instructor-provided CSV byte-for-byte in the repository. I record its SHA-256 checksum in `data/SHA256.txt`. Using another version of the dataset may change the cleaning results, splits and reported model scores.

## My proposed deployment boundary

I propose an **educational, access-controlled demonstration**, with validated inputs, the saved preprocessing pipeline, model-version tracking, monitoring for distribution drift and clear limitations. I have not clinically validated or approved this application. Any real medical use would require independent patient-cohort validation, clinical oversight, privacy protection and applicable regulatory review.
