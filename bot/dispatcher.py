from collections.abc import Callable

from bot.messenger import Messenger


class Dispatcher:
    def __init__(
        self,
        messenger: Messenger,
        handlers: list[Callable[[dict, Messenger], None]],
    ):
        self.messenger = messenger
        self.handlers = handlers

    def dispatch(self, update: dict) -> None:
        message = update.get("message")

        if not isinstance(message, dict):
            return

        for handler in self.handlers:
            handler(message, self.messenger)
