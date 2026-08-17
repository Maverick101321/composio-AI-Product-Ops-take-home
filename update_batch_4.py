import json

updates = [
  {
    "app_name": "Klaviyo",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly create a free test account to experiment with custom apps and integrations without risking production data.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.klaviyo.com/en/docs/create_a_test_account"
  },
  {
    "app_name": "Pinterest",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly register apps and obtain API credentials through the Pinterest developer portal for standard access.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.pinterest.com/docs/getting-started/introduction/"
  },
  {
    "app_name": "SendGrid",
    "self_serve": True,
    "self_serve_evidence": "Users can sign up for a free SendGrid tier and instantly generate API keys from the settings dashboard after enabling 2FA.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.sendgrid.com/for-developers/sending-email/api-getting-started"
  },
  {
    "app_name": "Shopify",
    "self_serve": True,
    "self_serve_evidence": "Developers can join the Shopify Partner Program for free and instantly spin up development stores to build and test apps.",
    "api_surface": "GraphQL",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://shopify.dev/docs/apps/getting-started/create"
  },
  {
    "app_name": "Salesforce Commerce Cloud",
    "self_serve": False,
    "self_serve_evidence": "Access to Account Manager credentials and sandbox environments requires an enterprise contract or partner portal approval.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "Requires enterprise contract or partner approval for sandbox access.",
    "evidence_url": "https://developer.salesforce.com/docs/commerce/commerce-api/references/authorization"
  },
  {
    "app_name": "Squarespace",
    "self_serve": True,
    "self_serve_evidence": "Developers can request free developer trials, and merchants with Advanced Commerce plans can self-generate API keys in settings.",
    "api_surface": "REST - narrow",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.squarespace.com/commerce-api/getting-started"
  },
  {
    "app_name": "Gumroad",
    "self_serve": True,
    "self_serve_evidence": "Anyone can create a free Gumroad account and instantly generate a Personal Access Token in the advanced settings tab.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://app.gumroad.com/api"
  },
  {
    "app_name": "DataForSEO",
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up for a DataForSEO account and immediately obtain API credentials from the dashboard.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.dataforseo.com/v3/appendix/authentication/"
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
