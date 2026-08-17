import json

data_c4 = [
  {
    "app_name": "MrScraper",
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up and get an API token directly from the platform without sales approval.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://mrscraper.com"
  },
  {
    "app_name": "Apify",
    "self_serve": True,
    "self_serve_evidence": "API tokens can be generated from the API & Integrations section of the Apify Console for free.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.apify.com/api/v2"
  },
  {
    "app_name": "Firecrawl",
    "self_serve": True,
    "self_serve_evidence": "A free tier is available, and developers can manage API keys directly via the Firecrawl dashboard.",
    "api_surface": "REST - narrow",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.firecrawl.dev"
  },
  {
    "app_name": "Bright Data",
    "self_serve": True,
    "self_serve_evidence": "Users can independently create an account and generate API keys for proxy and scraping services.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://brightdata.com/support/docs"
  },
  {
    "app_name": "GitHub",
    "self_serve": True,
    "self_serve_evidence": "Developers can easily create Personal Access Tokens (PATs) for free from their account settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.github.com/rest"
  },
  {
    "app_name": "Vercel",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate a Bearer Token from Vercel Account Settings for free.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://vercel.com/docs/rest-api"
  },
  {
    "app_name": "Cloudflare",
    "self_serve": True,
    "self_serve_evidence": "API tokens can be freely created from the Cloudflare Developer dashboard.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.cloudflare.com/api/"
  },
  {
    "app_name": "Supabase",
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up for free and get auto-generated REST APIs and management API keys immediately.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://supabase.com/docs/guides/api"
  },
  {
    "app_name": "Neo4j",
    "self_serve": True,
    "self_serve_evidence": "Developers can start for free with Neo4j Aura or Sandbox and get connection credentials immediately.",
    "api_surface": "REST - narrow",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://neo4j.com/docs/"
  },
  {
    "app_name": "Snowflake",
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up for a 30-day free trial to self-serve an account and access the REST APIs.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.snowflake.com/en/developer-guide/rest-api/index"
  }
]

data_c2 = [
  {
    "app_name": "Help Scout",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate OAuth credentials directly inside their Help Scout account under My Apps without external approval.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.helpscout.com/mailbox-api/overview/authentication/"
  },
  {
    "app_name": "Gorgias",
    "self_serve": True,
    "self_serve_evidence": "Admins can generate a personal API Key directly from their Gorgias account settings for Basic Authentication.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.gorgias.com/reference/authentication"
  },
  {
    "app_name": "Slack",
    "self_serve": True,
    "self_serve_evidence": "Developers can freely create an app and install it in their workspace to instantly receive Bot and User OAuth tokens.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://api.slack.com/authentication/token-types"
  },
  {
    "app_name": "Discord",
    "self_serve": True,
    "self_serve_evidence": "Developers can create a bot application in the Discord Developer Portal to instantly get a Bot Token.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://discord.com/developers/docs/topics/oauth2"
  },
  {
    "app_name": "Telegram",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly generate a bot token by messaging BotFather on the Telegram app.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://core.telegram.org/bots/api"
  },
  {
    "app_name": "WhatsApp Business",
    "self_serve": True,
    "self_serve_evidence": "Meta provides Embedded Signup allowing businesses to get credentials and onboard directly from the App Dashboard without manual review.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.facebook.com/docs/whatsapp/embedded-signup"
  },
  {
    "app_name": "Google Ads",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly get Test access with a Developer Token from their Google Ads Manager account and OAuth credentials from Google Cloud.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.google.com/google-ads/api/docs/oauth/cloud-project"
  },
  {
    "app_name": "Meta Ads",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly create a Meta App and generate User or System User Tokens via the Graph API Explorer.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.facebook.com/docs/marketing-apis"
  },
  {
    "app_name": "LinkedIn Ads",
    "self_serve": False,
    "self_serve_evidence": "The Advertising API requires explicit vetting and approval from LinkedIn through the Marketing Developer Program.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "requires partner approval",
    "evidence_url": "https://learn.microsoft.com/en-us/linkedin/marketing/"
  },
  {
    "app_name": "GoHighLevel",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly create an app in the Developer Marketplace to get OAuth credentials or use Private Integration Tokens.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://marketplace.gohighlevel.com/docs/"
  }
]

with open("master_dataset.json", "r") as f:
    master = json.load(f)

for item in data_c4 + data_c2:
    app_name = item.get("app_name") or item.get("app")
    if not app_name:
        continue
    # Find the corresponding app in master
    for m in master:
        if m["name"].lower() == app_name.lower():
            m["self_serve"] = item["self_serve"]
            m["self_serve_evidence"] = item["self_serve_evidence"]
            m["api_surface"] = item["api_surface"]
            m["has_mcp"] = item["has_mcp"]
            m["buildability_verdict"] = item["buildability_verdict"]
            m["blocker"] = item["blocker"]
            m["evidence_url"] = item["evidence_url"]
            break

with open("master_dataset.json", "w") as f:
    json.dump(master, f, indent=2)

print("Updated master_dataset.json with C2 and C4 results.")
