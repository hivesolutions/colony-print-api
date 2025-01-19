#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import colony_print


def get_api():
    return colony_print.API(key=appier.conf("PRINT_KEY"))
