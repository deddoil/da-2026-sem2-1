import csv
import json
import time
import os
import requests
from dotenv import load_dotenv, dotenv_values

def classify(text):

    return {"verdict": "verdict","topic": "topic"}

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

    with open(os.getenv("OUTPUT_FILE"), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

main()