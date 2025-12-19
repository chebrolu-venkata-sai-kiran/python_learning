import asyncio
import aiohttp

async def fetch_url(session,url):
    async with session.get(url) as response:
        print(f"Feteched {url} with status {response.status}")
        return await response.text()
    
async def main():
    urls = ["https://www.example.com", "https://www.google.com", "https://www.wikipedia.org"]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
       # print(responses)

asyncio.run(main()) 