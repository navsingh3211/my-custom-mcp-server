import random
from fastmcp import FastMCP

mcp = FastMCP(name="Demo server")

#Decorator
@mcp.tool
def roll_dice(n_dice:int=1)->list[int]:
    """Rolls n_dice 6-sided dice and returns the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool
def add_numbers(a:float, b:float)->float:
    """Adds two numbers and returns the result."""
    return a + b


if __name__ == "__main__":
    mcp.run()
