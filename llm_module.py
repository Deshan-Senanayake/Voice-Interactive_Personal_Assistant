# llm_module.py

import requests

def ask_ollama(prompt, model="llama2"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt},
        stream=True
    )

    result = ""
    for line in response.iter_lines():
        if line:
            try:
                json_data = line.decode("utf-8")
                # Each line is a JSON object like: {"response": "..."}
                if '"response":' in json_data:
                    text = json_data.split('"response":')[1].split('"')[1]
                    result += text
            except Exception as e:
                print(f"Error decoding line: {e}")
                continue
    return result
