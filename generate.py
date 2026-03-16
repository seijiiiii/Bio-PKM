import os
from dotenv import load_dotenv
from google import genai
import time

load_dotenv()

# Initialise, API_KEY = your own api key
def get_client():
    print("API Called")
    # API_KEY = os.getenv("API_KEY")
    #print("DEBUG API:", API_KEY)
    if not API_KEY:
        raise ValueError("API_KEY not found")
    return genai.Client(api_key=API_KEY)

def generate_data(text_input, API_KEY):
    prompt = """
    Extract core biological concepts (including mechanism, protein, structure) and return STRICT JSON.

    Schema:
    [
    {
        "name": "",
        "definition": "- Definition:",
        "role": "- Role:",
        "context": "- Context:"
    }
    ]

    Example:
    [
    {
        "name": "aaRS",
        "definition": "- Definition: Enzyme linking amino acid to tRNA before translation",
        "role": "- Role:\n   1. linking amino acid to tRNA\n   2. tRNA proofreading and editing\n - Position/Stage: post-transcription",
        "context": "- Context: before translation / during transcription"
    }
    ]

    Rules:
    - STRICTLY FOLLOW THE SCHEMA!!STRICTLY FOLLOW THE SCHEMA!!STRICTLY FOLLOW THE SCHEMA!!
    - Return ONLY valid JSON.
    - No extra text.
    - Use escape sequences and unicode, and retain indentation
    - Do NOT output generic context, include full but CONCISE pathway context
    - BE CLEAR
    - Do NOT generate markdown code block
    """
    # client = get_client()

    client = genai.Client(api_key=API_KEY)
    print("Starting extraction...")

    start = time.time()

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt + "\n\n" + text_input
    )

    end = time.time()

    print("Time used:", end - start)
    print("Raw output:")
    print(response.text)

    # Change posible markdown into strict json
    text_output = response.text.strip()
    if text_output.startswith("```"):
        text_output = text_output.replace("```json", "")
        text_output = text_output.replace("```", "")
        text_output = text_output.strip()

    return text_output

