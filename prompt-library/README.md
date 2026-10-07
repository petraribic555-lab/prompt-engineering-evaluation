# Prompt Library

A reusable prompt library created during Phase 2 of the AI Engineering learning project.

The goal of this mini project is to organize tested prompt patterns into reusable Python components that can be imported into future AI applications.

## Included Prompts

The library currently includes four prompt templates:

### SOP Prompt

Converts unstructured process descriptions into structured Standard Operating Procedures.

Key focus areas:

- source fidelity
- avoiding invented process steps
- preserving business rules
- handling missing information
- structured output

### Table Analysis Prompt

Analyzes tabular business data while separating direct observations from interpretations.

Key focus areas:

- numerical comparisons
- business trade-offs
- avoiding unsupported causal claims
- distinguishing facts from implications
- identifying missing information

### Data Extraction Prompt

Extracts structured business information from supplier messages.

Key focus areas:

- JSON output
- missing values
- `null` handling
- follow-up logic
- structured information extraction

### AI Evaluator Prompt

Evaluates AI-generated responses using a structured rubric.

Evaluation criteria:

- Factuality
- Completeness
- Relevance
- Instruction Following

The evaluator also calculates an overall score.

## Project Structure

```text
prompt-library/
├── README.md
├── prompts.py
└── example_usage.py
```

## Using the Library

Prompts can be imported directly from `prompts.py`.

Example:

```python
from prompts import DATA_EXTRACTION_PROMPT
```

The imported prompt can then be used in an OpenAI API request:

```python
response = client.responses.create(
    model="gpt-4.1-mini",
    instructions=DATA_EXTRACTION_PROMPT,
    input=source_text
)
```

## Available Imports

```python
from prompts import (
    SOP_PROMPT,
    TABLE_ANALYSIS_PROMPT,
    DATA_EXTRACTION_PROMPT,
    AI_EVALUATOR_PROMPT
)
```

## Why Use a Prompt Library?

Keeping prompts in a separate module makes AI applications easier to:

- maintain
- test
- reuse
- improve
- version
- compare

It also separates prompt logic from application logic.

Instead of storing large prompts directly inside every application file, prompts can be maintained centrally and reused across multiple applications.

## Key Learning

Prompt engineering is not only about writing better instructions.

Production-oriented prompt design also requires:

- consistent structure
- reusable prompt components
- explicit business rules
- hallucination controls
- output format definitions
- evaluation criteria
- clear separation between prompts and application code

This mini project demonstrates how prompts can begin to be treated as reusable software components rather than one-off text instructions.