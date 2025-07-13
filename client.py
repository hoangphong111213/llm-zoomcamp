from fastmcp import Client
import asyncio

async def main():
    async with Client("agent.py") as mcp_client:
        tools = await mcp_client.list_tools()
        print("Available tools:")
        print(tools)

if __name__ == "__main__":
    asyncio.run(main())