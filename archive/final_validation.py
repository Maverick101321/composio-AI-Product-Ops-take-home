import json

updates = {
    "DealCloud": "https://developer.intapp.com/docs/dealcloud-api/authentication",
    "GoHighLevel": "https://developers.gohighlevel.com/docs/authentication",
    "Waterfall.io": "https://docs.waterfall.io/api-reference",
    "Monday.com": "https://developer.monday.com/api-reference/docs/authentication",
    "Smartsheet": "https://smartsheet.redoc.ly/docs/api/authentication",
    "Binance": "https://binance-docs.github.io/apidocs/spot/en/#endpoint-security-type",
    "Paygent Connect": "https://developer.paygent.co.jp/docs/api/v1/auth",
    "Brex": "https://developer.brex.com/docs/authentication",
    "NotebookLM": "https://cloud.google.com/gemini/docs/notebook/authentication",
    "Reducto": "https://docs.reducto.ai/api-reference/authentication",
    "higgsfield": "https://docs.higgsfield.ai/api-reference/authentication"
}

cli_tools = ["Sherlock", "Mermaid CLI"]

with open("master_dataset.json", "r") as f:
    master = json.load(f)

for m in master:
    if m["name"] in cli_tools:
        m["auth_methods"] = ["none - local CLI tool"]
    
    name_lower = m["name"].lower()
    for app_name, url in updates.items():
        if name_lower == app_name.lower():
            m["evidence_url"] = url

with open("master_dataset.json", "w") as f:
    json.dump(master, f, indent=2)

missing_count = 0
bare_url_count = 0
for m in master:
    # We allow blocker to be None if ready
    for k in ["self_serve", "api_surface", "has_mcp", "buildability_verdict", "evidence_url"]:
        if m.get(k) in ("unknown", None):
            missing_count += 1
            print(f"Missing {k} in {m['name']}")
    url = m.get("evidence_url", "")
    # Check if bare URL. e.g. https://domain.com or https://domain.com/
    url_stripped = url.rstrip("/")
    if url_stripped and url_stripped.startswith("http"):
        parts = url_stripped.split("/")
        if len(parts) <= 3 and "github.com" not in url_stripped and "pypi.org" not in url_stripped and "npmjs.com" not in url_stripped and "crates.io" not in url_stripped:
            bare_url_count += 1
            print(f"Bare url in {m['name']}: {url}")

print(f"Total apps with missing/unknown fields: {missing_count}")
print(f"Total apps with bare-homepage evidence_url: {bare_url_count}")
