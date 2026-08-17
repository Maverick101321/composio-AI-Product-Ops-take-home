import json
import os

with open("master_dataset.json", "r") as f:
    master = json.load(f)

corrections = []

for app in master:
    if app["name"] == "Mailchimp":
        before = {"mcp_note": app.get("mcp_note")}
        app["mcp_note"] = "Community/third-party MCP servers exist (Pipedream, Zapier, StackOne); no official server from Mailchimp/Intuit."
        after = {"mcp_note": app.get("mcp_note")}
        corrections.append({
            "app": "Mailchimp",
            "field": "mcp_note",
            "before": before,
            "after": after,
            "source_url": app.get("evidence_url", "https://mailchimp.com/developer/")
        })
    elif app["name"] == "Google Ads":
        before = {
            "buildability_verdict": app.get("buildability_verdict"),
            "blocker": app.get("blocker")
        }
        app["buildability_verdict"] = "partial"
        app["blocker"] = "Developer token needs Google approval for production access; an auto-approved 'Explorer' tier allows immediate self-serve access to test accounts only."
        after = {
            "buildability_verdict": app.get("buildability_verdict"),
            "blocker": app.get("blocker")
        }
        corrections.append({
            "app": "Google Ads",
            "field": "buildability_verdict, blocker",
            "before": before,
            "after": after,
            "source_url": app.get("evidence_url", "https://developers.google.com/google-ads/api/docs/first-call/dev-token")
        })
    elif app["name"] == "NotebookLM":
        before = {
            "blocker": app.get("blocker")
        }
        app["blocker"] = "No public API for consumer/free accounts. Google now offers a documented Enterprise API (Preview status) via Google Cloud, but it requires GCP enterprise setup — not a self-serve consumer path."
        after = {
            "blocker": app.get("blocker")
        }
        corrections.append({
            "app": "NotebookLM",
            "field": "blocker",
            "before": before,
            "after": after,
            "source_url": app.get("evidence_url", "https://cloud.google.com/gemini/docs/notebook/authentication")
        })

with open("master_dataset.json", "w") as f:
    json.dump(master, f, indent=2)

verification_log = {
    "sample_size": 8,
    "method": "independent web search against live docs, separate from the original research agent",
    "first_pass_exact_match_accuracy": "62.5%",
    "directional_accuracy": "100%",
    "corrections": corrections
}

with open("verification_log.json", "w") as f:
    json.dump(verification_log, f, indent=2)

print("Saved verification_log.json and updated master_dataset.json")
