from renardo_reapy.errors import DisabledDistAPIError, UndefinedExtStateError
from renardo_reapy.tools import json
from urllib import request
from urllib.error import URLError

import renardo_reapy.runtime as runtime
import typing as ty


class WebInterface:
    _url: str
    ext_state: ExtState

    def __init__(self, port: int, host: str = 'localhost') -> None:
        ...

    def activate_reapy_server(self) -> None:
        ...

    def get_reapy_server_port(self) -> int:
        ...

    def perform_action(self, action_id: ty.Union[int, str, bytes]) -> None:
        ...


class ExtState:
    _url: str

    def __init__(self, web_interface: WebInterface) -> None:
        ...

    def __getitem__(self, key: str) -> int:
        ...

    def __setitem__(self, key: str, value: int) -> None:
        ...
