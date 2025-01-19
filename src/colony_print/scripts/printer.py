#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

import appier
import colony_print


def print(id, printer=None):
    api = colony_print.API()
    if printer:
        return api.print_hello_printer_node(id, printer)
    else:
        return api.print_hello_default_node(id)


if __name__ == "__main__":
    node = appier.conf("NODE", None)
    printer = appier.conf("PRINTER", None)

    if not node:
        raise appier.OperationalError(message="No node defined")

    result = print(node, printer=printer)
    pprint.pprint(result)
else:
    __path__ = []
