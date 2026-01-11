class SessionMemory:
    def __init__(self):
        self.last_product = None
        self.history = []

    def add(self, user, assistant):
        self.history.append({"user": user, "assistant": assistant})
        if len(self.history) > 6:
            self.history.pop(0)

session = SessionMemory()
