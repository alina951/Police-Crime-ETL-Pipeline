import json
import os
from src.mongodb import collection

def export_json():

    os.makedirs("exports", exist_ok=True)

    data = list(collection.find({}, {"_id": 0}))

    with open("exports/police_crimes.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Exported {len(data)} records to exports/police_crimes.json")