import requests
import re
import json

def classify_violations_llm(prompt, api_endpoint, headers):

    data = {
        "model": "mistral-medium",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }

    response = requests.post(api_endpoint, headers=headers, json=data)

    if response.status_code != 200:
        raise ValueError(f"API error: {response.status_code} - {response.text}")

    content = response.json()["choices"][0]["message"]["content"].strip()
    match = re.search(r"```json(.*?)```", content, re.DOTALL)
    if not match:
        raise ValueError("No JSON block found in the model response.")

    try:
        return json.loads(match.group(1).strip())
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON decode error: {e}")