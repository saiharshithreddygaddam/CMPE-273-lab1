import asyncio
import aiohttp
# Incomplete code
@asyncio.coroutine
def getData():
    
    r = yield from aiohttp.request(
        'GET', 'https://webhook.site/a3f70ce9-99a8-434f-a4fe-3ef1a24d350f')
    return r

loop = asyncio.get_event_loop()
loop.run_until_complete(getData())
