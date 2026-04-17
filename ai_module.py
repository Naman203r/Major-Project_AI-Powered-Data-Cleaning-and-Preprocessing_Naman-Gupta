import requests

def ask_ai(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]
    except Exception as e:
        return f"AI Error: {e}"