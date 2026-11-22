from collections.abc import Iterator

from bot.messenger import Messenger


def long_polling(messenger: Messenger) -> Iterator[dict]:
    offset = 0

    while True:
        updates = messenger.get_updates(offset=offset, timeout=30)

        for update in updates:
            offset = max(offset, update["update_id"] + 1)
            yield update
