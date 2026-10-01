#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import NotRequired, Sequence, TypedDict

from .job import JobsResult, PrintResult

class Font(TypedDict):
    name: str
    style: NotRequired[str]
    data_b64: NotRequired[str]
    url: NotRequired[str]
    md5: NotRequired[str]

class NodeFont(TypedDict):
    name: str
    style: str
    md5: str
    url: NotRequired[str]
    size: int
    time: float
    active: bool

class Node(TypedDict):
    name: str
    mode: str
    location: NotRequired[str]
    node_printer: NotRequired[str]
    engines: Sequence[str]
    capabilities: NotRequired[Sequence[str]]
    fonts: NotRequired[Sequence[NodeFont]]

class NodeAPI:
    def list_nodes(self) -> Sequence[Node]: ...
    def jobs_node(self, id: str) -> JobsResult: ...
    def print_default_node(
        self,
        id: str,
        data: str | None = None,
        data_b64: str | None = None,
        name: str | None = None,
        type: str | None = None,
        format: str | None = None,
        options: dict | None = None,
        fonts: Sequence[Font] | None = None,
    ) -> PrintResult: ...
    def print_hello_default_node(
        self,
        id: str,
        type: str | None = None,
        format: str | None = None,
        options: dict | None = None,
    ) -> PrintResult: ...
    def print_printer_node(
        self,
        id: str,
        printer: str | None = None,
        data: str | None = None,
        data_b64: str | None = None,
        name: str | None = None,
        type: str | None = None,
        format: str | None = None,
        options: dict | None = None,
        fonts: Sequence[Font] | None = None,
    ) -> PrintResult: ...
    def print_hello_printer_node(
        self,
        id: str,
        printer: str | None = None,
        type: str | None = None,
        format: str | None = None,
        options: dict | None = None,
    ) -> PrintResult: ...
    def fonts_node(self, id: str) -> Sequence[NodeFont]: ...
    def install_fonts_node(
        self, id: str, fonts: Sequence[Font], name: str | None = None
    ) -> PrintResult: ...

def font_entry(name: str, path: str, style: str | None = None) -> Font: ...
