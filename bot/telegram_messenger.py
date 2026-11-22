import json
import urllib.parse
import urllib.request


class TelegramMessenger:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url.rstrip("/")

    def _request(self, method: str, **params):
        url = f"{self.base_url}/bot{self.token}/{method}"

        request = urllib.request.Request(
            url,
            data=urllib.parse.urlencode(params).encode(),
            method="POST",
        )

        with urllib.request.urlopen(request, timeout=40) as response:
            payload = json.loads(response.read())

        if not payload["ok"]:
            raise RuntimeError(payload.get("description", "Telegram API error"))

        return payload["result"]

    def get_updates(
        self,
        offset: int,
        timeout: int = 30,
    ) -> list[dict]:
        return self._request(
            "getUpdates",
            offset=offset,
            timeout=timeout,
            limit=100,
            allowed_updates=json.dumps(["message"]),
        )

    def send_message(
        self,
        chat_id: int,
        text: str,
    ) -> None:
        self._request(
            "sendMessage",
            chat_id=chat_id,
            text=text,
        )
