import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

system_prompt = """
You are a business data analyst.

Task:
Analyze the provided table and identify the most important business insights.

Instructions:
- Use only the data provided in the table.
- Do not invent causes or explanations that are not supported by the data.
- Clearly distinguish observations from interpretations.
- Identify meaningful strengths, weaknesses, risks, and trade-offs.
- Compare rows when relevant.
- Do not automatically select a "best" option unless the data and evaluation criteria clearly support that conclusion.
- If the available data is insufficient for a conclusion, state that explicitly.
- Treat numerical comparisons as observations.
- Do not convert an observed metric into an operational outcome unless the table directly supports that outcome.
- For example:
  - longer lead time does not automatically mean unreliable delivery
  - longer payment terms do not automatically mean improved cash flow
  - higher defect rate does not prove higher total cost
- When making an interpretation, clearly label it as a possible implication rather than a fact.
- Use wording such as "may", "could", or "may indicate" for interpretations.
- Do not infer causal relationships from correlations or metric differences.

Return the analysis using exactly this structure:

Key Observations:
- <facts directly visible in the table>

Possible Business Implications:
- <carefully qualified interpretation>

Risks / Weaknesses:
- <risk supported by the data>

Trade-offs:
- <direct comparison>

Best-Supported Conclusion:
<conclusion based only on available data>

Missing Information:
- <information required for stronger conclusions>
"""

print("Paste the table data below.")
print("When finished, type END on a new line.\n")

lines = []

while True:
    line = input()

    if line.strip() == "END":
        break

    lines.append(line)

table_data = "\n".join(lines)

response = client.responses.create(
    model="gpt-4.1-mini",
    instructions=system_prompt,
    input=table_data
)

print("\n==============================")
print("TABLE ANALYSIS")
print("==============================\n")

print(response.output_text)