from schemas.context import AirlineContext


class ConversationContext:
    def __init__(self):
        self.context = AirlineContext()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self.context, key):
                setattr(self.context, key, value)

    def get(self) -> AirlineContext:
        return self.context