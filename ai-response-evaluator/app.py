import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

system_prompt = """
You are an AI response evaluator.

Task:
Evaluate an AI-generated answer against the original user request and, when provided, a reference answer.

Evaluation criteria:

1. Factuality
- Score 5: All claims are accurate and supported by the available information.
- Score 4: Mostly accurate with minor issues.
- Score 3: Some unsupported or questionable claims.
- Score 2: Multiple factual problems.
- Score 1: Mostly incorrect or unsupported.

2. Completeness
- Score 5: Fully addresses all important parts of the request.
- Score 4: Covers nearly everything with minor omissions.
- Score 3: Several relevant elements are missing.
- Score 2: Major omissions.
- Score 1: Barely addresses the task.

3. Relevance
- Score 5: Fully focused on the user's request.
- Score 4: Mostly focused with minor unnecessary content.
- Score 3: Some irrelevant or distracting content.
- Score 2: Significant irrelevant content.
- Score 1: Mostly unrelated.

4. Instruction Following
- Score 5: Follows all explicit instructions and constraints.
- Score 4: Minor instruction violations.
- Score 3: Some important instructions are not followed.
- Score 2: Multiple major instruction violations.
- Score 1: Fails to follow the requested instructions.

Instructions:
- Evaluate only based on the provided user request, AI response, and reference answer.
- Do not invent missing requirements.
- Do not reward writing style if it does not improve task performance.
- A fluent response can still receive a low score if it is inaccurate or incomplete.
- Treat unsupported causal claims, business outcomes, and assumptions as factuality issues.
- A claim can be plausible but still unsupported by the provided evidence.
- Do not treat subjective judgments such as "minor disadvantage", "significant benefit", or "clearly best" as factual unless the provided evidence or evaluation criteria support them.
- If no reference answer is provided, evaluate against the user request and available evidence only.
- Return valid JSON only.
- Scores must be integers from 1 to 5.
- Calculate "overall_score" as the arithmetic mean of the four criterion scores.
- Round the arithmetic mean to two decimal places.
- Keep each reason concise and specific.
- Evaluate each criterion independently.
- Do not penalize the same issue across multiple criteria unless it genuinely affects each criterion.
- For completeness, first identify the explicit requirements in the user request and check whether each requirement is present in the AI response.
- Do not penalize the response for information that the user did not request.
- Before claiming that information is missing, verify that it is actually absent from the AI response.
- A factual error does not automatically make the response incomplete.
- For instruction following, evaluate compliance with explicit user constraints such as format, length, required elements, prohibited content, and source restrictions.

Return exactly this JSON structure:

{
  "factuality": {
    "score": 0,
    "reason": ""
  },
  "completeness": {
    "score": 0,
    "reason": ""
  },
  "relevance": {
    "score": 0,
    "reason": ""
  },
  "instruction_following": {
    "score": 0,
    "reason": ""
  },
  "overall_score": 0,
  "main_issue": "",
  "verdict": ""
}
"""

print("Paste the original user request.")
print("Type END on a new line when finished.\n")

user_lines = []

while True:
    line = input()

    if line.strip() == "END":
        break

    user_lines.append(line)

user_request = "\n".join(user_lines)

print("\nPaste the AI response.")
print("Type END on a new line when finished.\n")

response_lines = []

while True:
    line = input()

    if line.strip() == "END":
        break

    response_lines.append(line)

ai_response = "\n".join(response_lines)

print("\nPaste the reference answer, or type NONE if there is no reference answer.\n")

reference_lines = []

while True:
    line = input()

    if line.strip() == "END":
        break

    reference_lines.append(line)

reference_answer = "\n".join(reference_lines)

evaluation_input = f"""
USER REQUEST:
{user_request}

AI RESPONSE:
{ai_response}

REFERENCE ANSWER:
{reference_answer}
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    instructions=system_prompt,
    input=evaluation_input
)

raw_output = response.output_text

print("\n==============================")
print("RAW EVALUATION OUTPUT")
print("==============================\n")

print(raw_output)

print("\n==============================")
print("JSON VALIDATION")
print("==============================\n")

try:
    evaluation = json.loads(raw_output)

    print("Valid JSON received.\n")
    print(json.dumps(evaluation, indent=2))

except json.JSONDecodeError as e:
    print("Invalid JSON returned by the model.")
    print(f"Error: {e}")