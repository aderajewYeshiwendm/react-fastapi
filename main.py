import subprocess
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# fetch a website and save it as html
def fetch_website(url: str):
    subprocess.run(["wget", "-q", "-O", "site.html", url], check=True)

@app.get("/", response_class=HTMLResponse)
def get_website():
    fetch_website("https://convin.ai/blog/which-ai-technology-is-used-behind-the-personal-voice-assistant") 
    with open("site.html", "r", encoding="utf-8") as file:
        content = file.read()
    return HTMLResponse(content=content)
