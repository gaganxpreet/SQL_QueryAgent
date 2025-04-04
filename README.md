# AI-Powered SQL Query Generation and Correction Agent

## 🚀 Overview
This project provides an AI-driven backend service capable of:
- Generating accurate SQL queries from natural language inputs.
- Automatically correcting erroneous SQL queries (syntax errors, incorrect attributes, or tables).

The solution leverages advanced NLP techniques, schema-aware query generation, and query correction methods to simplify database interactions for technical and non-technical users.

---

## 🛠 Tech Stack Used

| Technology / Tool              | Purpose / Role                                      |
|--------------------------------|-----------------------------------------------------|
| *Python (3.7+)*                | Core programming language                           |
| *PostgreSQL*                   | Database management                                 |
| *Groq API (mixtral-8x7b-32768)* | Large Language Model (LLM) for NLP tasks            |
| *Flask*                        | Backend API framework                               |
| *psycopg2-binary*              | PostgreSQL database connection                      |
| *python-dotenv*                | Secure environment variable management              |
| *Groq Python SDK*              | Official SDK for Groq API integration               |
| *Sentence Transformers*        | Semantic similarity for example retrieval          |
| *RAKE-NLTK*                    | Keyword extraction for schema filtering             |
| *sqlparse*                     | SQL validation                                     |

---

## 🎯 Approach Used

### 1. Natural Language to SQL Query Generation
- Leveraged **Groq's mixtral-8x7b-32768 model** to interpret user intent.
- Integrated **dynamic database schema extraction** to ensure accuracy.
- Implemented **semantic similarity-based few-shot learning** for context-aware query generation.
- Optimized schema selection by **extracting relevant table information** based on query keywords.

### 2. SQL Query Correction
- Used **Groq's mixtral-8x7b-32768 model** trained on query correction examples.
- Dynamically provided **schema context** to ensure corrected queries align with the database.
- Implemented **robust retry mechanisms and error handling** to improve reliability.

---

## 📂 Project Structure
```
project/
├── .env
├── app.py
├── database.py
├── requirements.txt
├── train_generate_task.json
├── train_query_correction_task.json
├── sample_submission_generate_task.json
├── sample_submission_query_correction_task.json
└── final_submission_generate_task.json
└── final_submission_query_correction_task.json
```

---

## ⚙ Low-Level Design (LLD)

### 🏛️ System Flow

1. **User/Client**  
   - Sends an **HTTP request** containing either:  
     - A **Natural Language (NL) Query**  
     - An **Incorrect SQL Query**  

2. **Flask Backend (`app.py`)**  
   - **Loads Schema Context** dynamically from PostgreSQL via `database.py`  
   - **Extracts Relevant Schema** using RAKE-based keyword extraction  
   - **Fetches Few-Shot Examples** using semantic similarity (Sentence Transformers)  
   - **Calls Groq API** using **Groq Python SDK**, leveraging:  
     - `mixtral-8x7b-32768` Model (Hosted on **Groq**)  

3. **Response Handling**  
   - Receives **Generated/Corrected SQL Query** from the model  
   - Returns an **HTTP Response** with the final **accurate SQL query**  

### 🛠️ Component Breakdown

| Component            | Description |
|----------------------|-------------|
| **User/Client**     | Sends a request with a natural language query or incorrect SQL |
| **Flask Backend**   | Processes the request, extracts schema, and fetches few-shot examples |
| **RAKE (Keyword Extraction)** | Filters relevant schema context for better query accuracy |
| **Sentence Transformers** | Finds the most relevant few-shot examples for better query formulation |
| **Groq API Call**   | Calls the `mixtral-8x7b-32768` model to generate or correct SQL |
| **Response Handling** | Returns the generated/corrected SQL back to the client |

---

## 🚩 How to Run the Project Locally

### 1. Clone the Repository & Navigate to Project Folder:
```bash
git clone <your-github-repo-link>
cd <your-project-folder>
```

### 2. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables (.env file):
Ensure you have a `.env` file with the following variables:
```plaintext
GROQ_API_KEY=<your_groq_api_key>
DB_NAME=<your_db_name>
DB_USER=<your_db_user>
DB_PASSWORD=<your_db_password>
DB_HOST=<your_db_host>
DB_PORT=<your_db_port>
```

### 4. Setup your PostgreSQL Database:
Run your database schema extraction script:
```bash
python database.py
```

### 5. Run Flask Backend:
```bash
python app.py
```

---

## ✅ API Endpoints:

| Endpoint                                    | Method | Description                           |
|---------------------------------------------|--------|---------------------------------------|
| `/generate_submission`                      | GET    | Generates SQL queries from NL inputs  |
| `/generate_query_correction_submission`    | GET    | Corrects erroneous SQL queries        |

---

## 🎉 Final Submission Files Generated:

- `final_submission_generate_task.json`
- `final_submission_query_correction_task.json`

These files are ready for submission as per **Adobe Emerge Hackathon** guidelines.

---

## 📌 Improvements Over Previous Version

- **Added schema filtering using RAKE** to dynamically include only relevant tables and columns.
- **Used Sentence Transformers for Few-Shot Learning**, making SQL generation more context-aware.
- **Implemented Asynchronous Processing** for concurrent SQL generation tasks.
- **Improved Error Handling & Retries**, ensuring more reliable SQL correction.
- **Optimized Schema Loading with Caching**, reducing redundant database calls.

---

## 🎯 Future Enhancements

- **Support for multiple SQL dialects** beyond PostgreSQL.
- **Integration with vector databases** for improved semantic search.
- **Fine-tuning LLM models** for domain-specific query optimization.
- **Interactive UI** for real-time query generation and correction.

---


