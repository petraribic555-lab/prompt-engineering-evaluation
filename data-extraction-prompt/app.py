import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

system_prompt = """
You are a business information extraction assistant.

Task:
Extract structured information from the provided supplier message.

Instructions:
- Use only information explicitly present in the source text.
- Do not infer missing values.
- If a value is not provided, return null.
- Set "requires_follow_up" to true if important information required to process the supplier message is missing or unclear.
- Set "requires_follow_up" to false only when the extracted information is sufficiently complete for processing.
- Include every missing or unclear required field in "missing_information".
- A partial date such as a month without a specific day may be extracted as provided, but should also be listed in "missing_information" as an incomplete effective date.
- Preserve names, dates, percentages, and commercial terms exactly when possible.
- Do not add explanations outside the JSON.
- Return valid JSON only.

Return exactly this JSON structure:

{
  "supplier_name": null,
  "effective_date": null,
  "price_change_percentage": null,
  "affected_products": [],
  "payment_terms": null,
  "contact_person": null,
  "requires_follow_up": false,
  "missing_information": []
}
"""

print("Paste the supplier message below.")
print("When finished, type END on a new line.\n")

lines = []

while True:
    line = input()

    if line.strip() == "END":
        break

    lines.append(line)

source_text = "\n".join(lines)

response = client.responses.create(
    model="gpt-4.1-mini",
    instructions=system_prompt,
    input=source_text
)

raw_output = response.output_text

print("\n==============================")
print("RAW MODEL OUTPUT")
print("==============================\n")

print(raw_output)

print("\n==============================")
print("JSON VALIDATION")
print("==============================\n")

try:
    extracted_data = json.loads(raw_output)

    print("Valid JSON received.\n")
    print(json.dumps(extracted_data, indent=2))

except json.JSONDecodeError as e:
    print("Invalid JSON returned by the model.")
    print(f"Error: {e}")