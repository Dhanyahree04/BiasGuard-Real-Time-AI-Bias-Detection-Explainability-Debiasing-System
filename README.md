**#BiasGuard — Real-Time AI Bias Detection, Explainability & Debiasing System**

Real-time AI bias detection, explainability, and debiasing system using AIF360 and Gemma (Vertex AI) for fair decision-making.

# BiasGuard — Real-Time AI Bias Detection, Explainability & Debiasing System


---

## 📌 Overview
BiasGuard is a real-time AI bias detection and correction platform that identifies, explains, and mitigates bias in decision-making systems such as hiring, lending, and healthcare.

It enables users to upload datasets, detect hidden bias using fairness metrics, generate human-readable explanations, and produce fairer alternative outcomes — all before a biased decision reaches a human.

---

## 🔴 Problem Statement
Artificial Intelligence systems are increasingly deployed to make life-altering decisions in hiring, lending, and healthcare. However, most of these systems operate as opaque black boxes — producing outcomes with no transparency, no explanation, and no recourse for affected individuals.

Bias originates at the data level, where historical discrimination against protected groups such as women, minorities, and older individuals is embedded. When machine learning models are trained on such data, they inherit and amplify this bias while still maintaining high accuracy, making the issue difficult to detect.

Existing bias auditing tools fail because:
- They detect bias only after decisions are made
- They produce complex, unreadable outputs for non-technical users
- They identify problems but do not provide actionable solutions

As a result, bias propagates silently, leading to unfair decisions and reduced trust in AI systems.

---

## 💡 Solution
BiasGuard  is a real-time bias interception system that detects bias, explains it clearly, and generates fairer alternatives before decisions are finalized.

The platform operates across four layers:

---

### ⚙️ Layer 1 — ML Bias Detection Engine
- Built using **AIF360 + scikit-learn**
- Trains a Random Forest model on uploaded datasets
- Computes fairness metrics:
  - Disparate Impact Ratio
  - Statistical Parity Difference
  - Equal Opportunity Difference
  - Average Odds Difference
- Classifies bias severity (LOW / MEDIUM / HIGH)

📊 Example Insight:
> Men are over 3x more likely to be classified as high earners than equally qualified women.

---

### 🤖 Layer 2 — Explainability & Fix Suggestions
- Powered by **Gemma 2B (Google)**
- Converts bias metrics into plain-English explanations

Example:
> "This system is significantly less likely to select female candidates due to bias in training data."

- Generates 3 actionable fixes for decision-makers

---

### 🔁 Layer 3 — Debiasing Engine
- Uses **AIF360 Reweighing**
- Retrains model with adjusted weights
- Provides before vs after comparison

| Metric | Before | After |
|------|--------|--------|
| Disparate Impact | 0.36 ❌ | 0.91 ✅ |
| Equal Opportunity Diff | -0.12 ❌ | -0.02 ✅ |
| Accuracy | 84.2% | 83.1% |
| Severity | 🔴 HIGH | 🟢 LOW |

---

### 🌐 Layer 4 — API + Frontend
- **FastAPI backend**
  - `POST /audit` → full bias pipeline
  - `GET /` → UI
- **HTML + JavaScript frontend**
  - Upload CSV
  - View results instantly
- **Google Cloud Run deployment**
  - Scalable and zero-cost (free tier)

---

## ⚙️ Features
- CSV dataset upload via browser
- Real-time bias detection
- Fairness metrics computation
- Plain-English explanation using AI
- Automated bias correction
- Before vs After comparison
- REST API integration

---

## 🏗️ System Architecture

Frontend (HTML / React)
        ↓
FastAPI Backend
        ↓
ML Bias Detection (AIF360)
        ↓
Explainability Layer (Gemma 2B)
        ↓
Debiasing Engine
        ↓
Output (UI + JSON)

---

## 🛠️ Tech Stack

### Machine Learning
- AIF360
- Fairlearn
- scikit-learn
- pandas, numpy

### Backend
- FastAPI
- Uvicorn

### Frontend
- HTML5
- JavaScript

### AI / LLM
- Gemma 2B (Google)
- HuggingFace / Vertex AI

### Cloud
- Google Cloud Run
- Firebase Hosting
- Google Colab

### Data Tools
- BigQuery
- Looker Studio

---

## 📊 Dataset
- Adult Income Dataset (UCI)
- Used to analyze bias in income prediction (proxy for hiring decisions)

---

## 🚀 How to Run

### Clone the repository
```bash
git clone https://github.com/your-username/fairlens.git
cd fairlens

#install dependencies
pip install -r requirements.txt

Install dependencies
pip install -r requirements.txt
Run backend
uvicorn main:app --host 0.0.0.0 --port 8000
Run frontend
Open index.html in browser
Upload CSV file
View results
🌐 API Endpoints
GET /
Launch frontend UI
POST /audit
Upload dataset
Returns bias analysis + explanation + fix
GET /health
API health check
📈 Results
Detects hidden bias in datasets
Provides explainable AI insights
Generates actionable fixes
Reduces bias while maintaining accuracy
🎯 Impact

Bias Guard shifts AI accountability from post-hoc auditing to real-time intervention.

It ensures:

Fair decision-making
Transparency in AI systems
Ethical and responsible AI deployment

🌍 SDG Alignment:

SDG 10 — Reduced Inequalities
SDG 16 — Peace, Justice & Strong Institutions
