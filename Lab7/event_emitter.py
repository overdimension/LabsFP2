class EventEmitter:
    def __init__(self):
        self.handlers = {}

    def subscribe(self, event, callback):
        if event not in self.handlers:
            self.handlers[event] = []
        self.handlers[event].append(callback)

        return lambda: self.handlers[event].remove(callback)

    def emit(self, event, data):
        if event not in self.handlers:
            return

        for handler in self.handlers[event]:
            handler(data)