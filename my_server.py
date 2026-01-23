from fastmcp import FastMCP
from random import randint

mcp = FastMCP("My MCP Server")

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
