import requests
import feedparser

# Example query
url = "http://export.arxiv.org/api/query?search_query=all:machine+learning&start=0&max_results=10"

response = requests.get(url)
feed = feedparser.parse(response.text)

for entry in feed.entries:
    print("Title:", entry.title)
    print("Authors:", [author.name for author in entry.authors])
    print("Published:", entry.published)
    print("Link:", entry.link)
    print("-" * 50)

def generate_project_idea(summary):
    if "CNN" in summary and "image" in summary:
        return "Build an image classification system using CNN"
    elif "time series" in summary:
        return "Create a time series forecasting model"
    elif "classification" in summary:
        return "Design a supervised classification project"
    else:
        return "Explore this topic and implement a prototype based on research"
