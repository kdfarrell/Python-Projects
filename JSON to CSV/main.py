import csv
import json
from pathlib import Path

parent_folder = Path(__file__).parent
json_file = parent_folder / "input.json"
csv_file = parent_folder / "output.csv"

try:
    with open(json_file, "r") as f:
        data = json.load(f)

    if not data:
        raise ValueError("JSON file is empty.")
    
    headers = list(data[0].keys())

    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

        for entry in data:
            row = {key: entry.get(key, "") for key in headers}
            writer.writerow(row)

    print(f"Success! CSV file created at: {csv_file}")

except FileNotFoundError:
    print(f"Error: JSON file not found at {json_file}")
except Exception as ex:
    print(f"An error occurred: {ex}")