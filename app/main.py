from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import graph

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
def ask(req: QueryRequest):
    result = graph.invoke({
        "query": req.query
    })

    return {
        "answer": result.get("answer"),
        "raw": result   # useful for debugging
    }