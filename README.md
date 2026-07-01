# 🚀 CareerFit AI - AI Powered Career Intelligence Platform #

> **Your Personal AI Career Coach for Resume Analysis, ATS Optimization, Career Guidance, Interview Preparation, and Real-Time Job Recommendations**

---

## 📌 Overview

CareerFit AI is a comprehensive AI-powered Career Intelligence Platform designed to help students and job seekers improve their employability. The platform combines **Natural Language Processing (NLP)**, **Machine Learning**, **Generative AI**, and **Modern Web Technologies** to automate resume analysis, ATS evaluation, career recommendations, interview preparation, and job discovery.

Unlike traditional ATS checkers that only provide a resume score, CareerFit AI offers an end-to-end career guidance experience by analyzing resumes, identifying skill gaps, recommending career paths, generating AI-powered resume summaries and interview questions, fetching live job opportunities, generating cover letters, and tracking job applications through an interactive SaaS dashboard.

---

# ✨ Key Features

## 📄 Resume Analysis

* Upload PDF and DOCX resumes
* Extract resume text automatically
* Clean and preprocess resume using NLP
* Multiple resume upload support
* Resume version comparison

---

## 🎯 ATS Analysis

* ATS Compatibility Score
* Resume Match Percentage
* Resume Strength Analysis
* Resume Ranking
* Resume Quality Insights

---

## 🧠 Skill Intelligence

* Skill Extraction
* Matched Skills Detection
* Missing Skills Identification
* Recommended Skills
* Skill Gap Analysis

---

## 📑 Resume Section Analyzer

Analyze each section individually:

* Skills
* Projects
* Experience
* Education
* Certifications

Receive section-wise scores and personalized improvement suggestions.

---

## 📊 Resume Comparison

* Resume Version Manager
* Compare multiple resume versions
* Resume Ranking
* ATS Score Comparison
* Select Best Resume

---

## 🏆 Top Candidate Comparison

Compare your resume with an ideal candidate profile.

Visual comparison includes:

* ATS Score
* Skills
* Projects
* Experience
* Certifications

Identify missing qualifications and improvement areas.

---

## 🤖 AI Features

Powered by **OpenRouter** and the **DeepSeek Large Language Model**.

Generate:

* AI Resume Summary
* Personalized Interview Questions
* Career Insights
* Resume Recommendations

---

## 🎓 Career Recommendation

Recommend the most suitable career based on candidate skills.

Supported roles include:

* Data Scientist
* Data Analyst
* Machine Learning Engineer
* AI Engineer
* Business Analyst

---

## 🛣 Learning Roadmap

Personalized learning roadmap based on missing skills.

Example:

SQL

↓

Python

↓

Machine Learning

↓

Deep Learning

↓

Generative AI

---

## 💼 Job Recommendation

Recommend relevant jobs based on skills and career path.

Examples:

* Data Scientist Intern
* ML Engineer
* Junior Data Analyst
* AI Engineer

---

## 🌐 Live Job Search

Integrated with **RapidAPI JSearch API**

Displays:

* Live Jobs
* Company Name
* Location
* Salary
* Apply Link

---

## 📝 AI Cover Letter Generator

Automatically generate professional cover letters customized for each job application.

Features:

* Edit
* Copy
* Download

---

## 🎤 Interview Preparation

Generate AI-powered interview questions based on:

* Resume
* Job Description
* Missing Skills

Includes:

* Technical Questions
* HR Questions
* Behavioral Questions

---

## 📋 Application Tracker

Professional Kanban Board

Track every application through:

* Saved
* Applied
* Assessment
* Interview Scheduled
* HR Round
* Offer
* Rejected

---

## 📈 Analytics Dashboard

Interactive dashboards displaying:

* ATS Trends
* Resume Comparison
* Skill Distribution
* Career Growth
* Application Statistics

---

# 🏗 System Architecture

```text
User
   │
   ▼
React Frontend
   │
   ▼
FastAPI Backend
   │
   ├── parser.py
   ├── preprocess.py
   ├── skills.py
   ├── matcher.py
   ├── career_recommender.py
   ├── job_recommender.py
   ├── job_api.py
   └── llm_utils.py
   │
   ▼
JSON Response
   │
   ▼
React Dashboard
```

---

# ⚙️ Project Workflow

```text
Resume Upload
      │
      ▼
Resume Parsing
      │
      ▼
Text Preprocessing
      │
      ▼
Skill Extraction
      │
      ▼
ATS Score Calculation
      │
      ▼
Matched Skills
      │
      ▼
Missing Skills
      │
      ▼
Resume Section Analysis
      │
      ▼
Career Recommendation
      │
      ▼
Learning Roadmap
      │
      ▼
AI Resume Summary
      │
      ▼
Interview Questions
      │
      ▼
Job Recommendation
      │
      ▼
Live Job Search
      │
      ▼
Application Tracker
```

---

# 🧠 Machine Learning & AI Techniques

### Natural Language Processing (NLP)

* Tokenization
* Stopword Removal
* Lemmatization
* Text Cleaning

### Machine Learning

* TF-IDF Vectorization
* Cosine Similarity

### Skill Analysis

* Set Intersection
* Set Difference

### Career Recommendation

* Rule-Based Recommendation Engine

### Artificial Intelligence

* OpenRouter API
* DeepSeek Large Language Model (LLM)
* Prompt Engineering
* AI Resume Summary Generation
* AI Interview Question Generation

---

# 🛠 Technology Stack

## Frontend

* React
* TypeScript
* Tailwind CSS
* ShadCN UI
* Framer Motion
* Recharts
* Lucide React

## Backend

* FastAPI
* Python
* Scikit-learn
* NLTK
* pdfplumber
* docx2txt
* Requests

## APIs

* OpenRouter API
* DeepSeek LLM
* RapidAPI JSearch API

---

# 📂 Project Structure

```text
CareerFit-AI/
│
├── frontend/
│
├── backend/
│
├── utils/
│   ├── parser.py
│   ├── preprocess.py
│   ├── skills.py
│   ├── matcher.py
│   ├── career_recommender.py
│   ├── job_recommender.py
│   ├── job_api.py
│   └── llm_utils.py
│
├── resumes/
│
├── requirements.txt
│
├── README.md
│
└── .env
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/CareerFit-AI.git
```

Navigate to the project folder:

```bash
cd CareerFit-AI
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Install frontend dependencies:

```bash
npm install
```

Run the FastAPI backend:

```bash
uvicorn main:app --reload
```

Run the React frontend:

```bash
npm run dev
```

---

# 📸 Screenshots

Add screenshots of:

* Landing Page
* Dashboard
* Resume Upload
* ATS Analysis
* Skill Insights
* Resume Comparison
* Career Recommendation
* AI Summary
* Interview Preparation
* Job Recommendations
* Application Tracker

---

# 🔮 Future Enhancements

* AI Resume Builder
* AI Mock Interview with Voice
* Resume Keyword Optimizer
* LinkedIn Profile Analyzer
* AI Salary Prediction
* Company Interview Experiences
* Recruiter Dashboard
* Email Notifications
* Multi-language Resume Analysis

---

# 👨‍💻 Author

**Preethi K**

Aspiring Data Scientist | Machine Learning Enthusiast | AI Developer

GitHub: https://github.com/preethikris

---

# ⭐ If you found this project useful, please consider giving it a Star!
