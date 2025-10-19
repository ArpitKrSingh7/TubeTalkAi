from openai import OpenAI
from config import GOOGLE_API_KEY, GOOGLE_API_URL
from prompts import CHAT_SYSTEM_PROMPT

client = OpenAI(api_key=GOOGLE_API_KEY, base_url=GOOGLE_API_URL)

def build_system_prompt(context, relationships):
    return CHAT_SYSTEM_PROMPT.format(context=context, relationships=relationships)

def ask_gemini(system_message, user_query):
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_query},
        ],
    )
    return response.choices[0].message.content
