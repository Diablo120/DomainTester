import aiohttp
import asyncio

my_file = open("Domain.txt")
l = (my_file.readlines())
l = [line.rstrip() for line in l]

async def fetch(client):
    async with client.get('https://' + l.pop(i)) as resp:
        assert resp.status == 200
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as client:
        html = await fetch(client)
        print('https://' + l.pop(i))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())