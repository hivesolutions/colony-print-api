#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import colony_print


class BaseTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(1 + 1, 2)

    def test_base_url(self):
        api = colony_print.API()
        api.get = lambda url, **kwargs: url
        self.assertEqual(api.base_url, "https://print.bemisc.com/")
        self.assertEqual(api.ping(), "https://print.bemisc.com/ping")
