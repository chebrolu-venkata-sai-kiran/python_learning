import asyncio
import time

async def brew(name):
    print(f"brewing {name} chai ...")
    await asyncio.sleep(1)
    print(f"{name} chai brewed!")

async def main():
    await asyncio.gather(
        brew("green"),
        brew("black"),
        brew("white"),
    )

asyncio.run(main())