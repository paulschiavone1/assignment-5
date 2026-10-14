# inventory_spotcheck.py

import requests

student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

if seed % 3 == 0:
    threshold = 15
elif seed % 3 == 1:
    threshold = 12
else:
    threshold = 9

total_skus = 0
reorder_count = 0

while True:
    sku = input("SKU: ").strip()

    if sku.upper() == "DONE":
        break

    if sku == "":
        print("SKU cannot be blank.")
        continue

    while True:
        try:
            on_hand = int(input("On hand: "))
            if on_hand >= 0:
                break
            print("Quantity cannot be negative.")
        except ValueError:
            print("Enter a valid whole number.")

    total_skus = total_skus + 1

    if on_hand < threshold:
        print("REORDER")
        reorder_count = reorder_count + 1
    else:
        print("OK")

if seed % 2 == 0:
    term = "weezer"
else:
    term = "drake"

songs_returned = "N/A"
api_status = "FAILED"

try:
    response = requests.get(
        "https://itunes.apple.com/search",
        params={
            "entity": "song",
            "limit": 5,
            "term": term
        },
        timeout=10
    )
    response.raise_for_status()

except requests.RequestException:
    api_status = "FAILED"

else:
    try:
        data = response.json()

        if not isinstance(data, dict):
            raise ValueError

        results = data.get("results")

        if not isinstance(results, list):
            raise ValueError

        if not all(isinstance(item, dict) for item in results):
            raise ValueError

        songs_returned = sum(
            1 for item in results
            if item.get("kind") == "song"
        )

        api_status = "OK"

    except (ValueError, TypeError):
        api_status = "INVALID_RESPONSE"
        songs_returned = "N/A"

print("Seed:", seed)
print("Threshold:", threshold)
print("SKUs entered:", total_skus)
print("Reorder flagged:", reorder_count)
print("Spotcheck term:", term)
print("Songs returned:", songs_returned)
print("API status:", api_status)