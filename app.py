# import os
# from dotenv import load_dotenv
# from flask import Flask, request, jsonify
# import requests
# from database import list_all_tables, get_table_schema

# load_dotenv()

# app = Flask(__name__)

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")

# # Groq API endpoint (replace with actual endpoint provided by Groq)
# GROQ_API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

# # Function to get schema details for prompt context
# def get_db_schema_context():
#     tables = list_all_tables(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
#     schema_context = ""
#     for table in tables:
#         columns = get_table_schema(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, table)
#         schema_context += f"Table {table} has columns: {', '.join(columns.keys())}\n"
#     return schema_context

# # Function to call Groq API for NL to SQL generation or Query Correction tasks
# def call_groq_api(prompt):
#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "mixtral-8x7b-32768",  # Replace with actual Groq model name (up to 7B parameters allowed)
#         "messages": [{"role": "user", "content": prompt}],
#         "temperature": 0,
#         "max_tokens": 500,
#     }
#     response = requests.post(GROQ_API_ENDPOINT, headers=headers, json=data)
#     if response.status_code == 200:
#         return response.json()['choices'][0]['message']['content'].strip()
#     else:
#         print(f"Groq API Error: {response.text}")
#         return None

# # Endpoint for Natural Language to SQL Query Generation
# @app.route('/generate_sql', methods=['POST'])
# def generate_sql():
#     data = request.get_json()
#     nl_query = data.get('nl_query')

#     schema_context = get_db_schema_context()

#     prompt = f"""
#     Given the following database schema information:
#     {schema_context}

#     Generate an accurate SQL query for the following natural language request:
#     "{nl_query}"

#     Provide only the SQL query without explanation.
#     """

#     sql_query = call_groq_api(prompt)
    
#     if sql_query:
#         return jsonify({"sql_query": sql_query})
#     else:
#         return jsonify({"error": "Failed to generate SQL query"}), 500

# # Endpoint for SQL Query Correction Task
# @app.route('/correct_sql', methods=['POST'])
# def correct_sql():
#     data = request.get_json()
#     incorrect_query = data.get('incorrect_query')

#     schema_context = get_db_schema_context()

#     prompt = f"""
#     Given the following database schema information:
#     {schema_context}

#     The following SQL query has errors (syntactical errors or incorrect attributes/tables):
    
#     "{incorrect_query}"

#     Correct the SQL query and provide only the corrected query without explanation.
#     """

#     corrected_query = call_groq_api(prompt)

#     if corrected_query:
#         return jsonify({"corrected_query": corrected_query})
#     else:
#         return jsonify({"error": "Failed to correct SQL query"}), 500

# if __name__ == "_main_":
#     app.run(debug=True)






# import os
# from dotenv import load_dotenv
# from flask import Flask, request, jsonify
# import requests
# from database import list_all_tables, get_table_schema

# load_dotenv()

# app = Flask(__name__)

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")

# # Groq API endpoint
# GROQ_API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

# # Function to get schema details for prompt context
# def get_db_schema_context():
#     tables = list_all_tables(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
#     schema_context = ""
#     for table in tables:
#         columns = get_table_schema(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, table)
#         schema_context += f"Table {table} has columns: {', '.join(columns.keys())}\n"
#     return schema_context

# # Function to call Groq API for NL to SQL generation or Query Correction tasks
# def call_groq_api(prompt):
#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "mixtral-8x7b-32768",  # Using Mixtral model
#         "messages": [{"role": "user", "content": prompt}],
#         "temperature": 0,
#         "max_tokens": 500,
#     }
#     response = requests.post(GROQ_API_ENDPOINT, headers=headers, json=data)
#     if response.status_code == 200:
#         return response.json()['choices'][0]['message']['content'].strip()
#     else:
#         print(f"Groq API Error: {response.text}")
#         return None

# # Endpoint for Natural Language to SQL Query Generation
# @app.route('/generate_sql', methods=['POST'])
# def generate_sql():
#     data = request.get_json()
#     nl_query = data.get('nl_query')

#     schema_context = get_db_schema_context()

#     prompt = f"""
#     Given the following database schema information:
#     {schema_context}

#     Generate an accurate SQL query for the following natural language request:
#     "{nl_query}"

#     Provide only the SQL query without explanation.
#     """

#     sql_query = call_groq_api(prompt)
    
#     if sql_query:
#         return jsonify({"sql_query": sql_query})
#     else:
#         return jsonify({"error": "Failed to generate SQL query"}), 500

# # Endpoint for SQL Query Correction Task
# @app.route('/correct_sql', methods=['POST'])
# def correct_sql():
#     data = request.get_json()
#     incorrect_query = data.get('incorrect_query')

#     schema_context = get_db_schema_context()

#     prompt = f"""
#     Given the following database schema information:
#     {schema_context}

#     The following SQL query has errors (syntactical errors or incorrect attributes/tables):
    
#     "{incorrect_query}"

#     Correct the SQL query and provide only the corrected query without explanation.
#     """

#     corrected_query = call_groq_api(prompt)

#     if corrected_query:
#         return jsonify({"corrected_query": corrected_query})
#     else:
#         return jsonify({"error": "Failed to correct SQL query"}), 500

# if __name__ == "__main__":  # Fixed the "__main__" string
#     app.run(debug=True)


# import os, json
# from dotenv import load_dotenv
# from flask import Flask, request, jsonify
# import requests
# from database import list_all_tables, get_table_schema

# load_dotenv()

# app = Flask(__name__)

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# GROQ_API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

# # Load training datasets at startup
# with open('train_generate_task.json', 'r') as f:
#     nl_to_sql_examples = json.load(f)

# # Get DB schema context for prompts
# def get_db_schema_context():
#     tables = list_all_tables(os.getenv("DB_NAME"), os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_HOST"), os.getenv("DB_PORT"))
#     schema_context = ""
#     for table in tables:
#         columns = get_table_schema(os.getenv("DB_NAME"), os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_HOST"), os.getenv("DB_PORT"), table)
#         schema_context += f"Table {table} columns: {', '.join(columns.keys())}\n"
#     return schema_context

# # Groq API call function
# def call_groq_api(prompt):
#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "mixtral-8x7b-32768",
#         "messages": [{"role": "user", "content": prompt}],
#         "temperature": 0,
#         "max_tokens": 500,
#     }
#     response = requests.post(GROQ_API_ENDPOINT, headers=headers, json=data)
#     if response.status_code == 200:
#         return response.json()['choices'][0]['message']['content'].strip()
#     else:
#         print(f"Groq API Error: {response.text}")
#         return None

# # Function to generate SQL from NL query (for internal use)
# def generate_sql_from_nl(nl_query):
#     schema_context = get_db_schema_context()
    
#     few_shot_examples = "\n\n".join(
#         [f"NL: {ex['NL']}\nSQL: {ex['Query']}" for ex in nl_to_sql_examples[:3]]
#     )

#     prompt = f"""
# You are an expert SQL assistant. Given the database schema below:

# {schema_context}

# Here are examples of translating natural language queries into SQL:

# {few_shot_examples}

# Now translate the following natural language query into an accurate SQL query:

# NL: {nl_query}
# SQL:
# """

#     return call_groq_api(prompt)

# # Endpoint to generate final submission file from sample_submission_generate_task.json
# @app.route('/generate_submission', methods=['GET'])
# def generate_submission():
#     with open('sample_submission_generate_task.json', 'r') as f:
#         submission_tasks = json.load(f)

#     final_submission = []
    
#     for task in submission_tasks:
#         nl_query = task["NL"]
#         print(f"Generating SQL for: {nl_query}")
        
#         generated_sql = generate_sql_from_nl(nl_query)
        
#         if generated_sql:
#             final_submission.append({
#                 "NL": nl_query,
#                 "Query": generated_sql
#             })
#             print(f"✅ Generated: {generated_sql}")
#         else:
#             final_submission.append({
#                 "NL": nl_query,
#                 "Query": "Generation Failed"
#             })
#             print("❌ Generation Failed")

#     # Save the generated queries to a new JSON file
#     with open('final_submission_generate_task.json', 'w') as outfile:
#         json.dump(final_submission, outfile, indent=2)

#     return jsonify({"message": "Submission file generated successfully!", 
#                     "submission_file": "final_submission_generate_task.json",
#                     "results": final_submission})

# if __name__ == "__main__":
#     app.run(debug=True)






# import os, json, time
# from dotenv import load_dotenv
# from flask import Flask, jsonify
# from database import list_all_tables, get_table_schema
# from groq import Groq

# load_dotenv()

# app = Flask(__name__)

# # Initialize Groq client
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# # Load training examples for few-shot prompts
# with open('train_generate_task.json', 'r') as f:
#     nl_to_sql_examples = json.load(f)

# def get_db_schema_context():
#     tables = list_all_tables(os.getenv("DB_NAME"), os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_HOST"), os.getenv("DB_PORT"))
#     schema_context = ""
#     for table in tables:
#         columns = get_table_schema(os.getenv("DB_NAME"), os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_HOST"), os.getenv("DB_PORT"), table)
#         schema_context += f"Table {table} columns: {', '.join(columns.keys())}\n"
#     return schema_context

# def generate_sql_from_nl(nl_query):
#     schema_context = get_db_schema_context()
    
#     few_shot_examples = "\n\n".join(
#         [f"NL: {ex['NL']}\nSQL: {ex['Query']}" for ex in nl_to_sql_examples[:3]]
#     )

#     prompt = f"""
# You are an expert SQL assistant. Given the database schema below:

# {schema_context}

# Here are examples of translating natural language queries into SQL:

# {few_shot_examples}

# Translate this natural language query into SQL accurately:

# NL: {nl_query}
# SQL:
# """
#     try:
#         chat_completion = client.chat.completions.create(
#             messages=[{"role": "user", "content": prompt}],
#             model="mixtral-8x7b-32768",
#             temperature=0,
#             max_tokens=500,
#         )
#         return chat_completion.choices[0].message.content.strip()
#     except Exception as e:
#         print(f"Groq API Error: {e}")
#         return None

# @app.route('/generate_submission', methods=['GET'])
# def generate_submission():
#     with open('sample_submission_generate_task.json', 'r') as f:
#         submission_tasks = json.load(f)

#     final_submission = []

#     for task in submission_tasks:
#         nl_query = task["NL"]
#         print(f"Generating SQL for: {nl_query}")

#         generated_sql = generate_sql_from_nl(nl_query)

#         retries = 0
#         while generated_sql is None and retries < 3:
#             print(f"Retrying ({retries+1})...")
#             time.sleep(2)
#             generated_sql = generate_sql_from_nl(nl_query)
#             retries += 1

#         if generated_sql:
#             # Remove unwanted backslashes from the generated SQL query
#             clean_sql = generated_sql.replace("\\", "")
#             final_submission.append({"NL": nl_query, "Query": clean_sql})
#             print(f"✅ Generated (cleaned): {clean_sql}")
#         else:
#             final_submission.append({"NL": nl_query, "Query": "Generation Failed"})
#             print("❌ Generation Failed after retries")

#     with open('final_submission_generate_task.json', 'w') as outfile:
#         json.dump(final_submission, outfile, indent=2)

#     return jsonify({
#       "message": "Submission file generated successfully!",
#       "submission_file": "final_submission_generate_task.json",
#       "results": final_submission
#     })

# if __name__ == "__main__":
#     app.run(debug=True)



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