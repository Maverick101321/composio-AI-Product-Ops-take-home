import os
import json
import argparse
import subprocess
from urllib.parse import urlparse
from composio import Composio

def normalize(s):
    """Normalize strings for robust matching."""
    return s.lower().replace(" ", "").replace("-", "").replace(".", "")


def fetch_composio_catalog(api_key, apps_file_path="apps.json"):
    """
    Fetches the Composio catalog and matches it against our list of apps.
    Extracts basic auth and URL hints.
    """
    with open(apps_file_path, "r") as f:
        apps = json.load(f)

    composio = Composio(api_key=api_key)
    
    print("Fetching Composio catalog...")
    all_items = []
    cursor = None
    while True:
        try:
            res = composio.toolkits.list(limit=1000, cursor=cursor)
            items = res.items
            all_items.extend(items)
            if getattr(res, 'next_cursor', None):
                cursor = res.next_cursor
            else:
                break
        except Exception as e:
            print(f"Error fetching catalog: {e}")
            break
            
    print(f"Total Composio toolkits fetched: {len(all_items)}")
    
    catalog_map = {}
    for item in all_items:
        catalog_map[normalize(item.slug)] = item
        catalog_map[normalize(item.name)] = item

    master_dataset = []
    
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
            meta = matched_item.meta if hasattr(matched_item, 'meta') else {}
            # Handle Pydantic objects or dicts safely
            meta_dict = meta.model_dump() if hasattr(meta, 'model_dump') else (meta.dict() if hasattr(meta, 'dict') else meta)
            auth_methods = matched_item.auth_schemes if hasattr(matched_item, 'auth_schemes') else []
            one_liner = meta_dict.get("description", None) if isinstance(meta_dict, dict) else None
            evidence_url = meta_dict.get("app_url", website) if isinstance(meta_dict, dict) else website
            
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
                "composio_toolkit_slug": matched_item.slug
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
        
    return master_dataset


def research_app(app_name, hint_url):
    """
    Uses the Gemini CLI (agy) to research an app's developer docs.
    """
    print(f"Researching {app_name} (Hint: {hint_url})...")
    
    prompt = (
        f"Research the {app_name} developer docs (starting at {hint_url}). "
        f"Return ONLY a JSON object matching this schema exactly: "
        f"self_serve (bool), self_serve_evidence (str), api_surface (str), "
        f"has_mcp (bool), mcp_note (str or null), buildability_verdict (must be exactly 'ready', 'blocked', or 'partial'), "
        f"blocker (str or null), evidence_url (str). "
        f"When checking has_mcp, search for both official and community/third-party MCP servers. "
        f"If any exist, has_mcp is true, and detail it in mcp_note."
    )
    
    cmd = ["agy", "--print", prompt, "--output-format", "json"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            raise RuntimeError(f"agy exited with {result.returncode}. Stderr: {result.stderr}")
            
        # agy outputs an envelope with 'response'. The response might have markdown code blocks.
        envelope = json.loads(result.stdout)
        response_text = envelope.get("response", "")
        # Clean markdown if present
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.endswith("```\n"):
            response_text = response_text[:-4]
        elif response_text.endswith("```"):
            response_text = response_text[:-3]
        
        return json.loads(response_text.strip())
    except Exception as e:
        print(f"Error researching {app_name}: {e}")
        try:
            with open("failures.json", "a") as f:
                failure_entry = {"app_name": app_name, "error": str(e), "stdout": result.stdout if 'result' in locals() else "", "stderr": result.stderr if 'result' in locals() else ""}
                f.write(json.dumps(failure_entry) + "\n")
        except:
            pass
        return None


def run_batch(master_dataset, app_list_to_research):
    """
    Calls research_app() over a list, saving incrementally to master_dataset.json.
    """
    updated_apps = []
    for app_name in app_list_to_research:
        for m in master_dataset:
            if m["name"].lower() == app_name.lower():
                # Perform the research
                research_result = research_app(app_name, m.get("website", ""))
                
                # Apply the research results
                m["self_serve"] = research_result.get("self_serve")
                m["self_serve_evidence"] = research_result.get("self_serve_evidence")
                m["api_surface"] = research_result.get("api_surface")
                m["has_mcp"] = research_result.get("has_mcp")
                m["buildability_verdict"] = research_result.get("buildability_verdict")
                m["blocker"] = research_result.get("blocker")
                m["evidence_url"] = research_result.get("evidence_url")
                
                updated_apps.append(m)
                
                # Save incrementally
                with open("master_dataset.json", "w") as f:
                    json.dump(master_dataset, f, indent=2)
                break
                
    return updated_apps


def validate(master_dataset):
    """
    Validates the dataset for missing fields and bare-homepage URLs.
    """
    missing_count = 0
    bare_url_count = 0
    
    for m in master_dataset:
        for k in ["self_serve", "api_surface", "has_mcp", "buildability_verdict", "evidence_url"]:
            if m.get(k) in ("unknown", None):
                missing_count += 1
                print(f"Missing {k} in {m['name']}")
                
        url = m.get("evidence_url", "")
        url_stripped = url.rstrip("/")
        if url_stripped and url_stripped.startswith("http"):
            parts = url_stripped.split("/")
            if len(parts) <= 3 and "github.com" not in url_stripped and "pypi.org" not in url_stripped and "npmjs.com" not in url_stripped and "crates.io" not in url_stripped:
                bare_url_count += 1
                print(f"Bare url in {m['name']}: {url}")

    print(f"Total apps with missing/unknown fields: {missing_count}")
    print(f"Total apps with bare-homepage evidence_url: {bare_url_count}")
    return missing_count == 0 and bare_url_count == 0


def apply_manual_corrections(master_dataset, corrections_list):
    """
    Applies manual verification corrections to the dataset and logs them.
    corrections_list format:
    [
        {"app_name": "Mailchimp", "updates": {"mcp_note": "Community..."}, "source_url": "https://...", "field_name": "mcp_note"}, ...
    ]
    """
    log_entries = []
    
    for correction in corrections_list:
        app_name = correction["app_name"]
        for m in master_dataset:
            if m["name"] == app_name:
                before = {}
                after = {}
                for k, v in correction["updates"].items():
                    before[k] = m.get(k)
                    m[k] = v
                    after[k] = v
                
                log_entries.append({
                    "app": app_name,
                    "field": correction["field_name"],
                    "before": before,
                    "after": after,
                    "source_url": correction.get("source_url", m.get("evidence_url"))
                })
                break
                
    # Save the updated master dataset
    with open("master_dataset.json", "w") as f:
        json.dump(master_dataset, f, indent=2)
        
    return log_entries

def main():
    parser = argparse.ArgumentParser(description="Composio App Research Pipeline")
    parser.add_argument("--research", type=str, help="Research a single app by name and print the result")
    parser.add_argument("--validate", action="store_true", help="Run the final validation on master_dataset.json")
    args = parser.parse_args()

    # Always need the master dataset for lookup/validation
    try:
        with open("master_dataset.json", "r") as f:
            master_dataset = json.load(f)
    except FileNotFoundError:
        print("Error: master_dataset.json not found.")
        return

    if args.validate:
        print("Validating master dataset...")
        validate(master_dataset)
    elif args.research:
        app_name = args.research
        # Find the website hint
        app = next((m for m in master_dataset if m["name"].lower() == app_name.lower()), None)
        if not app:
            print(f"App '{app_name}' not found in master_dataset.json")
            return
        
        result = research_app(app_name, app.get("website", ""))
        if result:
            print(f"\n--- Result for {app_name} ---")
            print(json.dumps(result, indent=2))
        else:
            print(f"Research failed for {app_name}. See failures.json.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
