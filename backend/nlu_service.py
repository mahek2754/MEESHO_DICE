from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import json

app = FastAPI()
model = SentenceTransformer('all-MiniLM-L6-v2')

class QueryInput(BaseModel):
    text: str

@app.post("/nlu/parse")
def parse(input: QueryInput):
    text = input.text.lower()
    intent = "product_search" if "buy" in text or "saree" in text else "sales_trend_query"
    entities = []
    if "saree" in text:
        entities.append({"type": "product", "value": "saree"})
    vector = model.encode(text).tolist()
    return {"intent": intent, "entities": entities, "vector": vector}
