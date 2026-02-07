# 🧠 AI Recruitment & ATS Resume Screening Platform

An end-to-end AI hiring assistant that automates resume screening, ATS evaluation, candidate ranking, skill gap detection, recruiter Q&A, and interview preparation using LLMs.

This system simulates a real **Applicant Tracking System (ATS)** used by companies to filter and shortlist candidates efficiently.

---

## 🚀 Live Features

* ATS Resume Screening with **SHORTLIST / REJECT**
* Resume Format Scanner (ATS Compatibility)
* Skill Gap Analysis with Learning Recommendations
* Candidate Summary Dashboard
* Recruiter Q&A Assistant
* Interview Question Generator
* Candidate Ranking & Bulk Resume Processing
* CSV Export of Results
* Animated Modern UI

---

## 📸 Screenshots

> Add screenshots here after deployment

```
/screenshots/dashboard.png
/screenshots/analysis.png
/screenshots/ranking.png
```

---

## 🎯 Problem Statement

Recruiters spend hours manually screening resumes.
This process is slow, repetitive, and prone to human bias.

Our goal is to automate the early recruitment pipeline using AI and NLP to improve hiring efficiency and reduce recruiter workload.

---

## 💡 Solution

We built an AI-powered recruitment platform that:

1. Extracts text from resumes
2. Evaluates ATS compatibility
3. Matches resumes with job descriptions using LLMs
4. Identifies missing skills and learning paths
5. Ranks candidates based on job fit
6. Generates interview questions automatically

---

## ⭐ Features Explained

### 🤖 ATS Screening Engine

* Overall Match Score (0–100)
* Technical Skill Score
* Project Relevance Score
* Experience Score
* Recruiter-style reasoning
* Final decision → **SHORTLIST / REJECT**

---

### 📄 Resume Format Scanner

Checks ATS friendliness:

* Contact information check
* Resume structure analysis
* Formatting risk detection
* ATS Score with suggestions
* ATS PASS / FAIL badge

---

### 🎯 Skill Gap Analysis

* Must-have missing skills
* Good-to-have missing skills
* Personalized learning recommendations

---

### 💬 Recruiter Q&A Assistant

Ask natural questions:

* “How much Python experience?”
* “Why was candidate shortlisted?”
* “What is the biggest achievement?”

---

### 🎤 Interview Question Generator

Creates:

* Technical questions
* Project-based questions
* HR questions

---

### 🏆 Candidate Ranking System

* Compare multiple resumes
* Rank candidates by job fit
* Bulk processing (up to 50 resumes)

---

## ⚙️ Tech Stack

| Category    | Tools              |
| ----------- | ------------------ |
| Language    | Python             |
| LLM         | Groq API           |
| Backend     | FastAPI            |
| Frontend    | Streamlit          |
| NLP         | Prompt Engineering |
| Data        | Pandas, NumPy      |
| PDF Parsing | PyPDF2             |

---

## 🔄 System Workflow

```
Resume Upload → ATS Scan → AI Screening → Skill Gap Analysis → 
Candidate Summary → Recruiter Q&A → Interview Questions → Ranking
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Rudra-005/AI_ATS_Recruiment.git
cd AI_ATS_Recruiment
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

### 5️⃣ Run Application

```bash
streamlit run app.py
```

---

## 🎯 Use Cases

* HR Resume Screening
* Campus Placements
* Hiring Automation Tools
* Career Guidance Platforms

---

## 🔮 Future Improvements

* Cloud deployment
* Integration with job portals
* Multilingual resume support
* Bias & fairness detection

---

## 👨‍💻 Author

**Rudra Pratap Singh**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

After creating README.md, push it:

```bash
git add README.md
git commit -m "Added README"
git push
```

Your repo will look professional 🔥
