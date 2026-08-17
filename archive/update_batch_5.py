import json

updates = [
  {
    "app_name": "Ahrefs",
    "self_serve": False,
    "self_serve_evidence": "API access requires an Enterprise plan and must be managed by a workspace owner or administrator.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "Requires an Enterprise plan for API access.",
    "evidence_url": "https://docs.ahrefs.com/en/api/docs/introduction"
  },
  {
    "app_name": "MrScraper",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly generate an API token from their MrScraper account dashboard.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://mrscraper.com/docs/api"
  },
  {
    "app_name": "Apify",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate secret API tokens instantly from the Apify Console under Settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.apify.com/api/v2"
  },
  {
    "app_name": "Firecrawl",
    "self_serve": True,
    "self_serve_evidence": "Developers can obtain a standard API key directly from their Firecrawl account dashboard.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.firecrawl.dev/api-reference"
  },
  {
    "app_name": "Bright Data",
    "self_serve": True,
    "self_serve_evidence": "Developers can log in to the Bright Data Dashboard and instantly generate an API Token.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.brightdata.com/api-reference/"
  },
  {
    "app_name": "GitHub",
    "self_serve": True,
    "self_serve_evidence": "Developers can easily generate Personal Access Tokens (PATs) or register GitHub Apps instantly via their account settings.",
    "api_surface": "REST - broad, GraphQL",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.github.com/en/rest/authentication/about-authentication"
  },
  {
    "app_name": "Vercel",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly create a Vercel Access Token from their personal account settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://vercel.com/docs/rest-api"
  },
  {
    "app_name": "Cloudflare",
    "self_serve": True,
    "self_serve_evidence": "Developers can create scoped API tokens instantly from their Cloudflare dashboard profile.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.cloudflare.com/fundamentals/api/get-started/create-token/"
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
