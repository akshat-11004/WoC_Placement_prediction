# 🎓 Placement Prediction System (Checkpoint 2)

This project builds a **machine learning–based placement prediction system** using engineered academic, skill, and engagement features.  
The objective is to accurately predict whether a student will be **Placed** or **Not Placed**, while following **proper ML practices** such as feature selection, model comparison, and metric-driven evaluation.

---

## 📊 Dataset Overview

The dataset consists of **17 numeric features**, including engineered composite scores, and a binary target variable:

- **Target**: `PlacementStatus` (Placed / Not Placed)

### Examples of Feature Groups:
- Academic performance (CGPA, SSC, HSC, composites)
- Skills & training (projects, certifications, aptitude)
- Engagement & experience (internships, extracurriculars)
- Engineered indices (competitiveness, skill development, engagement)

---

## 🛠️ Feature Engineering

To capture real-world placement decision factors, several **composite and normalized features** were engineered:

- **Academic_Composite**
- **Competitiveness_Score**
- **Skill_Development_Index**
- **Practical_Experience_Score**
- **Engagement_Score**

These reduce noise and better represent latent student capability.

---

## 🔍 Feature Selection Strategy

Multiple **filter-based feature selection methods** were applied:

### 1️⃣ Correlation with Target  
### 2️⃣ ANOVA F-Score (SelectKBest)

Top features were selected based on **consistent ranking across methods**.

### 🔝 Top Features (Both Methods)

| Feature | Correlation | ANOVA F-Score |
|------|------------|---------------|
Competitiveness_Score | 0.57 | 4870 |
Academic_Composite | 0.56 | 4782 |
Academic_Normalized | 0.56 | 4782 |
Skill_Development_Index | 0.52 | 3840 |
AptitudeTestScore | 0.52 | 3739 |
Engagement_Score | 0.51 | 3652 |
HSC_Marks | 0.50 | 3436 |
ExtracurricularActivities | 0.48 | 3033 |
Practical_Experience_Score | 0.47 | 2954 |
Projects | 0.47 | 2916 |

---

## 🤖 Models Trained

Three **tree-based ensemble models** were trained using the selected features:

- **XGBoost**
- **LightGBM**
- **Random Forest**

Hyperparameters were tuned beforehand using **RandomizedSearchCV** with **ROC-AUC** as the optimization metric.

---

## 📈 Evaluation Metrics

Models were evaluated on a **held-out test set** using:

- Accuracy
- ROC-AUC (primary metric)
- F1-Score
- Precision & Recall (via classification report)

> **Why ROC-AUC?**  
> The dataset is moderately imbalanced. ROC-AUC provides a **threshold-independent** measure of how well the model separates placed vs non-placed students.

---

## 🧪 Model Performance Comparison

| Model | Accuracy | ROC-AUC | F1-Score |
|----|--------|--------|---------|
XGBoost | 0.794 | 0.875 | 0.747 |
LightGBM | **0.794** | **0.875** | **0.748** |
Random Forest | 0.792 | 0.872 | 0.762 |

### 🏆 Best Model: **LightGBM**
- Achieved the **highest ROC-AUC**
- Better ranking and class separation
- Efficient handling of tabular, engineered features

---

## 💾 Model Saving

All trained models were saved using `joblib` for reproducibility and deployment.
