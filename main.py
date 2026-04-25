from fastapi import FastAPI
import ollama
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")

@app.post("/generate")
async def generate(prompt: str):
    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return {"response": response.message.content}
    