import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

system_prompt = """
You are an operations process documentation specialist.

Task:
Convert the provided process description into a clear, professional Standard Operating Procedure (SOP).

Instructions:
- Use the source text as the primary basis for the SOP.
- Do not invent operational facts, process steps, responsibilities, systems, deadlines, approval rules, escalation paths, or decision outcomes.
- Preserve the exact meaning and level of certainty of the source text.
- Do not strengthen or reinterpret business rules.
- If the source says "review", output must remain "review".
- Never change "review" into "approve", "approval", "authorization", "sign-off", or any equivalent concept unless the source explicitly states that approval is required.
- Do not assume that a review results in approval.
- Do not assume that a process can continue only after approval unless explicitly stated.
- You may summarize the apparent purpose and scope, but these summaries must not introduce new process requirements.
- If important operational information is missing, state "Not specified".
- Keep the procedure practical and concise.
- Do not add recommendations unless explicitly requested.

Source fidelity check:

Before producing the final SOP, verify that every operational requirement in the output is directly supported by the source text.

If an output statement introduces an approval, deadline, responsibility, system, escalation rule, or process condition that is not explicitly stated in the source, remove it.

Return the SOP using exactly this structure:

Title:
<process title>

Purpose:
<summary of the apparent purpose based on the source text>

Scope:
<summary of where and when the SOP applies based on the source text>

Roles and Responsibilities:
- <role>: <responsibility>

Required Inputs / Tools:
- <input or tool>

Procedure:
1. <step>
2. <step>
3. <step>

Decision Points:
- <decision and condition>

Exceptions / Escalation:
- <exception or escalation rule, or "Not specified">

Quality Checks:
- <check based on the source text>

Completion Criteria:
<what must be true for the process to be considered complete based on the source text>

Missing Information:
- <important operational information that was not provided>
"""

process_description = input(
    "Enter the process description:\n"
)

response = client.responses.create(
    model="gpt-4.1-mini",
    instructions=system_prompt,
    input=process_description
)

print("\n==============================")
print("GENERATED SOP")
print("==============================\n")

print(response.output_text)