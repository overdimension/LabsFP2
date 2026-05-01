class EventEmitter:
    def __init__(self):
        self.handlers = {}

    def subscribe(self, event, callback):
        if event not in self.handlers:
            self.handlers[event] = []
        self.handlers[event].append(callback)

    def emit(self, event, data):
        for handler in self.handlers[event]:
            handler(data)