# AI-Powered SQL Query Generation and Correction Agent

## 🚀 Overview
This project provides an AI-driven backend service capable of:
- Generating accurate SQL queries from natural language inputs.
- Automatically correcting erroneous SQL queries (syntax errors, incorrect attributes, or tables).

The solution leverages advanced NLP techniques, schema-aware query generation, and query correction methods to simplify database interactions for technical and non-technical users.

---

## 🛠 Tech Stack Used

| Technology / Tool                | Purpose / Role                                      |
|----------------------------------|-----------------------------------------------------|
| *Python (3.7+)*                | Core programming language                           |
| *PostgreSQL*                   | Database management                                 |
| *Groq API (mixtral-8x7b-32768)*         | Large Language Model (LLM) for NLP tasks            |
| *Flask*                        | Backend API framework                               |
| *psycopg2-binary*              | PostgreSQL database connection                      |
| *python-dotenv*                | Secure environment variable management              |
| *Groq Python SDK*              | Official SDK for Groq API integration               |

---

## 🎯 Approach Used

### 1. Natural Language to SQL Query Generation
- Leveraged Groq's mixtral-8x7b-32768 model to interpret user intent.
- Integrated dynamic database schema extraction to ensure accuracy.
- Implemented few-shot learning prompts using provided training datasets.

### 2. SQL Query Correction
- Used Groq's mixtral-8x7b-32768 model trained on provided correction examples.
- Dynamically provided schema context to ensure corrected queries align with the database.
- Included robust retry mechanisms and error handling to ensure reliability.

---

## 📂 Project Structure
project/
├── .env
├── app.py
├── database.py
├── requirements.txt
├── train_generate_task.json
├── train_query_correction_task.json
├── sample_submission_generate_task.json
└── sample_submission_query_correction_task.json

---

## ⚙ Low-Level Design (LLD)

User/Client
│
├─── HTTP Request (NL Query or Incorrect SQL)
│ │
│ ▼
│ Flask Backend (app.py)
│ │
│ ├─── Load Schema Context from PostgreSQL via database.py
│ │
│ ├─── Load Few-Shot Examples from Training JSON files
│ │
│ └─── Call Groq API via Groq Python SDK ──► mixtral-8x7b-32768 Model
│ ▲ (Hosted by Groq)
│ │ │
│ ◄──────────── Return Generated/Corrected SQL
│
└─── HTTP Response (Accurate or Corrected SQL Query)

---

## 🚩 How to Run the Project Locally

### 1. Clone the Repository & Navigate to Project Folder:

git clone <your-github-repo-link>
cd <your-project-folder>

### 2. Install Dependencies:

pip install -r requirements.txt

### 3. Setup Environment Variables (.env file):

### 4. Setup your PostgreSQL Database:
Run your provided database.py script:

python database.py 

### 5. Run Flask Backend:

python app.py 

---


## ✅ API Endpoints:

| Endpoint                                   | Method | Description                           |
|--------------------------------------------|--------|---------------------------------------|
| /generate_submission                     | GET    | Generates SQL queries from NL inputs  |
| /generate_query_correction_submission    | GET    | Corrects erroneous SQL queries        |

---

## 🎉 Final Submission Files Generated:

- final_submission_generate_task.json
- final_submission_query_correction_task.json

These files are ready for submission as per Adobe Emerge Hackathon guidelines.

---