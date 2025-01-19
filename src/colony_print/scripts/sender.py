#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

import appier
import colony_print


def send(*args, **kwargs):
    api = colony_print.API()
    return api.send(kwargs)


if __name__ == "__main__":
    receivers = appier.conf("RECEIVERS", [], cast=list)
    subject = appier.conf("SUBJECT", None)
    title = appier.conf("TITLE", None)
    contents = appier.conf("CONTENTS", None)
    copyright = appier.conf("COPYRIGHT", None)

    kwargs = dict()
    if receivers:
        kwargs["receivers"] = receivers
    if subject:
        kwargs["subject"] = subject
    if title:
        kwargs["title"] = title
    if contents:
        kwargs["contents"] = contents
    if copyright:
        kwargs["copyright"] = copyright

    result = send(**kwargs)
    pprint.pprint(result)
else:
    __path__ = []
