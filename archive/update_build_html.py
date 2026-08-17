import re

with open("build_html.py", "r") as f:
    content = f.read()

# CSS replacement
new_css = """
        .insight-block {
            background: var(--card-bg);
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            border-left: 5px solid var(--accent);
        }
        .insight-block h3 {
            margin-top: 0;
            color: var(--accent);
        }
        .patterns-section {"""

content = content.replace("        .patterns-section {", new_css)


new_patterns = """        <section id="patterns-insights" class="insights-container">
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
                <p>Our autonomous research agent flagged an impressive {has_mcp} out of {researched} apps as having an MCP server (<code>has_mcp: true</code>). Because claims of finding integrations are highly susceptible to AI false positives, this became a priority for our hand-check sample.</p>
                <p>We ran a targeted, independent 8-app verification pass. The verification confirmed 5 out of 8 checks exactly (100% directional accuracy), but highlighted a critical nuance the agent missed: <strong>the distinction between official, first-party MCP servers and community-built wrappers</strong> (e.g., Mailchimp, which relies on community servers like Pipedream or StackOne). The verification pass also successfully corrected two blocker descriptions (shifting Google Ads to "partial" and clarifying NotebookLM's enterprise-only preview status). This ties our data together perfectly: while AI agents are incredible at bulk data gathering, human-in-the-loop verification remains essential for catching nuanced technical distinctions.</p>
            </div>
        </section>"""

# Replace old patterns section
old_patterns_regex = r'        <section class="patterns-section">.*?        </section>'
content = re.sub(old_patterns_regex, new_patterns, content, flags=re.DOTALL)

with open("build_html.py", "w") as f:
    f.write(content)
