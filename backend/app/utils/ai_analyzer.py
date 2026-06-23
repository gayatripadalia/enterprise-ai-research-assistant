import requests

def analyze_text(text: str):
    url = "http://localhost:11434/api/generate"

    prompt = f"""
You are an AI assistant. Analyze the following document and give a short, clear summary:

{text}
"""

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)

    return response.json()["response"]

def answer_question(context: str, question: str):

    url = "http://localhost:11434/api/generate"

    prompt = f"""
You are an AI assistant.

Answer the question using ONLY the document below.

Document:
{context}

Question:
{question}

Answer:
"""

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)

    return response.json()["response"]