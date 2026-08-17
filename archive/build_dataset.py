import json
import os

def normalize(s):
    return s.lower().replace(" ", "").replace("-", "").replace(".", "")

def main():
    with open("apps.json", "r") as f:
        apps = json.load(f)
        
    with open("composio_catalog.json", "r") as f:
        catalog = json.load(f)

    catalog_map = {}
    for item in catalog:
        slug = item.get("slug", "")
        name = item.get("name", "")
        if slug:
            catalog_map[normalize(slug)] = item
        if name:
            catalog_map[normalize(name)] = item
            
    master_dataset = []
    
    auth_populated_count = 0
    needs_one_liner_count = 0
    needs_api_surface_count = 0

    for app in apps:
        app_name = app["name"]
        norm_name = normalize(app_name)
        website = app.get("website_hint", "")
        
        matched_item = None
        if norm_name in catalog_map:
            matched_item = catalog_map[norm_name]
        else:
            for k, v in catalog_map.items():
                if norm_name == k or norm_name in k or k in norm_name:
                    if len(k) > 4:
                        matched_item = v
                        break
                        
        if matched_item:
            meta = matched_item.get("meta", {})
            auth_methods = matched_item.get("auth_schemes", [])
            one_liner = meta.get("description", None)
            evidence_url = meta.get("app_url", website)
            
            entry = {
                "number": app["number"],
                "name": app_name,
                "category": app["category"],
                "website": website,
                "one_liner": one_liner,
                "auth_methods": auth_methods,
                "self_serve": "unknown",
                "self_serve_evidence": None,
                "api_surface": "unknown",
                "has_mcp": "unknown",
                "buildability_verdict": "unknown",
                "blocker": None,
                "evidence_url": evidence_url,
                "source": "composio_catalog",
                "composio_toolkit_slug": matched_item.get("slug", None)
            }
        else:
            entry = {
                "number": app["number"],
                "name": app_name,
                "category": app["category"],
                "website": website,
                "one_liner": None,
                "auth_methods": [],
                "self_serve": "unknown",
                "self_serve_evidence": None,
                "api_surface": "unknown",
                "has_mcp": "unknown",
                "buildability_verdict": "unknown",
                "blocker": None,
                "evidence_url": None,
                "source": "manual_research",
                "composio_toolkit_slug": None
            }
            
        master_dataset.append(entry)
        
        if entry["auth_methods"]:
            auth_populated_count += 1
        if not entry["one_liner"]:
            needs_one_liner_count += 1
        if entry["api_surface"] == "unknown":
            needs_api_surface_count += 1

    with open("master_dataset.json", "w") as f:
        json.dump(master_dataset, f, indent=2)

    print(f"Saved master_dataset.json with {len(master_dataset)} apps.")
    print(f"Apps with auth_methods populated: {auth_populated_count}")
    print(f"Apps needing one_liner research: {needs_one_liner_count}")
    print(f"Apps needing api_surface research: {needs_api_surface_count}")

if __name__ == "__main__":
    main()
