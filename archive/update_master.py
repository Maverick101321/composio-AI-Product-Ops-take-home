import json

subagent_data = [
  {
    "app_name": "Binance",
    "one_liner": "Binance offers a comprehensive suite of APIs for spot trading, futures, options, market data, and account management.",
    "auth_methods": ["API Key", "API Secret"],
    "self_serve": True,
    "self_serve_evidence": "Developers can generate API keys directly from their Binance dashboard without contacting sales.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.binance.com"
  },
  {
    "app_name": "Paygent Connect",
    "one_liner": "Paygent Connect is a Japanese payment gateway offering B2B modules and API integrations for e-commerce transactions.",
    "auth_methods": ["Client Certificate", "Merchant ID", "Connection ID", "Connection Password"],
    "self_serve": False,
    "self_serve_evidence": "API documentation and sandbox environments are only accessible upon signing a contract with Paygent via their merchant management screen.",
    "api_surface": "REST - narrow",
    "has_mcp": False,
    "buildability_verdict": "blocked",
    "blocker": "Requires merchant contract and partner approval to access documentation and sandbox.",
    "evidence_url": "https://www.paygent.co.jp/"
  },
  {
    "app_name": "iPayX",
    "one_liner": "iPayX provides a developer API and MCP server for forensic foreign exchange auditing and detecting hidden bank markups.",
    "auth_methods": ["API Key"],
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up on ipayx.ai to get an API key and integrate with their endpoint.",
    "api_surface": "REST - narrow",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://ipayx.ai/docs"
  },
  {
    "app_name": "PitchBook",
    "one_liner": "PitchBook is a financial data provider that offers comprehensive insights into private and public markets via its API.",
    "auth_methods": ["API Key"],
    "self_serve": False,
    "self_serve_evidence": "Access to the PitchBook API requires an enterprise-tier offering, and clients must request access directly from the PitchBook Platform or sales team.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "Enterprise subscription required, manual access approval.",
    "evidence_url": "https://pitchbook.com/products/api-and-direct-data"
  },
  {
    "app_name": "Otter AI",
    "one_liner": "Otter.ai is an AI-powered meeting assistant that provides automated transcription, summaries, and action item extraction accessible programmatically.",
    "auth_methods": ["Bearer Token"],
    "self_serve": False,
    "self_serve_evidence": "The Public API is restricted to the Otter Enterprise plan, and access may need to be requested via an account manager.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "Enterprise plan required for API access.",
    "evidence_url": "https://help.otter.ai/hc/en-us/articles/12395350314135-Otter-Developer-API"
  },
  {
    "app_name": "Reducto",
    "one_liner": "Reducto provides an API and developer toolkit for advanced document processing, extracting structured data from unstructured files like PDFs and images.",
    "auth_methods": ["API Key"],
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up at Reducto Studio and generate an API key immediately to use with their SDKs.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.reductoai.com"
  },
  {
    "app_name": "higgsfield",
    "one_liner": "Higgsfield AI provides a suite of APIs for generating and editing high-quality video and image content using state-of-the-art AI models.",
    "auth_methods": ["API Key", "API Secret", "OAuth"],
    "self_serve": True,
    "self_serve_evidence": "Developers can register on cloud.higgsfield.ai to generate API credentials and purchase API credits directly from the dashboard.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.higgsfield.ai"
  },
  {
    "app_name": "Mermaid CLI",
    "one_liner": "Mermaid CLI is a command-line tool that renders Mermaid diagrams into visual formats like SVG, PNG, or PDF locally.",
    "auth_methods": [],
    "self_serve": True,
    "self_serve_evidence": "It is an open source Node.js CLI tool that can be installed directly via npm without any registration.",
    "api_surface": "SDK only",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://github.com/mermaid-js/mermaid-cli"
  },
  {
    "app_name": "Grain",
    "one_liner": "Grain is an AI-powered meeting assistant that provides a developer API to programmatically access meeting recordings, transcripts, and highlights.",
    "auth_methods": ["Personal Access Token", "Workspace Access Token", "OAuth 2.0"],
    "self_serve": True,
    "self_serve_evidence": "Tokens and OAuth configurations can be generated directly from the Integrations & API Settings page within a Grain account.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://grain.com/app/settings/integrations?tab=api"
  },
  {
    "app_name": "Amazon Selling Partner",
    "one_liner": "The Amazon Selling Partner API allows developers to build applications that programmatically access Amazon listings, orders, and fulfillment data.",
    "auth_methods": ["OAuth2"],
    "self_serve": False,
    "self_serve_evidence": "Registering as a developer requires an active Professional Selling Account ($39.99/mo) and identity verification.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "paid plan required",
    "evidence_url": "https://developer-docs.amazon.com/sp-api/docs/authorizing-selling-partner-api-applications"
  },
  {
    "app_name": "fanbasis",
    "one_liner": "Fanbasis provides developer infrastructure and APIs for creator economy tools, multi-processor payment orchestration, and alternative payment rails.",
    "auth_methods": ["API key"],
    "self_serve": False,
    "self_serve_evidence": "Access to technical documentation and API keys requires booking a demo or contacting their implementation team.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "blocked",
    "blocker": "requires sales contact",
    "evidence_url": "https://fanbasis.com"
  },
  {
    "app_name": "SE Ranking",
    "one_liner": "SE Ranking provides an API to programmatically access SEO data including keyword rank tracking, website audits, and competitor research.",
    "auth_methods": ["API key"],
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up for a 14-day free trial and generate an API key directly from their account settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://seranking.com/api.html"
  },
  {
    "app_name": "Sherlock",
    "one_liner": "Sherlock is an open-source command-line tool used to hunt down social media accounts by username across various networks.",
    "auth_methods": [],
    "self_serve": True,
    "self_serve_evidence": "It is a free, open-source tool available for anyone to clone and use from GitHub.",
    "api_surface": "no public API",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://github.com/sherlock-project/sherlock"
  },
  {
    "app_name": "Waterfall.io",
    "one_liner": "Waterfall.io provides a Go-to-Market API that aggregates over 30 data vendors for B2B data enrichment and prospecting.",
    "auth_methods": ["API key"],
    "self_serve": False,
    "self_serve_evidence": "Testing the API requires booking a demo or call with their team rather than an automated self-serve signup.",
    "api_surface": "REST - narrow",
    "has_mcp": False,
    "buildability_verdict": "blocked",
    "blocker": "requires sales contact",
    "evidence_url": "https://waterfall.io"
  },
  {
    "app_name": "Clay",
    "one_liner": "Clay is a data enrichment and automation platform that aggregates multiple data providers to build automated GTM workflows.",
    "auth_methods": ["API key"],
    "self_serve": True,
    "self_serve_evidence": "Users can sign up for a free tier and manage their personal API key directly from their workspace settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://clay.com/developer"
  },
  {
    "app_name": "Netlify",
    "one_liner": "Netlify provides a platform for deploying, scaling, and managing modern web applications and frontend infrastructure.",
    "auth_methods": ["OAuth2", "Personal Access Token"],
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up for free and generate Personal Access Tokens directly from their Netlify User Settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.netlify.com/api/get-started/"
  },
  {
    "app_name": "MongoDB Atlas",
    "one_liner": "MongoDB Atlas is a fully managed cloud database service offering APIs to programmatically manage clusters and database infrastructure.",
    "auth_methods": ["OAuth2", "API key", "HTTP Digest"],
    "self_serve": True,
    "self_serve_evidence": "Developers can create a free Atlas account and instantly generate API keys or Service Accounts via the Atlas UI.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://www.mongodb.com/docs/atlas/api/"
  },
  {
    "app_name": "Smartsheet",
    "one_liner": "Smartsheet is a cloud-based enterprise work management platform that offers an API to automate sheet updates and collaboration.",
    "auth_methods": ["OAuth2", "Personal Access Token"],
    "self_serve": True,
    "self_serve_evidence": "Developers can start a 30-day free trial and generate Personal Access Tokens directly from the API Access tab in their settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://smartsheet.redoc.ly/"
  },
  {
    "app_name": "Plaid",
    "one_liner": "Plaid provides APIs that connect applications to users' bank accounts to access financial data and authenticate accounts.",
    "auth_methods": ["API key"],
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly sign up for a Plaid Dashboard account to access Sandbox API keys for free testing.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://plaid.com/docs/api/"
  },
  {
    "app_name": "Lark (Larksuite)",
    "one_liner": "An all-in-one enterprise collaboration platform offering messaging, docs, and calendar.",
    "auth_methods": ["OAuth2", "API Key"],
    "self_serve": True,
    "self_serve_evidence": "Developers can register an application in the Lark Developer Console to obtain app credentials for free.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://open.larksuite.com/document/server-docs/getting-started/api-overview"
  },
  {
    "app_name": "Pumble",
    "one_liner": "A team communication and collaboration app offering chat and messaging features.",
    "auth_methods": ["API Key"],
    "self_serve": True,
    "self_serve_evidence": "Users can generate API keys directly inside the chat interface using a slash command or in the workspace settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://pumble.com/help/api/"
  },
  {
    "app_name": "Aircall",
    "one_liner": "A cloud-based business phone system and call center software.",
    "auth_methods": ["Basic", "OAuth2"],
    "self_serve": True,
    "self_serve_evidence": "Customers can easily generate API keys directly from their Aircall dashboard for internal use.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.aircall.io/api-references/#authentication"
  },
  {
    "app_name": "Vonage",
    "one_liner": "A cloud communications platform providing voice, messaging, and video APIs.",
    "auth_methods": ["JWT", "Basic", "API Key"],
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up and create an application in the Vonage Dashboard to get credentials.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.vonage.com/en/getting-started/concepts/authentication"
  },
  {
    "app_name": "systeme.io",
    "one_liner": "An all-in-one marketing platform for building sales funnels, sending emails, and managing online courses.",
    "auth_methods": ["API Key"],
    "self_serve": True,
    "self_serve_evidence": "Users can generate a Public API token directly from their Systeme.io account settings.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://systeme.io/help/articles/11099688-how-to-generate-an-api-key"
  },
  {
    "app_name": "Threads (Meta)",
    "one_liner": "A text-based social media platform created by Meta.",
    "auth_methods": ["OAuth2"],
    "self_serve": True,
    "self_serve_evidence": "Developers can create an app in the Meta Developer dashboard to test with their own account, though public access requires App Review.",
    "api_surface": "REST - narrow",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.facebook.com/docs/threads/overview"
  },
  {
    "app_name": "WooCommerce",
    "one_liner": "An open-source e-commerce plugin built for WordPress.",
    "auth_methods": ["Basic", "OAuth 1.0a"],
    "self_serve": True,
    "self_serve_evidence": "Developers can generate a Consumer Key and Consumer Secret directly from the WooCommerce admin dashboard.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://woocommerce.com/document/woocommerce-rest-api/"
  },
  {
    "app_name": "BigCommerce",
    "one_liner": "A versatile e-commerce platform for creating and managing online stores.",
    "auth_methods": ["OAuth2", "API Token", "JWT"],
    "self_serve": True,
    "self_serve_evidence": "Developers can generate API credentials from the BigCommerce Control Panel for custom integrations.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.bigcommerce.com/api-docs/getting-started/authentication"
  },
  {
    "app_name": "Magento (Adobe Commerce)",
    "one_liner": "A flexible and scalable e-commerce platform for B2B and B2C businesses.",
    "auth_methods": ["Bearer Token", "OAuth 1.0a"],
    "self_serve": True,
    "self_serve_evidence": "Admins can generate integration tokens directly from the Magento Admin panel.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.adobe.com/commerce/webapi/rest/authentication/"
  },
  {
    "app_name": "Ecwid",
    "one_liner": "An e-commerce platform that allows users to add online stores to existing websites.",
    "auth_methods": ["OAuth2", "API Token"],
    "self_serve": True,
    "self_serve_evidence": "Merchants can generate secret tokens for REST API access by creating a Custom App in the Ecwid Admin Panel.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://api-docs.ecwid.com/reference/rest-api-overview"
  },
  {
    "app_name": "Twenty",
    "one_liner": "Twenty is an open-source CRM that allows users to manage contacts, opportunities, and activities natively in the cloud or self-hosted.",
    "auth_methods": ["API keys", "Bearer token"],
    "self_serve": True,
    "self_serve_evidence": "Developers can generate a secret token directly from their instance's Settings > API & Webhooks under Developers.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.twenty.com/developers/api/authentication"
  },
  {
    "app_name": "Podio",
    "one_liner": "Podio is a customizable work management and CRM platform that organizes team communication, business processes, and data.",
    "auth_methods": ["OAuth 2.0", "App Token"],
    "self_serve": True,
    "self_serve_evidence": "Developers can register an application on Podio to receive a unique Client ID and Client Secret for OAuth 2.0 authentication.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.podio.com/authentication"
  },
  {
    "app_name": "Zoho CRM",
    "one_liner": "Zoho CRM is an online sales management software that manages sales, marketing, and support in a single system.",
    "auth_methods": ["OAuth 2.0"],
    "self_serve": True,
    "self_serve_evidence": "Developers can access the Zoho API Console to freely register a client and receive credentials.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://www.zoho.com/crm/developer/docs/api/v6/oauth-overview.html"
  },
  {
    "app_name": "Copper",
    "one_liner": "Copper is a CRM tailored for Google Workspace users that helps manage leads, contacts, and sales pipelines.",
    "auth_methods": ["API keys", "OAuth 2.0"],
    "self_serve": True,
    "self_serve_evidence": "Users can generate an API Key directly from the Copper web app under Settings > Integrations > API Keys.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.copper.com/authentication.html"
  },
  {
    "app_name": "DealCloud",
    "one_liner": "DealCloud is a CRM and deal management platform designed specifically for financial services and investment banking.",
    "auth_methods": ["OAuth 2.0 Client Credentials"],
    "self_serve": False,
    "self_serve_evidence": "Intapp DealCloud does not offer a public self-service free trial; access requires an enterprise sandbox or client provisioned environment.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "Requires enterprise client or partner approval, no self-serve developer access.",
    "evidence_url": "https://api.docs.dealcloud.com"
  },
  {
    "app_name": "Front",
    "one_liner": "Front is a customer operations platform that functions as a shared inbox and helpdesk CRM for teams.",
    "auth_methods": ["Bearer Token", "OAuth 2.0"],
    "self_serve": True,
    "self_serve_evidence": "Developers can create API tokens under Settings > Developers > API Tokens, or register an OAuth app in the Front Developer Center.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://dev.frontapp.com/docs/authentication-1"
  },
  {
    "app_name": "LiveAgent",
    "one_liner": "LiveAgent is a helpdesk and ticketing system that helps businesses provide multichannel customer support.",
    "auth_methods": ["API Key"],
    "self_serve": True,
    "self_serve_evidence": "Developers can generate an API Key directly from the LiveAgent panel under Configuration > System > API.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://support.liveagent.com/840770-Complete-API-reference"
  },
  {
    "app_name": "Gladly",
    "one_liner": "Gladly is a radically personal customer service platform centered around people, not tickets.",
    "auth_methods": ["Basic Authentication"],
    "self_serve": True,
    "self_serve_evidence": "Users with API permissions can generate an API Token from their settings and use it as a password for Basic Auth.",
    "api_surface": "REST - broad",
    "has_mcp": False,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developer.gladly.com/rest/"
  },
  {
    "app_name": "Twilio",
    "one_liner": "Twilio is a cloud communications platform that enables developers to build voice, video, and messaging applications.",
    "auth_methods": ["Basic Authentication", "API Keys"],
    "self_serve": True,
    "self_serve_evidence": "Developers can sign up for a free Twilio account and immediately generate API keys or use their account SID and Auth Token.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://www.twilio.com/docs/usage/security"
  },
  {
    "app_name": "Zoho Cliq",
    "one_liner": "Zoho Cliq is a team communication and collaboration software that integrates with other Zoho apps and third-party tools.",
    "auth_methods": ["OAuth 2.0"],
    "self_serve": True,
    "self_serve_evidence": "Developers can freely access the Zoho API Console to register a client and receive OAuth credentials.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://www.zoho.com/cliq/help/restapi/authentication.html"
  }
]

with open("master_dataset.json", "r") as f:
    master = json.load(f)

for item in subagent_data:
    app_name = item.get("app_name") or item.get("app")
    if not app_name:
        continue
    # Find the corresponding app in master
    for m in master:
        if m["name"].lower() == app_name.lower():
            m["one_liner"] = item["one_liner"]
            m["auth_methods"] = item["auth_methods"]
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

print("Updated master_dataset.json with subagent results.")
