#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import base64
import shutil
import hashlib
import tempfile
import unittest

import colony_print


class NodeAPITest(unittest.TestCase):

    def setUp(self):
        self.api = colony_print.API(base_url="https://print.hive.pt/api/")
        self.api.get = lambda url, **kwargs: self._request("GET", url, **kwargs)
        self.api.post = lambda url, **kwargs: self._request("POST", url, **kwargs)
        self.requests = []
        self.target_dir = tempfile.mkdtemp(prefix="colony-print-api-test-")

    def tearDown(self):
        shutil.rmtree(self.target_dir, ignore_errors=True)

    def _request(self, method, url, **kwargs):
        self.requests.append((method, url, kwargs))
        return dict(result="success")

    def test_print_default_node(self):
        fonts = [
            dict(name="Colonia", url="https://fonts.hive.pt/colonia.ttf"),
            dict(name="Binaria", style="bold", md5="a" * 32),
        ]
        result = self.api.print_default_node(
            "node", data_b64="QUJD", format="binie", fonts=fonts
        )
        self.assertEqual(result, dict(result="success"))
        method, url, kwargs = self.requests[0]
        self.assertEqual(method, "POST")
        self.assertEqual(url, "https://print.hive.pt/api/nodes/node/print")
        self.assertEqual(json.loads(kwargs["params"]["fonts"]), fonts)
        self.assertEqual(kwargs["params"]["data_b64"], "QUJD")
        self.assertEqual(kwargs["params"]["format"], "binie")
        self.assertEqual(kwargs["params"]["options"], None)

        self.api.print_default_node("node", data_b64="QUJD")
        _method, _url, kwargs = self.requests[1]
        self.assertEqual(kwargs["params"]["fonts"], None)

        self.api.print_default_node("node", data_b64="QUJD", fonts=[])
        _method, _url, kwargs = self.requests[2]
        self.assertEqual(kwargs["params"]["fonts"], None)

    def test_print_printer_node(self):
        fonts = [dict(name="Colonia", data_b64="QUJD")]
        self.api.print_printer_node(
            "node",
            printer="receipt",
            data="<printing_document/>",
            format="xmpl",
            fonts=fonts,
        )
        method, url, kwargs = self.requests[0]
        self.assertEqual(method, "POST")
        self.assertEqual(url, "https://print.hive.pt/api/nodes/node/printers/print")
        self.assertEqual(kwargs["params"]["printer"], "receipt")
        self.assertEqual(kwargs["params"]["format"], "xmpl")
        self.assertEqual(json.loads(kwargs["params"]["fonts"]), fonts)

        self.api.print_printer_node("node", printer="receipt", data_b64="QUJD")
        _method, _url, kwargs = self.requests[1]
        self.assertEqual(kwargs["params"]["fonts"], None)

    def test_fonts_node(self):
        result = self.api.fonts_node("node")
        self.assertEqual(result, dict(result="success"))
        self.assertEqual(
            self.requests, [("GET", "https://print.hive.pt/api/nodes/node/fonts", {})]
        )

    def test_install_fonts_node(self):
        fonts = [dict(name="Colonia", url="https://fonts.hive.pt/colonia.ttf")]
        result = self.api.install_fonts_node("node", fonts)
        self.assertEqual(result, dict(result="success"))
        method, url, kwargs = self.requests[0]
        self.assertEqual(method, "POST")
        self.assertEqual(url, "https://print.hive.pt/api/nodes/node/fonts")
        self.assertEqual(json.loads(kwargs["params"]["fonts"]), fonts)
        self.assertEqual(kwargs["params"]["name"], None)

        self.api.install_fonts_node("node", fonts, name="label fonts")
        _method, _url, kwargs = self.requests[1]
        self.assertEqual(kwargs["params"]["name"], "label fonts")

    def test_font_entry(self):
        data = b"\x00\x01\x00\x00font file"
        path = os.path.join(self.target_dir, "colonia.ttf")
        with open(path, "wb") as file:
            file.write(data)

        font = colony_print.font_entry("Colonia", path)
        self.assertEqual(sorted(font.keys()), ["data_b64", "md5", "name"])
        self.assertEqual(font["name"], "Colonia")
        self.assertEqual(base64.b64decode(font["data_b64"]), data)
        self.assertEqual(font["md5"], hashlib.md5(data).hexdigest())
        self.assertEqual(json.loads(json.dumps(font)), font)

        font = colony_print.font_entry("Colonia", path, style="bold")
        self.assertEqual(font["style"], "bold")

        self.assertRaises(
            IOError,
            lambda: colony_print.font_entry(
                "Colonia", os.path.join(self.target_dir, "missing.ttf")
            ),
        )
