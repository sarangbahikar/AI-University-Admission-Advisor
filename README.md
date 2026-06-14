# 🎓 AI University Admission Advisor

An end-to-end Generative AI platform that helps students evaluate their university admission prospects, analyze application documents, discover scholarships, and interact with university information through Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

### 👤 Student Profile Management

* Academic profile creation
* IELTS / TOEFL support
* Experience tracking
* Projects, certifications, and research profile

### 📄 Resume Analyzer

* AI-powered resume analysis using Groq
* Strengths and weaknesses identification
* Improvement suggestions

### 📝 SOP Analyzer

* Statement of Purpose evaluation
* Writing quality assessment
* Personalized improvement recommendations

### 🏛️ University Recommendation Engine

* Dynamic CSV dataset upload
* AI-based schema detection
* University eligibility matching
* Scholarship-aware recommendations
* Ranking-aware recommendations

### 📊 Admission Predictor

* Trained using a real Graduate Admissions dataset
* Random Forest Regressor
* Real-world admission probability prediction
* Model Performance (R² Score ≈ 0.79)

### 💰 Scholarship Advisor

* Personalized UK scholarship recommendations
* Eligibility analysis
* Application guidance

### 🤖 University RAG Assistant

* PDF upload support
* ChromaDB vector database
* Sentence Transformer embeddings
* Document chunking
* Semantic retrieval
* Groq-powered answer generation

---

## 🏗️ Architecture

Student Profile
↓
University Recommendation Engine

Resume / SOP
↓
Groq Analysis

Graduate Admissions Dataset
↓
Random Forest Model
↓
Admission Prediction

PDF Upload
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
ChromaDB
↓
Semantic Retrieval
↓
Groq
↓
Answer Generation

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Generative AI

* Groq API
* Llama 3.3 70B Versatile

### Machine Learning

* Scikit-Learn
* Random Forest Regressor
* Pandas
* NumPy

### RAG

* ChromaDB
* Sentence Transformers
* all-MiniLM-L6-v2

### Data Processing

* PDFPlumber
* Python

---

## 📈 Model Performance

Admission Prediction Model:

* Algorithm: Random Forest Regressor
* Dataset: Graduate Admissions Dataset
* R² Score: 0.7901

---

## 📂 Project Structure

AI_University_Admission_Advisor/

├── app.py

├── pages/

├── utils/

├── models/

├── datasets/

├── chroma_db/

├── requirements.txt

└── README.md

---

## ⚙️ Installation

```bash
git clone <repository-url>

cd AI_University_Admission_Advisor

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

---

## 🎯 Future Improvements

* Multi-country university support
* Advanced recommendation engine using ML
* Scholarship database integration
* University ranking API integration
* Multi-document RAG
* Cloud deployment

---

## 👨‍💻 Author

Sarang Bahikar

AI | Data Science | Generative AI | Study Abroad Technology
