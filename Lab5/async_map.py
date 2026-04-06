import asyncio

#Callback
def async_map_callback(iterable, func, callback):
    result = []
    for item in iterable:
        result.append(func(item))
    callback(result)

#Async
async def async_map(iterable, func):
    tasks = [asyncio.create_task(func(x)) for x in iterable]
    return await asyncio.gather(*tasks)

#Abort
async def async_map_with_abort(iterable, func, abort_event: asyncio.Event):
    tasks = [asyncio.create_task(func(x)) for x in iterable]

    while not all(t.done() for t in tasks):
        if abort_event.is_set():
            for t in tasks:
                t.cancel()
            print("Mapping aborted!")
            return None
        await asyncio.sleep(0.05)

    results = []
    for t in tasks:
        try:
            results.append(await t)
        except asyncio.CancelledError:
            results.append(None)
    return results