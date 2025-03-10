from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data from a JSON file
with open("marks.json", "r") as file:
    student_marks = json.load(file)

@app.get("/api")
def get_marks(name: list[str]):
    """Return marks of given students in the same order"""
    marks = [student_marks.get(n, None) for n in name]
    return {"marks": marks}
