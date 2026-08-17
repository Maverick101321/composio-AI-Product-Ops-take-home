import os
import json
from composio import Composio

# Normalize for robust matching
def normalize(s):
    return s.lower().replace(" ", "").replace("-", "").replace(".", "")

def main():
    with open("apps.json", "r") as f:
        apps = json.load(f)

    composio = Composio(api_key=os.environ["COMPOSIO_API_KEY"])
    
    # 2. Call composio.toolkits.list() with pagination to get FULL catalog
    print("Fetching Composio catalog...")
    all_items = []
    cursor = None
    while True:
        try:
            res = composio.toolkits.list(limit=1000, cursor=cursor)
        except Exception as e:
            print(f"Error fetching catalog: {e}")
            break
            
        items = res.items
        all_items.extend(items)
        if getattr(res, 'next_cursor', None):
            cursor = res.next_cursor
        else:
            break
            
    print(f"Total Composio toolkits fetched: {len(all_items)}")
    
    # Dump to JSON
    # res.items are Pydantic models or similar. Let's serialize.
    catalog_json = []
    for item in all_items:
        # Pydantic v1 or v2? Let's just try model_dump or dict
        if hasattr(item, 'model_dump'):
            catalog_json.append(item.model_dump())
        elif hasattr(item, 'dict'):
            catalog_json.append(item.dict())
        else:
            catalog_json.append(str(item))

    with open("composio_catalog.json", "w") as f:
        json.dump(catalog_json, f, indent=2)
    
    # 3. Build a dict of {slug: toolkit_data} and variations for matching
    catalog_map = {}
    for item in all_items:
        catalog_map[normalize(item.slug)] = item
        catalog_map[normalize(item.name)] = item

    # 4 & 5. Matches each of our 100 apps to a Composio slug
    found_apps = []
    not_found_apps = []

    print("\n--- MATCHING RESULTS ---")
    for app in apps:
        app_name = app["name"]
        norm_name = normalize(app_name)
        
        # Add special cases for known mis-matches if needed
        # but let's try direct first
        matched_item = None
        if norm_name in catalog_map:
            matched_item = catalog_map[norm_name]
        else:
            # Maybe prefix/suffix matching?
            # E.g. "Zoho CRM" -> "zohocrm"
            # "WhatsApp Business" -> "whatsapp"
            for k, v in catalog_map.items():
                if norm_name == k or norm_name in k or k in norm_name:
                    if len(k) > 4: # avoid too short random matches
                        matched_item = v
                        break
        
        if matched_item:
            auth = matched_item.auth_schemes if hasattr(matched_item, 'auth_schemes') else []
            meta = matched_item.meta
            tools_count = meta.tools_count if meta and hasattr(meta, 'tools_count') else 0
            cat_list = [c.name for c in meta.categories] if meta and hasattr(meta, 'categories') else []
            
            found_apps.append({
                "app": app,
                "composio_item": matched_item.name,
                "auth_schemes": auth,
                "tools_count": tools_count,
                "categories": cat_list
            })
        else:
            not_found_apps.append(app)

    print(f"\nFound {len(found_apps)} / {len(apps)} apps.")
    
    print("\n--- FOUND APPS (sample/details) ---")
    for fa in found_apps:
        # print(f"✅ {fa['app']['name']} -> {fa['composio_item']} | Auth: {fa['auth_schemes']} | Tools: {fa['tools_count']} | Categories: {fa['categories']}")
        pass # avoid too much output, we will print it below
        
    print(f"\n--- NOT FOUND APPS ({len(not_found_apps)}) ---")
    for nf in not_found_apps:
        print(f"❌ #{nf['number']} {nf['name']} ({nf['category']}) - {nf['website_hint']}")

    print(f"\nFinal Result: {len(found_apps)} found / {len(not_found_apps)} not found")

if __name__ == "__main__":
    main()
