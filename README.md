# Composio App Research - AI Product Ops

This repository contains the work for the Composio AI Product Ops take-home assignment. The objective was to research a targeted list of 100 SaaS applications and evaluate their "buildability"—determining how easily they could be integrated as autonomous agent toolkits based on their authentication models, API surfaces, self-serve developer access, and Model Context Protocol (MCP) availability.

## Setup

1. **Clone the repository**
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Environment Variables**
   Create a `.env` file in the root directory and add your Composio API key:
   ```env
   COMPOSIO_API_KEY=your_api_key_here
   ```

## Running the Pipeline

The core research logic has been consolidated into `research_pipeline.py`. 

- **Research a single app:**
  ```bash
  python research_pipeline.py --research "App Name"
  ```
  *Note: This utilizes the `agy` (Gemini CLI) behind the scenes to perform web searches and structured data extraction.*

- **Validate the dataset:**
  ```bash
  python research_pipeline.py --validate
  ```
  *Checks `master_dataset.json` to ensure no fields are missing or unknown, and validates that all evidence URLs point to specific documentation pages rather than bare homepages.*

## Process Summary

1. **Catalog Matching:** The Composio SDK was used to instantly match 61 of the 100 apps to their existing catalog via `composio.toolkits.list()`, automatically extracting their known authentication schemes and categories.
2. **AI-Assisted Web Research:** The remaining 39 apps, along with the enrichment of all 100 apps for qualitative fields (self-serve status, API surface, MCP availability, and buildability verdicts), were researched using an agent loop. This loop shells out to the Gemini CLI with a strict, schema-enforced prompt, executes web searches against developer docs, and parses the returned JSON.
3. **Iterative Execution:** Most of the actual 100-app research was run interactively through the Gemini CLI directed by a human operator, processing small batches to manage rate limits and ensure quality. `research_pipeline.py` consolidates that exact logic into a single reusable script.

## Verification

An independent 8-app spot-check was performed against live documentation (separate from the research agent's initial pass) to verify accuracy. 
- The check found **5/8 exact matches** and **8/8 directionally correct calls**. 
- It successfully caught and corrected 3 technical nuances the agent missed (e.g., distinguishing between official and community-built MCP servers). 
- The exact corrections and accuracy metrics are logged in `verification_log.json`.

## File Guide

- `master_dataset.json`: The final, validated dataset containing the research for all 100 apps.
- `verification_log.json`: The accuracy check metrics and manual corrections applied to the dataset.
- `index.html`: The generated case study and statistical breakdown of the findings.
- `research_pipeline.py`: The consolidated agent research script.
- `apps.json`: The source list of 100 apps (name, category, website hint) used to build `master_dataset.json`.
- `archive/`: A directory containing the earlier iteration scripts, scratch files, and batch processing logic, kept for transparency and history.
