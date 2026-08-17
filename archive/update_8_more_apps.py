import json

updates = [
  {
    "app_name": "Discord",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly create a new bot application and generate tokens via the Discord Developer Portal.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://discord.com/developers/docs/topics/oauth2"
  },
  {
    "app_name": "Telegram",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly create bots and get access tokens by chatting with BotFather on Telegram.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://core.telegram.org/bots/api#authorizing-your-bot"
  },
  {
    "app_name": "WhatsApp Business",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly generate temporary access tokens in the Meta for Developers App Dashboard.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.facebook.com/docs/whatsapp/cloud-api/get-started"
  },
  {
    "app_name": "Google Ads",
    "self_serve": False,
    "self_serve_evidence": "API access requires applying for a developer token which must be manually reviewed and approved by Google.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "blocked",
    "blocker": "Requires manual review and approval of the developer token by Google.",
    "evidence_url": "https://developers.google.com/google-ads/api/docs/oauth/overview"
  },
  {
    "app_name": "Meta Ads",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate System User Access Tokens from the Business Manager settings for server-to-server interactions.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.facebook.com/docs/marketing-api/authentication"
  },
  {
    "app_name": "LinkedIn Ads",
    "self_serve": False,
    "self_serve_evidence": "API access requires submitting an application for the LinkedIn Marketing Developer Platform which must be approved by LinkedIn.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "blocked",
    "blocker": "Requires approval for the LinkedIn Marketing Developer Program.",
    "evidence_url": "https://learn.microsoft.com/en-us/linkedin/marketing/"
  },
  {
    "app_name": "GoHighLevel",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate Private Integration Tokens directly inside a GoHighLevel Sub-Account or Agency settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://marketplace.gohighlevel.com/"
  },
  {
    "app_name": "Mailchimp",
    "self_serve": True,
    "self_serve_evidence": "You can generate an API key instantly from your Mailchimp account dashboard for private scripts.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://mailchimp.com/developer/marketing/docs/fundamentals/"
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
