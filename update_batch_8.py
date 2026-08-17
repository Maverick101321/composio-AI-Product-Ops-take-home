import json

updates = [
  {
    "app_name": "Xero",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly generate client credentials by registering an app in the Xero Developer portal.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.xero.com/documentation/oauth2/overview"
  },
  {
    "app_name": "Brex",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate an API token directly from the Developer section of their Brex Dashboard.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.brex.com"
  },
  {
    "app_name": "Ramp",
    "self_serve": True,
    "self_serve_evidence": "Admins can create a developer app in the Ramp dashboard to obtain credentials for API access.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.ramp.com/developer/v1/token"
  },
  {
    "app_name": "NotebookLM",
    "self_serve": False,
    "self_serve_evidence": "Google offers no public, self-serve developer API key for the consumer version; programmatic access requires session cookie workarounds or enterprise setup.",
    "api_surface": "no public API",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "No official public API exists for consumer accounts; requires session cookie extraction.",
    "evidence_url": "https://notebooklm.google.com"
  },
  {
    "app_name": "Fathom",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate API tokens directly from the Settings \u2192 API section of their Fathom Analytics dashboard.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://usefathom.com/api"
  },
  {
    "app_name": "Consensus",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate API credentials directly from the Integrations section of the Consensus Webapp.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.consensus.app/llms.txt"
  },
  {
    "app_name": "Devin",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate a Personal Access Token or Service User API Key directly from their Devin account.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.devin.ai/api-reference"
  },
  {
    "app_name": "YouTube Transcript",
    "self_serve": True,
    "self_serve_evidence": "The unofficial Python library does not require authentication for public videos.",
    "api_surface": "SDK only",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://pypi.org/project/youtube-transcript-api/"
  }
]

with open("master_dataset.json", "r") as f:
    master = json.load(f)

updated_apps = []
for item in updates:
    for m in master:
        if m["name"].lower() == item["app_name"].lower() or (item["app_name"].lower() == "fathom" and "fathom" in m["name"].lower()):
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

print("--- Updated Apps ---")
print(json.dumps(updated_apps, indent=2))

# Validate if there are any remaining unknown self_serve
unknown_count = sum(1 for m in master if m.get("self_serve") in ("unknown", None) or m.get("self_serve") is None)
print(f"\nTotal apps with self_serve = unknown or null: {unknown_count}")
