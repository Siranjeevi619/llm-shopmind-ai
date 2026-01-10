import os
from langchain.prompts import PromptTemplate
from core.llm import llm

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_PATH = os.path.join(BASE_DIR, "..", "prompts", "admin_action.txt")

with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    prompt_text = f.read()

prompt = PromptTemplate(
    template=prompt_text,
    input_variables=["message"]
)

VALID_KEYS = {"action", "product", "quantity", "time_range"}

def clean_value(value: str):
    value = value.strip().strip(",")

    if value.lower() == "null":
        return None

    # remove surrounding quotes
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1]

    if value.isdigit():
        return int(value)

    return value

def parse_admin_command(message: str) -> dict:
    chain = prompt | llm
    result = chain.invoke({"message": message})

    raw = result.content.strip()
    lines = raw.splitlines()

    data = {
        "action": "UNKNOWN",
        "product": None,
        "quantity": None,
        "time_range": None
    }

    for line in lines:
        if ":" not in line:
            continue

        key, value = line.split(":", 1)

        key = key.strip().strip('"')
        value = value.strip()

        if key not in VALID_KEYS:
            continue

        data[key] = clean_value(value)

    return data
