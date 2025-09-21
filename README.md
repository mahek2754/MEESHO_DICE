# Meesho Saathi: AI-Driven Discovery & Seller Intelligence

## Overview
Meesho Saathi solves two critical problems:

1. **Customer Discovery Gap** – Existing keyword search fails on nuanced, multi-attribute queries.
2. **Seller Data Gap** – SMB sellers lack real-time, actionable insights for pricing and inventory.

Our solution combines **semantic search** + **conversational analytics** to boost conversions, retention, and seller success.

---

## Architecture

**Flow Summary**
- **NLU Service** – Intent + entity detection, query embeddings  
- **Customer Search Service** – Hybrid semantic + keyword retrieval, reranking  
- **Seller Analytics Service** – Conversational interface for real-time insights  

Datastores: **PostgreSQL (metadata)**, **Milvus (vectors)**, **ClickHouse (analytics)**  

---

## Features
- **NLU Service**: Intent + entity extraction, semantic embeddings  
- **Semantic Search**: Find top products by meaning, not just keywords  
- **Seller Bot**: Chat-style analytics (sales, demand forecasts)  
- **Lightweight & Demo-Ready**: Run locally with minimal setup  

---

## Repository Structure
```
meesho-copilot/
 ├── backend/
 │    └── nlu_service.py      # FastAPI NLU service
 ├── search_demo/
 │    └── semantic_search.py  # Semantic product search
 ├── analytics_demo/
 │    └── seller_bot.py       # Seller analytics chatbot
 ├── tests/
 │    └── test_end_to_end.py  # Minimal flow tests
 ├── requirements.txt
 ├── README.md
 └── docs/
      └── architecture.png    # System diagram
```

---

## Quick Start

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Start the NLU Service
```bash
uvicorn backend.nlu_service:app --reload
```

### 3️⃣ Run Demos
```bash
python search_demo/semantic_search.py
python analytics_demo/seller_bot.py
```

### 4️⃣ Run Tests
```bash
python tests/test_end_to_end.py
```

---

## Example Output

**Customer Search**
```json
[
  {"id": "P123", "title": "Red Silk Saree", "price": 1799, "score": 0.91},
  {"id": "P456", "title": "Cotton Embroidered Saree", "price": 1999, "score": 0.87}
]
```

**Seller Bot**
```json
{
  "textResponse": "You sold 1,245 kurtas in August (+12% from July)",
  "chartData": {
    "labels": ["01-08", "05-08", "10-08"],
    "values": [40, 65, 72]
  }
}
```

---

## Impact
- Higher conversion rates with intent-driven search  
- Data-empowered sellers → less stock-outs, more profits  
- Strengthened Meesho growth flywheel  

---

## Future Scope
- Personalized recommendations  
- Multi-turn conversational refinement  
- Forecasting models using real data  

