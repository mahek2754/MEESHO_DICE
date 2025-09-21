import json

def seller_query(message):
    if "sales" in message:
        return {
            "textResponse": "You sold 1,245 kurtas in August, +12% from July",
            "chartData": {"labels": ["01-08","05-08","10-08"], "values": [40, 65, 72]}
        }
    return {"textResponse": "Sorry, I cannot process this request yet."}

if __name__ == "__main__":
    print(json.dumps(seller_query("kurta sales last month"), indent=2))
