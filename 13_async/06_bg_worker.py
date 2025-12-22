import threading
import asyncio
import time

def bg_worker():
    while True:
        time.sleep(1)
        print("system health is logging 💉")

async def fetch_orders():
    await asyncio.sleep(3)
    print("order fetched 🎁")

threading.Thread(target=bg_worker,daemon=True).start()
threading.Thread(target=bg_worker,daemon=True).join()


asyncio.run(fetch_orders())