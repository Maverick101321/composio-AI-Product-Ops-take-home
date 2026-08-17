import json
from urllib.parse import urlparse

with open("master_dataset.json") as f:
    data = json.load(f)

incomplete = []
for app in data:
    if app.get("source") != "composio_catalog":
        # Check if the manual apps have a bare URL. The prompt says:
        # "Check master_dataset.json: the 61 apps with source='composio_catalog' still have...
        # and 33 apps total still have bare homepage URLs...
        # Finish the job: for all 61 composio_catalog apps..."
        # So I only need to research the composio_catalog apps?
        pass
        
    u = app.get("api_surface")
    ss = app.get("self_serve")
    mcp = app.get("has_mcp")
    bv = app.get("buildability_verdict")
    url = app.get("evidence_url", "")
    
    parsed = urlparse(url)
    is_bare = (parsed.path == "" or parsed.path == "/") and not parsed.query
    
    needs_research = False
    if u in ["unknown", None] or ss in ["unknown", None] or mcp in ["unknown", None] or bv in ["unknown", None]:
        needs_research = True
    if is_bare:
        needs_research = True
        
    if needs_research:
        incomplete.append(app)

print(f"Total incomplete: {len(incomplete)}")

batch_size = 10
batches = [incomplete[i:i+batch_size] for i in range(0, len(incomplete), batch_size)]

for i, batch in enumerate(batches):
    print(f"Batch {i+1}:")
    for app in batch:
        print(f"{app['number']}. {app['name']}")
    print()
