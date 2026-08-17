import json

data_c6 = [
  {
    "app_name": "Harvest",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly generate a personal access token directly from Settings > Developers.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://help.getharvest.com/api-v2/"
  },
  {
    "app_name": "Stripe",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly get test API credentials from the Stripe Dashboard upon signing up for free.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://stripe.com/docs/api"
  },
  {
    "app_name": "QuickBooks",
    "self_serve": True,
    "self_serve_evidence": "The Intuit Developer Portal provides a free sandbox testing environment and credentials upon registration.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.intuit.com/app/developer/qbo/docs/api-reference"
  },
  {
    "app_name": "Xero",
    "self_serve": True,
    "self_serve_evidence": "Developers can freely sign up on the Xero Developer portal to create apps and get OAuth credentials.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.xero.com/documentation/getting-started/getting-started-guide"
  },
  {
    "app_name": "Brex",
    "self_serve": False,
    "self_serve_evidence": "Brex does not offer a public sandbox; API access requires an active, approved corporate Brex account.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "Requires active Brex customer account",
    "evidence_url": "https://developer.brex.com/"
  },
  {
    "app_name": "Ramp",
    "self_serve": False,
    "self_serve_evidence": "Sandbox access must be requested through account management and requires an active customer account.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "Requires active Ramp customer account",
    "evidence_url": "https://docs.ramp.com/"
  },
  {
    "app_name": "NotebookLM",
    "self_serve": False,
    "self_serve_evidence": "Google does not provide any official public API or developer sandbox for consumer NotebookLM.",
    "api_surface": "no public API",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "No official public API exists",
    "evidence_url": "https://notebooklm.google.com/"
  },
  {
    "app_name": "Fathom",
    "self_serve": False,
    "self_serve_evidence": "API access requires a paid Team Edition plan or higher to generate keys.",
    "api_surface": "REST - narrow",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "paid plan required",
    "evidence_url": "https://developers.fathom.ai/"
  },
  {
    "app_name": "Consensus",
    "self_serve": False,
    "self_serve_evidence": "The Consensus API is restricted and developer access is available only by application.",
    "api_surface": "REST - narrow",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "requires partner approval",
    "evidence_url": "https://consensus.app/"
  },
  {
    "app_name": "Devin",
    "self_serve": False,
    "self_serve_evidence": "API access requires an enterprise account and reaching out to support for enablement.",
    "api_surface": "REST - narrow",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "Requires enterprise account and support enablement",
    "evidence_url": "https://docs.devin.ai/"
  },
  {
    "app_name": "YouTube Transcript",
    "self_serve": True,
    "self_serve_evidence": "Developers can freely use open-source SDKs like youtube-transcript-api without needing API keys.",
    "api_surface": "SDK only",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://pypi.org/project/youtube-transcript-api/"
  }
]

data_c1 = [
  {
    "app_name": "Salesforce",
    "self_serve": True,
    "self_serve_evidence": "Salesforce provides permanently free Developer Edition orgs for testing APIs.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.salesforce.com/signup"
  },
  {
    "app_name": "HubSpot",
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up for a free HubSpot account and spin up Developer Test Accounts.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.hubspot.com/"
  },
  {
    "app_name": "Pipedrive",
    "self_serve": True,
    "self_serve_evidence": "Offers a 14-day free trial and dedicated Developer Sandbox environments.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://pipedrive.readme.io/docs"
  },
  {
    "app_name": "Attio",
    "self_serve": True,
    "self_serve_evidence": "Attio offers a self-serve Free Tier with full API and webhook access.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.attio.com/"
  },
  {
    "app_name": "Close",
    "self_serve": True,
    "self_serve_evidence": "Close offers a self-serve free trial to test out features and generate test API keys.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.close.com/"
  },
  {
    "app_name": "Zendesk",
    "self_serve": True,
    "self_serve_evidence": "Zendesk offers a 14-day self-serve free trial and permanent Sponsored Developer Accounts.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.zendesk.com/"
  },
  {
    "app_name": "Intercom",
    "self_serve": True,
    "self_serve_evidence": "Intercom provides free developer workspaces for testing REST APIs and building apps.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.intercom.com/"
  },
  {
    "app_name": "Freshdesk",
    "self_serve": True,
    "self_serve_evidence": "Users can register for a self-serve 14-to-21-day free trial with API access enabled.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.freshdesk.com/api/"
  },
  {
    "app_name": "Pylon",
    "self_serve": False,
    "self_serve_evidence": "Pylon typically operates on a demo-led sales model for its core B2B platform rather than an open self-serve trial.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "requires sales demo/approval for account creation",
    "evidence_url": "https://docs.usepylon.com"
  },
  {
    "app_name": "Plain",
    "self_serve": True,
    "self_serve_evidence": "Plain offers a self-serve 14-day free trial on their standard plans to test the platform and API.",
    "api_surface": "GraphQL",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.plain.com"
  }
]

data_c3 = [
  {
    "app_name": "Mailchimp",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate API keys directly in their account settings under Extras.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://mailchimp.com/developer/marketing/docs/fundamentals/#authenticate-with-an-api-key"
  },
  {
    "app_name": "Klaviyo",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate private API keys directly in the Klaviyo account settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.klaviyo.com/en/docs/authenticate_with_klaviyo"
  },
  {
    "app_name": "Pinterest",
    "self_serve": True,
    "self_serve_evidence": "Developers can sign into the Pinterest Developer Portal to create apps and get an App ID and Client Secret.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.pinterest.com/docs/api/v5/"
  },
  {
    "app_name": "SendGrid",
    "self_serve": True,
    "self_serve_evidence": "API keys can be created directly through the Twilio SendGrid account dashboard settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.sendgrid.com/api-reference/how-to-use-the-sendgrid-v3-api/authentication"
  },
  {
    "app_name": "Shopify",
    "self_serve": True,
    "self_serve_evidence": "Developers can create custom apps via the Shopify Dev Dashboard or CLI to generate Admin API access tokens.",
    "api_surface": "GraphQL",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://shopify.dev/docs/apps/auth"
  },
  {
    "app_name": "Salesforce Commerce Cloud",
    "self_serve": True,
    "self_serve_evidence": "Account Administrators can use the self-service Account Manager to create API Clients and manage roles.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/b2c-admin-api-auth.html"
  },
  {
    "app_name": "Squarespace",
    "self_serve": True,
    "self_serve_evidence": "API keys can be generated directly from the Squarespace merchant site under Settings > Advanced > Developer API Keys.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.squarespace.com/commerce-apis/authentication-and-permissions"
  },
  {
    "app_name": "Gumroad",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate a self-issued access token directly in the advanced settings of their Gumroad account.",
    "api_surface": "REST - narrow",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://app.gumroad.com/api"
  },
  {
    "app_name": "DataForSEO",
    "self_serve": True,
    "self_serve_evidence": "API credentials can be found in the API Access section of the self-serve DataForSEO Dashboard.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.dataforseo.com/v3/getting-started/authentication"
  },
  {
    "app_name": "Ahrefs",
    "self_serve": False,
    "self_serve_evidence": "Ahrefs does not offer a free developer trial; API access is restricted to expensive Enterprise plans starting at $1,499/month.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "paid plan required",
    "evidence_url": "https://docs.ahrefs.com/docs/api/reference/introduction"
  }
]

data_c5 = [
  {
    "app_name": "Datadog",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly sign up for a free trial and generate API/App keys from Organization Settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.datadoghq.com/api/latest/"
  },
  {
    "app_name": "Sentry",
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up for free and generate internal integration tokens directly from Settings > Developer Settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.sentry.io/api/"
  },
  {
    "app_name": "Notion",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly create internal integrations in their workspace to get a Secret token.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.notion.com/"
  },
  {
    "app_name": "Airtable",
    "self_serve": True,
    "self_serve_evidence": "Developers can freely generate Personal Access Tokens directly from their Airtable Developer Hub.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://airtable.com/developers/web/api/introduction"
  },
  {
    "app_name": "Linear",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate Personal API keys for free from their workspace API settings.",
    "api_surface": "GraphQL",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.linear.app/docs/graphql/working-with-the-graphql-api"
  },
  {
    "app_name": "Jira",
    "self_serve": True,
    "self_serve_evidence": "Atlassian provides free Developer instances and allows instant creation of API tokens from account security settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/"
  },
  {
    "app_name": "Asana",
    "self_serve": True,
    "self_serve_evidence": "Developers can generate a Personal Access Token (PAT) freely from the Asana Developer Console.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.asana.com/docs/overview"
  },
  {
    "app_name": "Monday.com",
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up for a free developer account and instantly generate a personal API token in the Admin section.",
    "api_surface": "GraphQL",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.monday.com/api-reference/docs/authentication"
  },
  {
    "app_name": "ClickUp",
    "self_serve": True,
    "self_serve_evidence": "Users can instantly generate a Personal API token from their personal settings > Apps.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://clickup.com/api/developer-portal/authentication/"
  },
  {
    "app_name": "Coda",
    "self_serve": True,
    "self_serve_evidence": "Developers can easily generate an API token for free directly in their Coda account settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://coda.io/developers/apis/v1"
  }
]


import json
with open("master_dataset.json", "r") as f:
    master = json.load(f)

for item in data_c6 + data_c1 + data_c3 + data_c5:
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

print("Updated master_dataset.json with C6, C1, C3, and C5 results.")
