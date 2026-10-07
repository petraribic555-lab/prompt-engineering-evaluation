# SOP Prompt Generator

A prompt-engineering mini project for converting unstructured business process descriptions into structured Standard Operating Procedures (SOPs).

## Overview

The goal of this project is to test how prompt design affects source fidelity, structured output, and hallucination risk when generating SOP documentation from short process descriptions.

The project uses a Python application connected to an LLM API and iterates through multiple prompt versions based on evaluation results.

## Problem

The initial prompt successfully generated structured SOPs, but the model introduced unsupported business logic.

For example, the source text stated that price increases above 10% must be reviewed by a category manager.

The model repeatedly transformed this into an approval requirement, introducing phrases such as:

- "review and approve"
- "upon approval"
- "approved supplier price list"

This changed the meaning of the source process and reduced factuality.

## Prompt Iteration

### Version 1

The first prompt instructed the model to:

- use only explicitly provided information
- avoid inventing missing process steps
- generate a structured SOP
- identify missing information

The output structure was strong, but the model inferred an approval process that was not present in the source.

### Version 2

The prompt was updated with an explicit instruction not to convert a review requirement into an approval requirement.

The issue still persisted, showing that a simple negative instruction was not sufficient.

### Version 3

The final prompt added:

- semantic fidelity rules
- explicit prohibited transformations
- preservation of the original level of certainty
- a source-fidelity verification step before producing the final output

This version successfully preserved the original meaning of the process without introducing approval requirements.

## Evaluation

The outputs were evaluated using:

- Factuality
- Completeness
- Relevance
- Instruction following

### Results

Version 1:
- Factuality: 4/5
- Completeness: 5/5
- Relevance: 5/5
- Instruction following: 4/5

Version 2:
- Factuality: 3/5
- Completeness: 5/5
- Relevance: 5/5
- Instruction following: 3/5

Version 3:
- Factuality: 5/5
- Completeness: 5/5
- Relevance: 5/5
- Instruction following: 5/5

## Key Learning

A generic instruction such as "do not infer missing information" may not be enough to prevent semantic drift.

For high-fidelity business process generation, prompts benefit from:

- explicit semantic constraints
- prohibited transformation rules
- clear separation between summarization and invention
- verification steps before final output
- structured evaluation after each prompt iteration

## Project Structure

```text
sop-prompt-generator/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── evaluation_notes.md
└── prompt_versions/
    ├── v1_prompt.txt
    ├── v2_prompt.txt
    └── v3_prompt.txt
```

## Tech Stack

- Python
- OpenAI API
- OpenAI Python SDK
- python-dotenv

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

Run:

```bash
python app.py
```