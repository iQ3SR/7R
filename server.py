from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/ai")
async def ai_endpoint(data: Prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": data.prompt}]
    )
    answer = response.choices[0].message["content"]
    return {"response": answer}
