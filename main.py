# Shopee Product Data API Client
# This script:
# 1. Sends a request to the API
# 2. Retrieves product data asynchronously
# 3. Polls until data is ready
# 4. Saves the result into a JSON file

import requests
import time
import json

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
try:
    response = requests.get(submit_url, headers=headers, params=params)
    response.raise_for_status()
    response = response.json()
except Exception as e:
    print(f"[ERROR] Failed to submit request: {e}")
    exit()

batch_id = response["data"]["batch_id"]
print(f"[INFO] Batch ID received: {batch_id}")

# Step 2: Poll for result
query_url = f"{BASE_URL}/sp/v1/query/product_detail"

while True:
    query_params = {"batch_id": batch_id}
    result = requests.get(query_url, headers=headers, params=query_params).json()

    code = result["code"]

if code == 0:
print("[SUCCESS] Data retrieved successfully")
    product_data = result["data"]["source"]

    # Save data to JSON file
    with open("shopee_product_data.json", "w", encoding="utf-8") as f:
        json.dump(product_data, f, indent=4)

print("📁 Data saved to shopee_product_data.json")
    break

    elif code == -1:
       print("[INFO] Waiting for API to finish processing...")
        time.sleep(3)

    else:
        print(f"[ERROR] {result.get('msg', 'Unknown error')}")
        break

  Add main script
