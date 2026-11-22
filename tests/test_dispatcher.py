from unittest.mock import Mock

from bot.dispatcher import Dispatcher


def test_dispatch_message():
    messenger = Mock()
    handler = Mock()
    dispatcher = Dispatcher(messenger, [handler])

    message = {
        "text": "Привет!",
        "chat": {"id": 123},
    }

    dispatcher.dispatch({"message": message})

    handler.assert_called_once_with(message, messenger)


def test_ignore_unknown_update():
    messenger = Mock()
    handler = Mock()
    dispatcher = Dispatcher(messenger, [handler])

    dispatcher.dispatch({"edited_message": {"text": "Изменённое сообщение"}})

    handler.assert_not_called()


def test_multiple_handlers():
    messenger = Mock()
    first_handler = Mock()
    second_handler = Mock()

    dispatcher = Dispatcher(
        messenger,
        [first_handler, second_handler],
    )

    message = {
        "text": "Тест",
        "chat": {"id": 456},
    }

    dispatcher.dispatch({"message": message})

    first_handler.assert_called_once_with(message, messenger)
    second_handler.assert_called_once_with(message, messenger)
