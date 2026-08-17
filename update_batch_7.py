import json

updates = [
  {
    "app_name": "Jira",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate an API Token or Personal Access Token directly from their Atlassian account settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/"
  },
  {
    "app_name": "Asana",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate Personal Access Tokens directly from their Asana account's developer console.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.asana.com/docs/authentication"
  },
  {
    "app_name": "Monday.com",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate a Personal API Token directly from their Monday.com administration settings.",
    "api_surface": "GraphQL",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.monday.com/"
  },
  {
    "app_name": "ClickUp",
    "self_serve": True,
    "self_serve_evidence": "Developers can easily generate a Personal Token from their account settings for immediate API access.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://clickup.com/api/developer-portal/authentication/"
  },
  {
    "app_name": "Coda",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate a Personal API Token from their Coda account settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://coda.io/developers/apis/v1"
  },
  {
    "app_name": "Harvest",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate Personal Access Tokens directly from the Developers section of their Harvest ID.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/"
  },
  {
    "app_name": "Stripe",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate test and live API keys instantly from the Stripe Dashboard.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.stripe.com/keys"
  },
  {
    "app_name": "QuickBooks",
    "self_serve": True,
    "self_serve_evidence": "Developers can register on the Intuit Developer Portal and create an app to obtain OAuth credentials.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization"
  }
]

with open("master_dataset.json", "r") as f:
    master = json.load(f)

updated_apps = []
for item in updates:
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
