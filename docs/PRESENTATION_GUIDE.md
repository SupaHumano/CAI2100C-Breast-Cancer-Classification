# Oral Presentation and Questions

**Project 1 | Juan Luna Santibanez | CAI2100C**

## 60-second explanation

I used a dataset containing breast mass measurements and a known diagnosis label. I first checked the data for missing values and applied the cleaning approach from our course notebook. Then I converted the labels to a numeric target and compared three supervised algorithms: KNN, SVM and Decision Tree. I measured each model with a held-out test set, a confusion matrix and a classification report. In this classroom split, SVM had the highest accuracy, but I also checked its ability to identify malignant samples correctly and studied how performance changes across validation folds.

## The professor may ask

**Why is this supervised learning?** The dataset includes known class labels. A supervised classifier learns relationships between the measurements and those labels.

**Which column are you predicting?** I predict `diagnosis`, mapped as `B = 0` and `M = 1`.

**What does the dataset actually classify?** Benign versus malignant in this diagnostic dataset. It does not directly separate invasive cancer from non-invasive cancer stages.

**How many samples are included?** 569 originally; 543 remain after removing 26 incomplete rows. The classroom split uses 434 development records and 109 held-out cases.

**Why use StandardScaler?** Different numeric features have different scales. Distance-based KNN and margin-based SVM can be sensitive to scale. I learned the scaler on the training partition only.

**What is a confusion matrix?** A table of correct and incorrect predictions for each actual class. With rows as true diagnosis and columns as predicted diagnosis, the lower-left cell counts missed malignant samples.

**Which model was strongest?** SVM achieved 108 correct predictions out of 109 cases in the classroom holdout, or 99.08% accuracy. That is a result for that fixed split only.

**Why did your research show approximately 98% instead of 99%?** Nested cross-validation repeats training and selection over different development folds. It more fairly estimates how performance varies when the training data change.

**Which errors matter?** The cost of false negatives is particularly serious because a malignant case could be predicted benign. There were one such error for classroom SVM, five for KNN and four for Decision Tree.

**Why did you examine `id`?** It is an administrative record identifier, not a meaningful clinical feature. The course baseline mirrors the template, and the more rigorous research pipeline excludes that column.

**Does this system diagnose cancer?** No. This experiment is educational; medical diagnosis requires clinical validation, oversight and regulatory safeguards.

**How would you deploy a future system?** I would start with a secured teaching demonstration and preserve preprocessing consistency and model versions. I would not deploy a patient-facing clinical application from this classroom dataset.

**How did you complete the project?** I completed the project individually with Professor Beth Muturi's approval.

## Short conclusion

The main lesson is not a particular accuracy percentage. It is how to construct and compare classifiers, inspect their errors, and explain the limits of what the data can support.
