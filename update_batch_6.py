import json

updates = [
  {
    "app_name": "Supabase",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly create an account and generate Personal Access Tokens (PATs) for programmatic access.",
    "api_surface": "REST - broad, GraphQL",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://supabase.com/docs/reference/api/introduction"
  },
  {
    "app_name": "Neo4j",
    "self_serve": True,
    "self_serve_evidence": "Developers can spin up a cloud database via Neo4j Aura and instantly generate an API client ID and secret.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://neo4j.com/docs/operations-manual/current/authentication/"
  },
  {
    "app_name": "Snowflake",
    "self_serve": False,
    "self_serve_evidence": "Typically requires an enterprise setup with key-pair authentication configured by an administrator.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "blocked",
    "blocker": "Requires Snowflake account administrator setup and enterprise configuration.",
    "evidence_url": "https://docs.snowflake.com/en/user-guide/security-authentication-overview"
  },
  {
    "app_name": "Datadog",
    "self_serve": True,
    "self_serve_evidence": "Developers can create and manage API and Application keys directly within the Datadog platform under Organization Settings.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.datadoghq.com/api/latest/authentication/"
  },
  {
    "app_name": "Sentry",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly generate internal integration tokens for their organizations.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://docs.sentry.io/api/auth/"
  },
  {
    "app_name": "Notion",
    "self_serve": True,
    "self_serve_evidence": "Developers can create Personal Access Tokens and integrations instantly in the Notion Developer Portal.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.notion.com/docs/authorization"
  },
  {
    "app_name": "Airtable",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly generate Personal Access Tokens via the Airtable Developer hub.",
    "api_surface": "REST - broad",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://airtable.com/developers/web/api/authentication"
  },
  {
    "app_name": "Linear",
    "self_serve": True,
    "self_serve_evidence": "Developers can instantly generate Personal API Keys via their account security settings.",
    "api_surface": "GraphQL",
    "has_mcp": True,
    "buildability_verdict": "ready",
    "blocker": None,
    "evidence_url": "https://developers.linear.app/docs/graphql/working-with-the-graphql-api"
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
