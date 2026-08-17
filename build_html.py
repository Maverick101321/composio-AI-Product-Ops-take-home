import json

def generate_html():
    with open("master_dataset.json", "r") as f:
        apps = json.load(f)
        
    with open("verification_log.json", "r") as f:
        vlog = json.load(f)
        
    corrections_html = ""
    for c in vlog["corrections"]:
        corrections_html += f"<li><strong>{c['app']}</strong> ({c['field']}):<br><em>Before:</em> {c['before']}<br><em>After:</em> {c['after']}<br><a href='{c['source_url']}' target='_blank'>Source</a></li>\\n                "

    # Calculate stats
    total = len(apps)
    researched = sum(1 for app in apps if app.get("api_surface") != "unknown")
    self_serve_true = sum(1 for app in apps if app.get("self_serve") is True)
    self_serve_false = sum(1 for app in apps if app.get("self_serve") is False)
    ready = sum(1 for app in apps if app.get("buildability_verdict") == "ready")
    blocked = sum(1 for app in apps if app.get("buildability_verdict") == "blocked")
    has_mcp = sum(1 for app in apps if app.get("has_mcp") is True)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Composio App Research - AI Product Ops</title>
    <style>
        :root {{
            --primary: #1a1a1a;
            --secondary: #4a4a4a;
            --accent: #0066cc;
            --success: #28a745;
            --danger: #dc3545;
            --bg: #f8f9fa;
            --card-bg: #ffffff;
            --border: #e0e0e0;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            color: var(--primary);
            background-color: var(--bg);
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        header {{
            text-align: center;
            margin-bottom: 40px;
        }}
        h1 {{
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 10px;
        }}
        h2 {{
            color: var(--secondary);
            border-bottom: 2px solid var(--accent);
            padding-bottom: 10px;
            margin-top: 40px;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        .stat-card {{
            background: var(--card-bg);
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            text-align: center;
        }}
        .stat-number {{
            font-size: 2rem;
            font-weight: bold;
            color: var(--accent);
        }}
        .stat-label {{
            color: var(--secondary);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .insight-block {{
            background: var(--card-bg);
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            border-left: 5px solid var(--accent);
        }}
        .insight-block h3 {{
            margin-top: 0;
            color: var(--accent);
        }}
        .patterns-section {{
            background: var(--card-bg);
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            margin-bottom: 40px;
            border-left: 5px solid var(--accent);
        }}
        .patterns-section h3 {{
            margin-top: 0;
            color: var(--accent);
        }}
        .badge {{
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: bold;
            color: white;
        }}
        .badge-ready {{ background-color: var(--success); }}
        .badge-blocked {{ background-color: var(--danger); }}
        .badge-partial {{ background-color: #ffc107; color: #000; }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            background: var(--card-bg);
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            border-radius: 8px;
            overflow: hidden;
            margin-top: 20px;
        }}
        th, td {{
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }}
        th {{
            background-color: #f1f3f5;
            font-weight: 600;
            color: var(--secondary);
        }}
        tr:hover {{
            background-color: #f8f9fa;
        }}
        a {{
            color: var(--accent);
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>AI Product Ops: 100 Apps Research</h1>
            <p>Automated analysis of top 100 SaaS APIs for AI agent integration readiness.</p>
        </header>

        <section id="patterns-insights" class="insights-container">
            <h2>Key Patterns & Insights</h2>
            
            <div class="insight-block">
                <h3>1. Authentication: OAuth2 and API Keys Dominate</h3>
                <p>When it comes to securing developer access, <strong>OAuth2 and API keys</strong> cover the clear majority of the 100 apps we analyzed. While there is a long, thin tail of variants—including Bearer tokens, Basic Auth, PATs, and JWTs—the industry has largely standardized around these two models. Notably, two tools (Sherlock and Mermaid CLI) bypass traditional auth entirely, operating strictly as local CLI tools.</p>
            </div>

            <div class="insight-block">
                <h3>2. Self-Serve is the Default, Not the Exception</h3>
                <p>Gatekeeping basic API access is becoming rare. Overall, <strong>{self_serve_true} out of {researched} apps are fully self-serve</strong>, allowing developers to generate credentials without talking to a human. Certain sectors are completely frictionless: Communications/Messaging and Productivity/Project Management boast a 100% self-serve rate, making them the easiest categories to build in. The remaining categories still cluster strongly around an 80-90% self-serve rate.</p>
            </div>

            <div class="insight-block">
                <h3>3. The "Blocked" Apps Share a Common Theme: Gatekeeping</h3>
                <p>Our final buildability breakdown sits at <strong>{ready} Ready, {blocked} Blocked, and 1 Partial</strong> (Google Ads). The {blocked} blocked apps reveal a stark pattern: the blocker is almost never a lack of technology. With the sole exception of NotebookLM (which currently lacks any public consumer API path), blockers are driven purely by business gatekeeping:</p>
                <ul>
                    <li><strong>Enterprise-Tier Requirements (4):</strong> Snowflake, PitchBook, Otter AI, Ahrefs</li>
                    <li><strong>Partner/Sales Approval (5):</strong> DealCloud, Pylon, Waterfall.io, Paygent Connect, Salesforce Commerce Cloud</li>
                    <li><strong>Paid Plan Required (1):</strong> Amazon Selling Partner</li>
                    <li><strong>Platform Review Gates (1):</strong> LinkedIn Ads</li>
                    <li><strong>No Public Consumer API (1):</strong> NotebookLM</li>
                </ul>
            </div>

            <div class="insight-block">
                <h3>4. MCP Adoption Tracks Dev-Tool Maturity, Not Company Size</h3>
                <p>Model Context Protocol (MCP) availability strongly correlates with the engineering culture of the platform. Categories like Developer/Infra, Productivity/PM, and AI-native tools show a massive <strong>90-100% MCP coverage</strong>. Conversely, CRM/Sales and Marketing/Ads platforms lag significantly at around 50%. MCP adoption is currently driven by developer-tool culture rather than sheer company size or revenue.</p>
            </div>

            <div class="insight-block">
                <h3>5. The Importance of Human-in-the-Loop Verification</h3>
                <p>Our human-directed research agent flagged an impressive {has_mcp} out of {researched} apps as having an MCP server (<code>has_mcp: true</code>). Because claims of finding integrations are highly susceptible to AI false positives, this became a priority for our hand-check sample.</p>
                <p>We ran a targeted, independent 8-app verification pass. The verification confirmed 5 out of 8 checks exactly (100% directional accuracy), but highlighted a critical nuance the agent missed: <strong>the distinction between official, first-party MCP servers and community-built wrappers</strong> (e.g., Mailchimp, which relies on community servers like Pipedream or StackOne). The verification pass also successfully corrected two blocker descriptions (shifting Google Ads to "partial" and clarifying NotebookLM's enterprise-only preview status). This ties our data together perfectly: while AI agents are incredible at bulk data gathering, human-in-the-loop verification remains essential for catching nuanced technical distinctions.</p>
            </div>
        </section>

        <h2>Research Statistics</h2>
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">{researched}</div>
                <div class="stat-label">Apps Researched</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{self_serve_true}</div>
                <div class="stat-label">Self-Serve APIs</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{ready}</div>
                <div class="stat-label">Toolkit Ready</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{blocked}</div>
                <div class="stat-label">Blocked/Gated</div>
            </div>
        </div>

        <h2>Methodology: The Agent & Verification</h2>
        <div class="patterns-section" style="border-left-color: #28a745;">
            <h3>The Pipeline</h3>
            <p>Our research methodology relied on human-directed, iterative agent execution—pairing the <strong>Composio SDK</strong> for programmatic data with the <strong>Gemini CLI</strong> for qualitative research.</p>
            <ol>
                <li><strong>Catalog Matching:</strong> First, a script cross-referenced the 100 apps against the live Composio Toolkit catalog using <code>composio.toolkits.list()</code>. It matched 61 apps instantly, extracting their authentication schemes and base URLs.</li>
                <li><strong>Web Research:</strong> A human operator (acting as manager) directed the Gemini CLI through a sequence of small, scoped prompts (researching batches of 5-8 apps at a time). The agent utilized web search tools to locate specific developer documentation and extract missing qualitative data (Self-serve status, blockers, MCP availability).</li>
                <li><strong>Human in the loop:</strong> The human operator reviewed and validated the output after every batch, issuing corrections when the agent's output was incomplete or hallucinated (e.g., rejecting bare homepages and demanding specific API documentation URLs, or catching that Mailchimp's MCP servers are community-built rather than official).</li>
            </ol>
            <h3>Accuracy Verification (Sample)</h3>
            <p>We verified a targeted, risk-weighted sample of {vlog['sample_size']} apps — prioritizing the claims most likely to contain errors (MCP existence claims and 'blocked' verdicts) rather than a pure random sample. Exact-match accuracy was <strong>{vlog['first_pass_exact_match_accuracy']}</strong>, with directional accuracy of <strong>{vlog['directional_accuracy']}</strong>.</p>
            <p>The apps checked were: Notion, Airtable, Linear, Cloudflare, Mailchimp, Google Ads, NotebookLM, and Twenty.</p>
            <p>There were {len(vlog['corrections'])} nuanced misses corrected:</p>
            <ul>
                {corrections_html}
            </ul>
        </div>

        <h2>Proof: Run It Yourself</h2>
        <div class="patterns-section" style="border-left-color: #17a2b8;">
            <p>This is a live excerpt from an actual run — not fabricated output — demonstrating the same research logic that built the full 100-app dataset.</p>
            <pre style="background: #f1f3f5; padding: 15px; border-radius: 5px; overflow-x: auto;"><code>python research_pipeline.py --research "Twenty"</code></pre>
            <pre style="background: #272822; color: #f8f8f2; padding: 15px; border-radius: 5px; overflow-x: auto;"><code>{{
  "self_serve": true,
  "self_serve_evidence": "Twenty is an open-source CRM that offers both a self-serve cloud platform (app.twenty.com) and the ability to self-host workspaces.",
  "api_surface": "Dynamic REST and GraphQL APIs that automatically update based on tenant schema, alongside a Metadata API for schema management.",
  "has_mcp": true,
  "mcp_note": "Twenty includes a native Model Context Protocol (MCP) server built directly into its cloud workspaces, supporting OAuth for direct AI client connections.",
  "buildability_verdict": "ready",
  "blocker": null,
  "evidence_url": "https://docs.twenty.com"
}}</code></pre>
            <p><a href="https://github.com/Maverick101321/composio-AI-Product-Ops-take-home" target="_blank" style="font-weight: bold;">View the GitHub Repository</a></p>
        </div>

        <h2>Raw Data Matrix</h2>
        <table>
            <thead>
                <tr>
                    <th>#</th>
                    <th>App</th>
                    <th>Category</th>
                    <th>Auth</th>
                    <th>Self-Serve</th>
                    <th>Verdict</th>
                    <th>Blocker</th>
                    <th>Docs</th>
                </tr>
            </thead>
            <tbody>
"""
    for app in apps:
        if app.get("api_surface") == "unknown":
            continue
            
        verdict = app.get('buildability_verdict', 'unknown')
        badge_class = f"badge badge-{verdict}"
        
        auths = ", ".join(app.get('auth_methods', []))
        if not auths:
            auths = "None"
            
        ss = "✅" if app.get('self_serve') else "❌"
        
        docs = f"<a href='{app.get('evidence_url')}' target='_blank'>Link</a>" if app.get('evidence_url') else "N/A"
        
        blocker = app.get('blocker') or "-"
        
        html += f"""
                <tr>
                    <td>{app.get('number')}</td>
                    <td><strong>{app.get('name')}</strong></td>
                    <td>{app.get('category')}</td>
                    <td>{auths}</td>
                    <td>{ss}</td>
                    <td><span class="{badge_class}">{verdict.upper()}</span></td>
                    <td>{blocker}</td>
                    <td>{docs}</td>
                </tr>
"""
    
    html += """
            </tbody>
        </table>
    </div>
</body>
</html>
"""
    
    with open("index.html", "w") as f:
        f.write(html)
        
    print("Generated index.html!")

if __name__ == "__main__":
    generate_html()
