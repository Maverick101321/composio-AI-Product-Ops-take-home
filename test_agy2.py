import asyncio
from google.antigravity import Agent, LocalAgentConfig

async def main():
    try:
        async with Agent(LocalAgentConfig()) as agent:
            response = await agent.chat("Are you working?")
            print(await response.text())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
