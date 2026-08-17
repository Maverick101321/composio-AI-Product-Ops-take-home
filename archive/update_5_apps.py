import json

data_updates = [
  {
    "app_name": "Salesforce",
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up for a permanently free Salesforce Developer Edition org to build and test API integrations.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_authorization.htm"
  },
  {
    "app_name": "HubSpot",
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up for a free developer account and create test accounts to generate access tokens and OAuth credentials.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.hubspot.com/docs/guides/apps/authentication/authentication-overview"
  },
  {
    "app_name": "Pipedrive",
    "self_serve": True,
    "self_serve_evidence": "Users can generate a Personal API Token from their settings or register an app in the Developer Hub for OAuth 2.0 without prior approval.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://pipedrive.readme.io/docs/core-api-concepts-authentication"
  },
  {
    "app_name": "Attio",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate an API key directly from their Workspace settings under Developers > Create a new integration.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.attio.com/docs/authentication"
  },
  {
    "app_name": "Close",
    "self_serve": True,
    "self_serve_evidence": "Users can generate an API key in their Close account under Settings > Developer > API Keys.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.close.com/basics/authentication/"
  }
]

with open("master_dataset.json", "r") as f:
    master = json.load(f)

updated_apps = []
for item in data_updates:
    for m in master:
        if m["name"].lower() == item["app_name"].lower():
            m["self_serve"] = item["self_serve"]
            m["self_serve_evidence"] = item["self_serve_evidence"]
            m["api_surface"] = item["api_surface"]
            m["has_mcp"] = item["has_mcp"]
            m["buildability_verdict"] = item["buildability_verdict"]
            m["blocker"] = item["blocker"]
            m["evidence_url"] = item["evidence_url"]
            updated_apps.append(m)
            break

with open("master_dataset.json", "w") as f:
    json.dump(master, f, indent=2)

print(json.dumps(updated_apps, indent=2))
