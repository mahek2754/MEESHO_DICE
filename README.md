# Meesho Co-Pilot (Prototype)

## Overview
AI-powered **semantic search** + **seller analytics bot** for Meesho.

## Features
- NLU service with intent + entity detection
- Semantic search over product catalog
- Mock conversational analytics for sellers

## Setup
```bash
pip install -r requirements.txt
uvicorn backend.nlu_service:app --reload
python search_demo/semantic_search.py
python analytics_demo/seller_bot.py
