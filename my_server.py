from fastmcp import FastMCP
from fastmcp.tools import tool

class Calculator:
    def __init__(self, multiplier: int, divider: int ):
        self.multiplier = multiplier
        self.divider = divider

    @tool()
    def multiply(self, x: int) -> int:
        """Multiply x by the instance multiplier."""
        return x * self.multiplier

    @tool()
    def divide(self, x: int) -> int:
        """Divide x by the instance divider."""
        return x / self.divider

calc = Calculator(multiplier=3,divider=3)
mcp = FastMCP()
mcp.add_tool(calc.multiply)     # Registers with correct schema (only 'x', not 'self')
mcp.add_tool(calc.divide)       # Registers with correct schema (only 'x', not 'self')
