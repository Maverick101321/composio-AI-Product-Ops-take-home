import json
with open("master_dataset.json", "r") as f:
    master = json.load(f)

blocked = [m for m in master if m.get("buildability_verdict") == "blocked"]
print(f"Total blocked: {len(blocked)}")
for b in blocked:
    print(f"- {b['name']}: {b['blocker']}")
