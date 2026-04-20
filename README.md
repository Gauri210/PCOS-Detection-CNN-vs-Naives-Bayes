# 🩺 PCOS Detection using CNN vs Naive Bayes

A comparative machine learning project for automated detection of **Polycystic Ovary Syndrome (PCOS)** from ultrasound images using both **traditional** and **deep learning** approaches.

---

## 📌 Overview

Polycystic Ovary Syndrome (PCOS) is a common endocrine disorder that can lead to serious health complications if not detected early. This project aims to build an **automated diagnostic system** that classifies ovarian ultrasound images as:

* ✅ Normal
* ⚠️ PCOS (Abnormal)

We compare two fundamentally different approaches:

* **Gaussian Naive Bayes (Baseline Model)**
* **Convolutional Neural Network (CNN)**

---

## 🚀 Features

* 📊 End-to-end ML pipeline (data → preprocessing → training → evaluation)
* 🧠 Deep learning model for image-based classification
* ⚖️ Comparative analysis between ML and DL models
* 📈 Performance metrics: Accuracy, Precision, Recall, F1-score
* 📁 Exported predictions for test dataset

---

## 🗂️ Project Structure

```
pcos-detection-cnn-vs-naive-bayes/
│
├── dataset/
│   ├── train/
│   └── test/
│
├── models/
│   ├── naive_bayes_model.pkl
│   └── cnn_model.h5
│
├── notebooks/
│   └── training.ipynb
│
├── outputs/
│   └── pcod_predictions.csv
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Methodology

### 🧹 Preprocessing

* Grayscale conversion
* Image resizing (128 × 128)
* Normalization (0–1 scaling)

### 📉 Naive Bayes

* Flattened images (16,384 features)
* Standard scaling
* Gaussian Naive Bayes classifier

### 🧠 CNN Architecture

* 4 Convolutional blocks (32 → 256 filters)
* MaxPooling + Batch Normalization
* Fully connected layers (256 → 128)
* Dropout (0.5)
* Softmax output layer

---

## 📊 Results

| Metric    | Naive Bayes | CNN    |
| --------- | ----------- | ------ |
| Accuracy  | 61.19%      | 78.78% |
| Precision | 86.20%      | 77.59% |
| Recall    | 54.68%      | 99.04% |
| F1-Score  | 66.92%      | 87.01% |

### 🔍 Key Insight

CNN significantly outperforms Naive Bayes, especially in **recall**, making it more reliable for medical diagnosis (fewer false negatives).

---

## 📁 Output

Final predictions are saved in:

```
outputs/pcod_predictions.csv
```

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* Scikit-learn
* NumPy, Pandas
* OpenCV / PIL

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/pcos-detection-cnn-vs-naive-bayes.git
cd pcos-detection-cnn-vs-naive-bayes
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the notebook or app:

```bash
python app.py
```

---

## 📌 Future Improvements

* 🔄 Transfer learning (ResNet, VGG)
* 🎯 Attention mechanisms for region focus
* 🌐 Deploy as web app (Flask/Render)
* 📱 Mobile integration (Android app)

---

## 👩‍💻 Author

**Gauri Deshmukh**
B.Tech Data Science
MPSTME, NMIMS

---

## 📚 References

* Faust et al., *Deep learning for healthcare applications*, 2018
* Esteva et al., *Deep learning in healthcare*, 2019
* Scikit-learn Documentation
* TensorFlow Documentation

---
