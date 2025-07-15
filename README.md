# 🧠 Computational Physics & Machine Learning Projects

This repository contains two independent but methodologically rigorous projects, developed as part of graduate-level coursework in **Computational Quantum Physics and Applications**, at the **Aristotle University of Thessaloniki**.

Each project combines theory, numerical methods, and data analysis in Python—using real-world datasets or analytical models—to extract meaningful insights and validate physical or statistical hypotheses.

---

## 📌 Projects Overview

### 1️⃣ Information Entropy Analysis of Atomic Systems

- **Objective**: Calculate and analyze information-theoretic measures such as **Shannon entropy**, **Onicescu energy**, **order parameter**, and **complexity** for atoms from **He (Z = 2)** to **Ne (Z = 10)**.
- **Approach**:
  - Utilizes analytical **Roothaan-Hartree-Fock (RHF)** wavefunctions.
  - Extracts RHF coefficients via **OCR** from scientific literature.
  - Computes wavefunctions and electron densities in **position and momentum space**.
  - Analyzes how entropy and complexity scale with atomic number \( Z \).
- **Includes**:
  - Jupyter notebooks and Python scripts for numerical integration and plotting.
  - Automated regression analysis and interpretative plots.
  - Full LaTeX report with equations and results.


---

### 2️⃣ Higgs Boson Signal Classification Using Machine Learning

- **Objective**: Apply classical machine learning and deep learning methods to distinguish between **Higgs boson signals** and **background noise** using tabular high-energy physics data.
- **Dataset**: A reduced and cleaned version of the **HIGGS UCI Dataset** with 8,000 events.
- **Algorithms Implemented**:
  - **Random Forest** classifier with scikit-learn.
  - **K-Nearest Neighbors (KNN)** classification with parameter tuning.
  - **Artificial Neural Network (ANN)** using TensorFlow and Keras.
- **Evaluation Metrics**:
  - Accuracy, Confusion Matrix, ROC Curve, AUC Score.
  - Feature separation into **low-level** and **high-level** physics features for comparative analysis.
- **Includes**:
  - Modular, well-commented `.ipynb` notebooks.
  - LaTeX-ready plots and performance analysis.


---
