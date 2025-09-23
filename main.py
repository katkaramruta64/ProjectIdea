from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import xml.etree.ElementTree as ET
from idea_generator import generate_project_idea

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/get-papers")
def get_papers(query: str = "ai"):
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=50"
    response = requests.get(url)
    root = ET.fromstring(response.content)

    ns = {"atom": "http://www.w3.org/2005/Atom"}

    papers = []
    for entry in root.findall("atom:entry", ns):
        title = entry.find("atom:title", ns).text.strip()
        summary = entry.find("atom:summary", ns).text.strip()
        link = entry.find("atom:link", ns).attrib.get("href")

        project_idea = generate_project_idea(title, summary)  # <-- Generate idea here

        papers.append({
            "title": title,
            "summary": summary,
            "link": link,
            "suggested_idea": project_idea  # <-- Add idea to output
        })

    return {"papers": papers}