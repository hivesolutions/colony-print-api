from typing import TypedDict
from appier import API as BaseAPI

from .node import NodeAPI

BASE_URL: str = ...

class Ping(TypedDict):
    time: float

class API(BaseAPI, NodeAPI):
    def ping(self) -> Ping: ...
