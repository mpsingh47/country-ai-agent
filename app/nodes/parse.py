# from pydantic import BaseModel, Field
# from typing import List
# from app.utils.llm import llm

# class ParseOutput(BaseModel):
#     country: str = Field(description="Country name")
#     fields: List[str] = Field(description="Fields like capital, population, currency")

# structured_llm = llm.with_structured_output(ParseOutput)

# def parse_query(state):
#     query = state["query"]

#     try:
#         result = structured_llm.invoke(query)

#         return {
#             "country": result.country,
#             "fields": result.fields if result.fields else ["capital", "population"]
#         }

#     except Exception as e:
#         print(e)
#         return {
#             "error": "Failed to parse query"
#         }




import json
from app.utils.llm import llm

def parse_query(state):
    query = state["query"]

    prompt = f"""
    Extract the country and requested fields from the query.

    Query: "{query}"

    Return ONLY valid JSON in this format:
    {{
        "country": "country name",
        "fields": ["capital", "population", "currency"]
    }}

    Rules:
    - If no fields mentioned, use ["capital", "population"]
    - Only include relevant fields from: capital, population, currency, region
    - Do NOT add extra text
    """

    try:
        res = llm.invoke(prompt)
        content = res.content.strip()

        # Try to extract JSON safely
        start = content.find("{")
        end = content.rfind("}") + 1
        json_str = content[start:end]

        parsed = json.loads(json_str)

        return {
            "country": parsed.get("country"),
            "fields": parsed.get("fields", ["capital", "population"])
        }

    except Exception:
        return {
            "error": "Failed to parse query"
        }