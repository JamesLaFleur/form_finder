import json
import typing
from email.message import Message

class Response(typing.NamedTuple):
    body: str
    headers: Message
    status: int
    error_count: int = 0

    def json(self) -> typing.Any:
        """
        Конвертирует тело response в JSON
        """
        try:
            output = json.loads(self.body)
        except json.JSONDecodeError:
            output = ""
        return output