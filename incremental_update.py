import json
import sys
import os

def update_master(input_file):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    try:
        with open(input_file, "r") as f:
            new_data = json.load(f)
    except Exception as e:
        print(f"Failed to parse {input_file}: {e}")
        return

    try:
        with open("master_dataset.json", "r") as f:
            master = json.load(f)
    except Exception as e:
        print(f"Failed to read master_dataset.json: {e}")
        return

    updated_count = 0
    for item in new_data:
        app_name = item.get("app_name") or item.get("app")
        if not app_name:
            continue
        
        # Find corresponding app
        for m in master:
            if m["name"].lower() == app_name.lower():
                # Update fields if provided
                if "self_serve" in item: m["self_serve"] = item["self_serve"]
                if "self_serve_evidence" in item: m["self_serve_evidence"] = item["self_serve_evidence"]
                if "api_surface" in item: m["api_surface"] = item["api_surface"]
                if "has_mcp" in item: m["has_mcp"] = item["has_mcp"]
                if "buildability_verdict" in item: m["buildability_verdict"] = item["buildability_verdict"]
                if "blocker" in item: m["blocker"] = item["blocker"]
                
                # Check that evidence_url is not a bare homepage
                e_url = item.get("evidence_url", "")
                from urllib.parse import urlparse
                parsed = urlparse(e_url)
                if (parsed.path == "" or parsed.path == "/") and not parsed.query:
                    print(f"WARNING: {app_name} still has a bare homepage URL: {e_url}")
                    # we still update it, but warn
                
                m["evidence_url"] = e_url
                updated_count += 1
                break
                
    with open("master_dataset.json", "w") as f:
        json.dump(master, f, indent=2)
        
    print(f"Successfully updated {updated_count} apps in master_dataset.json.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python incremental_update.py <json_file>")
        sys.exit(1)
    update_master(sys.argv[1])
