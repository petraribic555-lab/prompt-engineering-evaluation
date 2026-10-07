# Structured Data Extraction Prompt

A prompt-engineering mini project for extracting structured business information from unstructured supplier messages and returning the result as valid JSON.

## Overview

The project demonstrates how an LLM can transform free-text business communication into structured data that could later be used in workflows, databases, dashboards, ERP systems, or AI agents.

The model is instructed to extract predefined fields, avoid unsupported assumptions, return `null` for missing values, and produce JSON only.

## Extracted Fields

The current version extracts:

- supplier name
- effective date
- price change percentage
- affected products
- payment terms
- contact person
- follow-up requirement
- missing information

## Key Concepts

This mini project focuses on:

- structured output
- JSON generation
- source-grounded extraction
- handling missing values
- avoiding hallucinated fields
- validating model output in Python

## JSON Validation

The model output is validated with Python using:

```python
json.loads(raw_output)
```

If the response is not valid JSON, the program reports a parsing error.

## Project Structure

```text
data-extraction-prompt/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

## Tech Stack

- Python
- OpenAI API
- OpenAI Python SDK
- python-dotenv
- Python JSON module

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

Run the application:

```bash
python app.py
```

The program accepts a multi-line supplier message. Type `END` on a new line when the input is complete.