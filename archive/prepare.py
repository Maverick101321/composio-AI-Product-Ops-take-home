import json

data = """
1. CRM and Sales
1 Salesforce salesforce.com
2 HubSpot hubspot.com
3 Pipedrive pipedrive.com
4 Attio attio.com
5 Twenty twenty.com
6 Podio podio.com
7 Zoho CRM zoho.com/crm
8 Close close.com
9 Copper copper.com
10 DealCloud api.docs.dealcloud.com

2. Support and Helpdesk
11 Zendesk zendesk.com
12 Intercom intercom.com
13 Freshdesk freshdesk.com
14 Front front.com
15 Pylon usepylon.com
16 LiveAgent liveagent.com
17 Plain plain.com
18 Help Scout helpscout.com
19 Gorgias gorgias.com
20 Gladly gladly.com

3. Communications and Messaging
21 Slack slack.com
22 Twilio twilio.com
23 Zoho Cliq zoho.com/cliq
24 Lark (Larksuite) open.larksuite.com
25 Pumble pumble.com
26 Discord discord.com
27 Telegram core.telegram.org
28 WhatsApp Business developers.facebook.com/docs/whatsapp
29 Aircall aircall.io
30 Vonage developer.vonage.com

4. Marketing, Ads, Email and Social
31 Google Ads developers.google.com/google-ads
32 Meta Ads developers.facebook.com/docs/marketing-apis
33 LinkedIn Ads learn.microsoft.com/linkedin/marketing
34 GoHighLevel highlevel.stoplight.io
35 Mailchimp mailchimp.com/developer
36 Klaviyo developers.klaviyo.com
37 systeme.io systeme.io
38 Pinterest developers.pinterest.com
39 Threads (Meta) developers.facebook.com/docs/threads
40 SendGrid sendgrid.com

5. Ecommerce
41 Shopify shopify.dev
42 WooCommerce woocommerce.com/document/woocommerce-rest-api
43 BigCommerce developer.bigcommerce.com
44 Salesforce Commerce Cloud developer.salesforce.com/docs/commerce
45 Magento (Adobe Commerce) developer.adobe.com/commerce
46 Squarespace developers.squarespace.com
47 Ecwid api-docs.ecwid.com
48 Gumroad gumroad.com/api
49 Amazon Selling Partner developer-docs.amazon.com/sp-api
50 fanbasis fanbasis.com

6. Data, SEO and Scraping
51 DataForSEO docs.dataforseo.com
52 SE Ranking seranking.com/api
53 Ahrefs ahrefs.com/api
54 MrScraper docs.mrscraper.com
55 Apify docs.apify.com
56 Firecrawl firecrawl.dev
57 Bright Data brightdata.com
58 Sherlock github.com/sherlock-project/sherlock
59 Waterfall.io waterfall.io
60 Clay clay.com

7. Developer, Infra and Data platforms
61 GitHub docs.github.com/rest
62 Vercel vercel.com/docs/rest-api
63 Netlify docs.netlify.com/api
64 Cloudflare developers.cloudflare.com/api
65 Supabase supabase.com/docs
66 Neo4j neo4j.com/docs/api
67 Snowflake docs.snowflake.com
68 MongoDB Atlas mongodb.com/docs/atlas/api
69 Datadog docs.datadoghq.com/api
70 Sentry docs.sentry.io/api

8. Productivity and Project Management
71 Notion developers.notion.com
72 Airtable airtable.com/developers
73 Linear developers.linear.app
74 Jira developer.atlassian.com
75 Asana developers.asana.com
76 Monday.com developer.monday.com
77 ClickUp clickup.com/api
78 Coda coda.io/developers
79 Smartsheet smartsheet.com/developers
80 Harvest harvestapp.com

9. Finance and Fintech
81 Stripe stripe.com/docs/api
82 Plaid plaid.com/docs
83 Binance binance-docs.github.io
84 Paygent Connect paygent
85 iPayX ipayx.ai/docs
86 QuickBooks developer.intuit.com
87 Xero developer.xero.com
88 Brex developer.brex.com
89 Ramp docs.ramp.com
90 PitchBook pitchbook.com

10. AI, Research and Media-native
91 NotebookLM notebooklm.google.com
92 Otter AI otter.ai
93 Fathom fathom.video
94 Consensus consensus.app
95 Reducto reducto.ai
96 Devin devin.ai
97 higgsfield higgsfield.ai
98 Mermaid CLI github.com/mermaid-js/mermaid-cli
99 YouTube Transcript youtube.com
100 Grain grain.com
"""

apps = []
current_category = ""
for line in data.strip().split('\n'):
    line = line.strip()
    if not line:
        continue
    if line[0].isdigit() and '. ' in line and len(line) > 5 and line.split('. ')[0].isdigit():
        # Category line
        current_category = line.split('. ', 1)[1]
    else:
        # App line
        parts = line.split(' ')
        number = int(parts[0])
        # Find where website hint starts (usually the last token)
        website_hint = parts[-1]
        name = ' '.join(parts[1:-1])
        apps.append({
            "number": number,
            "name": name,
            "category": current_category,
            "website_hint": website_hint
        })

with open("apps.json", "w") as f:
    json.dump(apps, f, indent=2)

print(f"Saved {len(apps)} apps to apps.json")
