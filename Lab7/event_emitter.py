import asyncio

class EventEmitter:
    def __init__(self):
        self.handlers = {}

    def subscribe(self, event, callback):
        if event not in self.handlers:
            self.handlers[event] = []
        self.handlers[event].append(callback)

        return lambda: self.handlers[event].remove(callback)

    async def emit(self, event, data):
        if event not in self.handlers:
            if event == "error": 
                print(f"CRITICAL: Unhandled error event: {data}")
            return

        for handler in self.handlers[event]:
            try:
                if asyncio.iscoroutinefunction(handler):
                    await handler(data)
                else:
                    handler(data)
            except Exception as e:
                if event != "error":
                    await self.emit("error", f"Failure in {event}: {e}")