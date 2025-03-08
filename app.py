

import os, json, time
from dotenv import load_dotenv
from flask import Flask, jsonify
from database import list_all_tables, get_table_schema
from groq import Groq

load_dotenv()

app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Load training datasets at startup
with open('train_generate_task.json', 'r') as f:
    nl_to_sql_examples = json.load(f)

with open('train_query_correction_task.json', 'r') as f:
    query_correction_examples = json.load(f)

def get_db_schema_context():
    tables = list_all_tables(os.getenv("DB_NAME"), os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_HOST"), os.getenv("DB_PORT"))
    schema_context = ""
    for table in tables:
        columns = get_table_schema(os.getenv("DB_NAME"), os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_HOST"), os.getenv("DB_PORT"), table)
        schema_context += f"Table {table} columns: {', '.join(columns.keys())}\n"
    return schema_context

def call_groq_api(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="mixtral-8x7b-32768",
            temperature=0,
            max_tokens=500,
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Groq API Error: {e}")
        return None

# Function to correct erroneous SQL queries
def correct_sql_query(incorrect_query):
    schema_context = get_db_schema_context()

    few_shot_examples = "\n\n".join(
        [f"Incorrect SQL: {ex['IncorrectQuery']}\nCorrected SQL: {ex['CorrectQuery']}" for ex in query_correction_examples[:3]]
    )

    prompt = f"""
You are an expert SQL assistant. Given the database schema below:

{schema_context}

Here are examples of correcting erroneous SQL queries:

{few_shot_examples}

Now correct this erroneous SQL query:

Incorrect SQL: {incorrect_query}
Corrected SQL:
"""
    return call_groq_api(prompt)

# Endpoint to generate final submission file for Query Correction Task
@app.route('/generate_query_correction_submission', methods=['GET'])
def generate_query_correction_submission():
    with open('sample_submission_query_correction_task.json', 'r') as f:
        correction_tasks = json.load(f)

    final_correction_submission = []

    for task in correction_tasks:
        incorrect_query = task["IncorrectQuery"]
        print(f"Correcting SQL: {incorrect_query}")

        corrected_sql = correct_sql_query(incorrect_query)

        retries = 0
        while corrected_sql is None and retries < 3:
            print(f"Retrying ({retries+1})...")
            time.sleep(2)
            corrected_sql = correct_sql_query(incorrect_query)
            retries += 1

        if corrected_sql:
            clean_corrected_sql = corrected_sql.replace("\\", "")
            final_correction_submission.append({
                "IncorrectQuery": incorrect_query,
                "CorrectQuery": clean_corrected_sql
            })
            print(f"✅ Corrected (cleaned): {clean_corrected_sql}")
        else:
            final_correction_submission.append({
                "IncorrectQuery": incorrect_query,
                "CorrectQuery": "Correction Failed"
            })
            print("❌ Correction Failed after retries")

    with open('final_submission_query_correction_task.json', 'w') as outfile:
        json.dump(final_correction_submission, outfile, indent=2)

    return jsonify({
      "message": "Query Correction submission file generated successfully!",
      "submission_file": "final_submission_query_correction_task.json",
      "results": final_correction_submission
    })

if __name__ == "__main__":
    app.run(debug=True)