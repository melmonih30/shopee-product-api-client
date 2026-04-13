import requests
import time

BASE_URL = "https://api.bodapi.com"
TOKEN = "YOUR_API_TOKEN"
SECRET = "YOUR_API_SECRET"

headers = {
    "X-API-Token": TOKEN,
    "X-API-Secret": SECRET
}

params = {
    "shop_id": "123456",
    "item_id": "987654",
    "country": "ph"
}

# Step 1: Submit task
submit_url = f"{BASE_URL}/sp/v1/submit/product_detail"
response = requests.get(submit_url, headers=headers, params=params).json()

batch_id = response["data"]["batch_id"]
print("Batch ID:", batch_id)

# Step 2: Poll for result
query_url = f"{BASE_URL}/sp/v1/query/product_detail"

while True:
    query_params = {"batch_id": batch_id}
    result = requests.get(query_url, headers=headers, params=query_params).json()

    code = result["code"]

    import json

if code == 0:
    print("✅ Data ready!")
    product_data = result["data"]["source"]

    # Save data to JSON file
    with open("product_data.json", "w", encoding="utf-8") as f:
        json.dump(product_data, f, indent=4)

    print("📁 Data saved to product_data.json")
    break

    elif code == -1:
        print("⏳ Still processing...")
        time.sleep(3)

    else:
        print("❌ Error:", result["msg"])
        break

  Add main script
