import csv
import json
import time
import os
import requests
from dotenv import load_dotenv, dotenv_values

def classify(text):
    prompt = f"""Classify the following customer book review.

Review: "{text}"

Respond ONLY with a valid JSON object in this exact format:
{{
    "verdict": "positive" | "negative" | "neutral",
    "topic": one short English word or phrase (e.g. "delivery", "plot", "characters", "price")
}}
"""

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv("API_KEY")}",
            "Content-Type": "application/json",
        },
        json={
            "model": "nvidia/nemotron-3-super-120b-a12b:free",
            "messages":
                [
                    {"role": "user", "content": prompt}
                ],
            "max_tokens": 300,
            "reasoning": {"enabled": False},
        },
    )

    print(response.text)

    raw = response.json()["choices"][0]["message"]["content"].strip()

    print(raw)

    return json.loads(raw)

def main():

    results = []

    load_dotenv()

    with open(os.getenv("INPUT_FILE"), newline="", encoding="utf-8") as f:
        dictlist = list(csv.DictReader(f))

    for i in dictlist:
        id = i.get('id')
        text = i.get('text')
        classify_result = classify(text)
        result = {
            "id": id,
            "text": text,
            "sentiment": classify_result.get("verdict"),
            "topic": classify_result.get("topic"),
        }
        results.append(result)

        time.sleep(0.3)

    with open(os.getenv("OUTPUT_FILE"), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

main()