import numpy as np
from sentence_transformers import SentenceTransformer, util
import pandas as pd

model = SentenceTransformer('all-MiniLM-L6-v2')
products = pd.DataFrame([
    {"id": "P123", "title": "Red Silk Saree", "price": 1799},
    {"id": "P456", "title": "Embroidered Cotton Saree", "price": 1999}
])

def search_products(query):
    q_vec = model.encode(query, convert_to_tensor=True)
    p_vecs = model.encode(products['title'].tolist(), convert_to_tensor=True)
    scores = util.pytorch_cos_sim(q_vec, p_vecs)[0].cpu().numpy()
    products['score'] = scores
    results = products.sort_values(by='score', ascending=False)
    return results.head(3).to_dict(orient="records")

if __name__ == "__main__":
    print(search_products("saree for wedding under 2000"))
