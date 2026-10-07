# AI Response Evaluator

A prompt-engineering mini project for evaluating AI-generated answers against a user request and, optionally, a reference answer.

## Overview

The project demonstrates how one language model can be used to evaluate the output of another model using a structured scoring rubric.

The evaluator scores responses across four criteria:

- Factuality
- Completeness
- Relevance
- Instruction Following

Each criterion is scored from 1 to 5 and accompanied by a short explanation.

The evaluator also returns:

- overall score
- main issue
- final verdict

## Key Concepts

This project focuses on:

- LLM-as-a-judge
- evaluation rubrics
- structured scoring
- JSON output
- automatic score calculation
- separating evaluation criteria
- avoiding double counting
- detecting evaluator hallucinations

## Evaluation Criteria

### Factuality

Measures whether claims are accurate and supported by the available information.

### Completeness

Measures whether the response addresses all important parts of the user request.

### Relevance

Measures whether the response stays focused on the requested task.

### Instruction Following

Measures whether the response follows explicit constraints such as format, length, required elements, source restrictions, and prohibited content.

## Overall Score

The overall score is calculated as the arithmetic mean of the four criterion scores.

Example:

```text
Factuality: 4
Completeness: 5
Relevance: 5
Instruction Following: 4

Overall Score = (4 + 5 + 5 + 4) / 4 = 4.5
```

## Important Evaluation Rules

The evaluator is instructed to:

- evaluate each criterion independently
- avoid penalizing the same issue across multiple criteria unless necessary
- check explicit user requirements before scoring completeness
- avoid penalizing information that was never requested
- verify that information is actually missing before claiming an omission
- treat unsupported assumptions and causal claims as factuality issues
- distinguish factual errors from completeness issues

## Example Finding

During testing, the evaluator correctly detected a factual error where an AI response stated that a supplier had a 24-day lead time instead of the provided 28 days.

However, the evaluator also incorrectly claimed that another supplier's defect rate had been omitted even though it was present in the response.

This demonstrated an important limitation:

An AI evaluator can itself make mistakes or hallucinate.

Therefore, LLM-based evaluation should not automatically be treated as ground truth.

## JSON Output

The evaluator returns structured JSON in the following format:

```json
{
  "factuality": {
    "score": 4,
    "reason": "..."
  },
  "completeness": {
    "score": 5,
    "reason": "..."
  },
  "relevance": {
    "score": 5,
    "reason": "..."
  },
  "instruction_following": {
    "score": 4,
    "reason": "..."
  },
  "overall_score": 4.5,
  "main_issue": "...",
  "verdict": "..."
}
```

The JSON response is validated in Python using:

```python
json.loads(raw_output)
```

## Project Structure

```text
ai-response-evaluator/
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

The program asks for:

1. the original user request
2. the AI-generated response
3. an optional reference answer

Type `END` on a new line after each multi-line input.

## Key Learning

LLM-based evaluation can improve consistency and scalability, but the evaluator itself must also be tested.

A structured rubric helps reduce ambiguity, but evaluation quality still depends on:

- clear scoring definitions
- criterion independence
- source grounding
- deterministic score calculation
- validation of evaluator behavior