from unittest.mock import Mock

from bot.handlers.echo import echo_handler


def test_echo_text():
    messenger = Mock()
    message = {
        "text": "Привет!",
        "chat": {"id": 123},
    }

    echo_handler(message, messenger)

    messenger.send_message.assert_called_once_with(
        chat_id=123,
        text="Привет!",
    )


def test_ignore_photo():
    messenger = Mock()
    message = {
        "photo": [{"file_id": "123"}],
        "chat": {"id": 123},
    }

    echo_handler(message, messenger)

    messenger.send_message.assert_not_called()


def test_ignore_sticker():
    messenger = Mock()
    message = {
        "sticker": {"file_id": "456"},
        "chat": {"id": 123},
    }

    echo_handler(message, messenger)

    messenger.send_message.assert_not_called()
