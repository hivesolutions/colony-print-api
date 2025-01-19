#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Mapping, TypedDict

class JobInfo(TypedDict):
    name: str
    node_id: str
    printer: str | None
    status: str | None

JobsResult = Mapping[str, JobInfo]
