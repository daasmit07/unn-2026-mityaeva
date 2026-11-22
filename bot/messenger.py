from typing import Protocol


class Messenger(Protocol):
    def get_updates(
        self,
        offset: int,
        timeout: int = 30,
    ) -> list[dict]: ...

    def send_message(
        self,
        chat_id: int,
        text: str,
    ) -> None: ...
