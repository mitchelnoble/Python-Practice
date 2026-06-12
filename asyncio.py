#Python deals with asynchronous programming using the asyncio library that introduces the async and await keywords.

#Fetching Data
import asyncio
import aiohttp

async def fetch_data():
  async with aiohttp.ClientSession() as session:
    async with session.get('https://api.example.com/data') as response:
      data = await response.json()
      print(data)

asyncio.run(fetch_data())

#explicitly defines asynchronous functions with "async def"
#asyncio library is required to run the event loop
#is more structured but requires more setup compared to javascript

#asynchronous programming is suitible for tasks that involve waiting such as: network requests, file I/O, or database queries.
#Python's asynchronous model excels at handling I/O based tasks such as file processing, web scraping, or data base queries.

