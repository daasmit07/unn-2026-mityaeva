import os

from dotenv import load_dotenv

from bot.dispatcher import Dispatcher
from bot.handlers.echo import echo_handler
from bot.long_polling import long_polling
from bot.telegram_messenger import TelegramMessenger


def main() -> None:
    load_dotenv()

    messenger = TelegramMessenger(
        token=os.environ["TELEGRAM_TOKEN"],
        base_url=os.environ["TELEGRAM_BASE_URL"],
    )

    dispatcher = Dispatcher(
        messenger=messenger,
        handlers=[echo_handler],
    )

    print("Бот запущен")

    for update in long_polling(messenger):
        dispatcher.dispatch(update)


if __name__ == "__main__":
    main()
