import json

updates = [
  {
    "app_name": "Zendesk",
    "self_serve": True,
    "self_serve_evidence": "Zendesk offers a 14-day self-serve free trial and permanent Sponsored Developer Accounts for testing.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.zendesk.com/api-reference/introduction/security-and-auth/"
  },
  {
    "app_name": "Intercom",
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up for a free developer workspace to build and test private or public apps without a paid subscription.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/"
  },
  {
    "app_name": "Freshdesk",
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up for a free Freshdesk account (like the free Sprout plan) to get an API key.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.freshdesk.com/api/#authentication"
  },
  {
    "app_name": "Pylon",
    "self_serve": False,
    "self_serve_evidence": "Pylon does not offer a public self-serve sign up; access requires contacting sales and a paid plan.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "No self-serve sign-up; requires a sales conversation to get access.",
    "evidence_url": "https://usepylon.com/docs/api"
  },
  {
    "app_name": "Plain",
    "self_serve": True,
    "self_serve_evidence": "Developers can self-serve by creating a Machine User in their workspace settings to generate an API key.",
    "api_surface": "GraphQL",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://www.plain.com/docs/graphql-api/authentication"
  },
  {
    "app_name": "Help Scout",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate OAuth 2.0 App ID and Secret directly from the My Apps section in their Profile settings.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.helpscout.com/mailbox-api/overview/authentication/"
  },
  {
    "app_name": "Gorgias",
    "self_serve": True,
    "self_serve_evidence": "Users can generate a REST API key directly from the REST API section under their account settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.gorgias.com/reference/authentication"
  },
  {
    "app_name": "Slack",
    "self_serve": True,
    "self_serve_evidence": "Developers can create an app and generate tokens from the Slack API dashboard without admin approval for their own workspace.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://api.slack.com/authentication"
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
