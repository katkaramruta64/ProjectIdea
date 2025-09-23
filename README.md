# Project Idea Suggestion System

## About
This project suggests project ideas based on **research papers** fetched via backend API.  
Frontend is built with **HTML, CSS, and JavaScript**, while backend is powered by **FastAPI (Python)**.

## Features
- Search research papers by keyword  
- Display project ideas (title, abstract, and suggested idea)  
- Pagination (5 ideas per page with Next/Previous)  
- Save ideas to a separate tab  
- Remove saved ideas easily  

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: FastAPI (Python)  


## Setup & Run
### Backend
```bash
cd ProjectIdea
uvicorn main:app --reload
