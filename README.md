# Phase 2: Prompt Engineering and Evaluation

This phase focuses on designing, testing, evaluating, and organizing prompts for practical AI applications.

The goal was not only to write better prompts, but to understand how prompt structure affects model behavior, source fidelity, hallucination risk, structured output, and evaluation quality.

## Topics Covered

- zero-shot prompting
- few-shot prompting
- role prompting
- structured output
- JSON output
- evaluation rubrics
- factuality
- completeness
- relevance
- instruction following
- tone control
- hallucination checks
- LLM-as-a-judge
- prompt iteration
- reusable prompt libraries

## Mini Projects

### 1. SOP Prompt Generator

Converts unstructured business process descriptions into structured Standard Operating Procedures.

Key focus areas:

- source fidelity
- preserving business rules
- avoiding invented process steps
- handling missing information
- iterative prompt refinement

### 2. Table Analysis Prompt

Analyzes business tables and separates direct observations from possible interpretations.

Key focus areas:

- numerical comparison
- trade-off analysis
- avoiding unsupported causal claims
- distinguishing facts from implications

### 3. Structured Data Extraction

Extracts predefined business information from unstructured supplier messages and returns valid JSON.

Key focus areas:

- JSON output
- `null` handling
- missing information detection
- follow-up logic
- JSON validation in Python
- schema semantics

### 4. AI Response Evaluator

Uses an LLM to evaluate another AI response using a structured rubric.

Evaluation criteria:

- Factuality
- Completeness
- Relevance
- Instruction Following

Key focus areas:

- LLM-as-a-judge
- structured scoring
- overall score calculation
- evaluator hallucinations
- avoiding double counting across criteria

### 5. Prompt Library

Organizes tested prompts into reusable Python components.

Key focus areas:

- reusable prompts
- modular prompt design
- prompt maintenance
- separating prompt logic from application logic

## Project Structure

```text
phase-2-prompt-engineering/
├── README.md
├── sop-prompt-generator/
│   ├── app.py
│   ├── README.md
│   ├── requirements.txt
│   ├── .gitignore
│   └── .env
│
├── table-analysis-prompt/
│   ├── app.py
│   ├── README.md
│   ├── requirements.txt
│   ├── .gitignore
│   └── .env
│
├── data-extraction-prompt/
│   ├── app.py
│   ├── README.md
│   ├── requirements.txt
│   ├── .gitignore
│   └── .env
│
├── ai-response-evaluator/
│   ├── app.py
│   ├── README.md
│   ├── requirements.txt
│   ├── .gitignore
│   └── .env
│
└── prompt-library/
    ├── README.md
    ├── prompts.py
    └── example_usage.py
```

## Key Learnings

### 1. Prompt quality depends on explicit constraints

Generic instructions such as "do not infer" may not be enough.

Models often need:

- semantic constraints
- explicit prohibited transformations
- clear source-fidelity rules
- validation steps

### 2. Structured output requires schema design

Returning valid JSON is not sufficient.

The meaning and expected type of every field must also be defined.

### 3. Business implications are not the same as facts

A model may turn a metric into an unsupported operational conclusion.

Examples:

- longer lead time does not automatically mean unreliable delivery
- longer payment terms do not prove improved cash flow
- higher defect rate does not prove higher total cost

### 4. Evaluation models can also make mistakes

LLM-as-a-judge can improve evaluation consistency, but the evaluator itself must be tested.

An evaluator can:

- hallucinate omissions
- double-count the same issue
- misinterpret criteria
- score inconsistently

### 5. Prompts should be treated as software components

Prompt libraries make prompts easier to:

- reuse
- maintain
- test
- version
- improve

## Tech Stack

- Python
- OpenAI API
- OpenAI Python SDK
- python-dotenv
- Python JSON module
- Git
- GitHub

## Outcome

By the end of this phase, the project demonstrates practical understanding of prompt engineering, structured output, evaluation, hallucination control, and reusable prompt architecture.

The phase moves from simple prompt writing toward a more engineering-oriented approach in which prompts are tested, evaluated, validated, and maintained as part of an AI application.