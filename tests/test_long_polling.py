from unittest.mock import Mock, call

from bot.long_polling import long_polling


def test_get_updates():
    messenger = Mock()
    update = {"update_id": 1, "message": {"text": "Привет"}}
    messenger.get_updates.return_value = [update]

    polling = long_polling(messenger)
    result = next(polling)

    assert result == update
    messenger.get_updates.assert_called_once_with(
        offset=0,
        timeout=30,
    )


def test_offset():
    messenger = Mock()
    messenger.get_updates.side_effect = [
        [{"update_id": 5}],
        [{"update_id": 6}],
    ]

    polling = long_polling(messenger)

    next(polling)
    next(polling)

    assert messenger.get_updates.call_args_list == [
        call(offset=0, timeout=30),
        call(offset=6, timeout=30),
    ]


def test_empty_updates():
    messenger = Mock()
    messenger.get_updates.side_effect = [
        [],
        [{"update_id": 10}],
    ]

    polling = long_polling(messenger)
    result = next(polling)

    assert result["update_id"] == 10
    assert messenger.get_updates.call_count == 2
