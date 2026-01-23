from fastmcp import FastMCP
from random import randint
import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = "hallosabuj"
GITHUB_REPO = "mcp-server"

mcp = FastMCP("github-automation")

# -----------------------------
# TOOL: Create GitHub Issue
# -----------------------------
@mcp.tool(
    name="create_github_issue",
    description="Create a GitHub issue in a repository"
)
def create_github_issue(
    title: str,
    body: str,
    labels: list[str] | None = None
) -> str:
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/issues"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    payload = {
        "title": title,
        "body": body,
        "labels": labels or []
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 201:
        raise RuntimeError(
            f"GitHub API error: {response.status_code} {response.text}"
        )

    issue_url = response.json()["html_url"]
    return f"Issue created successfully: {issue_url}"


# ---------------------------------
# PROMPT: Decide issue creation
# ---------------------------------
@mcp.prompt(
    name="github_issue_creator",
    description="Decide issue title, body, and labels, then create a GitHub issue"
)
def github_issue_prompt(context: str) -> str:
    return f"""
You are an automation agent connected to a GitHub repository.

Your task:
1. Decide whether a GitHub issue should be created.
2. If yes, decide:
   - title (short and clear)
   - body (detailed description)
   - labels (bug, enhancement, docs, etc.)

When ready, call the tool:
create_github_issue(title, body, labels)

Context:
{context}
"""

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}! I am calculator"

@mcp.tool
def multiplier(x:int) -> int:
    return randint(1,10)*x

@mcp.tool
def divider(x:int) -> int:
    return x/randint(1,10)

if __name__ == "__main__":
    mcp.run()
