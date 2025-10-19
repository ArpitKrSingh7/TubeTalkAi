from openai import OpenAI
import ast
from config import GOOGLE_API_KEY, GOOGLE_API_URL
from prompts import QUERY_REWRITE_PROMPT

client = OpenAI(api_key=GOOGLE_API_KEY, base_url=GOOGLE_API_URL)

def rewrite_queries(user_query: str):
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        temperature=0.6,
        messages=[
            {"role": "system", "content": QUERY_REWRITE_PROMPT},
            {"role": "user", "content": user_query},
        ],
    )
    rewritten = response.choices[0].message.content.strip()
    try:
        rewritten_list = ast.literal_eval(rewritten)
    except Exception as e:
        print("⚠️ Failed to parse rewritten queries:", e)
        rewritten_list = [user_query]
    return rewritten_list
