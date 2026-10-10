# Классификотор отзывов

Скрипт читает отзывы покупателей из CSV-файла, отправляет каждый в LLM через API (Groq) и сохраняет структурированный результат (тональность + тема) в JSON.

## Как это работает

1. Скрипт читает отзывы из `reviews.csv` и формирует список словарей с парами ключ-значение под `id` клиента и текст отзыва;
2. Текст очередного отзыва вставляется в промпт, отсылаемый модели (используется Nvidia Nemotron 3 Super)
3. LLM возвращает JSON с полями `verdict` и `topic`, из них формируется словарь с ключами `id`, `text`, `topic`, `sentiment` и помещается в список с результатами
4. Все результаты сохраняются в `results.json`

## Структура проекта

```
da-2026-sem2-1/
├──example.env             # пример файла переменных окружения
├──input_example.csv       # пример выходных данных
├── main.py                # основной скрипт
├──output_example.json     # пример входных данных
├── README.md
└── requirements.txt       # зависимости
```

## Установка и запуск

### 1. Установить зависимости

```bash
pip install requirements.txt
```

### 2. Получить API-ключ

На [openrouter.ai](https://openrouter.ai), создать аккаунт и в разделе [API Keys](https://openrouter.ai/workspaces/default/keys) создать api-ключ

### 3. Создать .env

Создать файл .env в каталоге со скриптом, внести в него api-ключ, имена входного и выходного файлов (example.env — пример файла)

### 4. Запустить скрипт

```bash
python main.py
```

## Пример входных данных (`reviews.csv`)

```csv
id,text
1,"The book arrived in perfect condition and the story had me hooked from the very first page. Absolutely loved it!"
2,"Incredibly boring and poorly written. I could barely finish the first chapter. Total waste of time."
3,"It's a decent read, nothing extraordinary. Arrived on time."
4,"The author's writing style is beautiful and the characters felt so real. Five stars for this masterpiece!"
5,"The plot was way too predictable and the ending felt rushed. Very disappointed."
6,"Shipping took three weeks. No updates from the seller whatsoever."
7,"Exactly as described. A gripping story with well-developed characters. Good value for money."
8,"Amazing book! My whole family enjoyed reading it. Will definitely order more from this author."
9,"The cover was different from the photo on the website. A bit misleading."
10,"Fast shipping, solid packaging, and the book is in great condition. No complaints at all."
```

## Пример выходных данных (`results.json`)

```json
[
  {
    "id": "1",
    "text": "The book arrived in perfect condition and the story had me hooked from the very first page. Absolutely loved it!",
    "sentiment": "positive",
    "topic": "plot"
  },
  {
    "id": "2",
    "text": "Incredibly boring and poorly written. I could barely finish the first chapter. Total waste of time.",
    "sentiment": "negative",
    "topic": "plot"
  },
  {
    "id": "3",
    "text": "It's a decent read, nothing extraordinary. Arrived on time.",
    "sentiment": "neutral",
    "topic": "delivery"
  },
  {
    "id": "4",
    "text": "The author's writing style is beautiful and the characters felt so real. Five stars for this masterpiece!",
    "sentiment": "positive",
    "topic": "characters"
  },
  {
    "id": "5",
    "text": "The plot was way too predictable and the ending felt rushed. Very disappointed.",
    "sentiment": "negative",
    "topic": "plot"
  },
  {
    "id": "6",
    "text": "Shipping took three weeks. No updates from the seller whatsoever.",
    "sentiment": "negative",
    "topic": "delivery"
  },
  {
    "id": "7",
    "text": "Exactly as described. A gripping story with well-developed characters. Good value for money.",
    "sentiment": "positive",
    "topic": "characters"
  },
  {
    "id": "8",
    "text": "Amazing book! My whole family enjoyed reading it. Will definitely order more from this author.",
    "sentiment": "positive",
    "topic": "plot"
  },
  {
    "id": "9",
    "text": "The cover was different from the photo on the website. A bit misleading.",
    "sentiment": "negative",
    "topic": "cover"
  },
  {
    "id": "10",
    "text": "Fast shipping, solid packaging, and the book is in great condition. No complaints at all.",
    "sentiment": "positive",
    "topic": "condition"
  }
]
```
