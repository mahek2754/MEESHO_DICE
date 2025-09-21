from search_demo.semantic_search import search_products
from analytics_demo.seller_bot import seller_query

def test_search():
    results = search_products("red saree")
    assert len(results) > 0

def test_seller():
    resp = seller_query("kurta sales last month")
    assert "textResponse" in resp

if __name__ == "__main__":
    test_search()
    test_seller()
    print("All tests passed ✅")
