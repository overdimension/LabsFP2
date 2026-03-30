import asyncio

#Callback
def sync_map(func, iterable):
    return [func(x) for x in iterable]
#Async
