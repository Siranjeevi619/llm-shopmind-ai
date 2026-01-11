class SessionState:
    def __init__(self):
        self.last_product = None
        self.last_intent = None
        self.last_message = None

    def reset(self):
        self.last_product = None
        self.last_intent = None
        self.last_message = None


session = SessionState()
