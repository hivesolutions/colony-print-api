#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import NotRequired, Sequence, TypedDict

class Node(TypedDict):
    name: str
    mode: str
    location: NotRequired[str]
    node_printer: NotRequired[str]
    engines: Sequence[str]

class NodeAPI:
    def list_nodes(self) -> Sequence[Node]: ...
