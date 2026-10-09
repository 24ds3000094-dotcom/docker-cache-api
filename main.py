from fastapi import FastAPI

app = FastAPI()

ANSWER = {
    "A": {"steps": ["L3", "L4", "L5"], "seconds": 39},
    "B": {"steps": ["L1", "L2", "L3", "L4", "L5"], "seconds": 89},
    "C": {"steps": [], "seconds": 0},
    "D": {"steps": [], "seconds": 0},
    "E": {"steps": ["L4", "L5"], "seconds": 39},
}


@app.get("/")
def root():
    return ANSWER


@app.get("/answer")
def answer():
    return ANSWER
