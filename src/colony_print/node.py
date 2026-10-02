#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import base64
import hashlib


class NodeAPI(object):

    def list_nodes(self, *args, **kwargs):
        url = self.base_url + "nodes"
        contents = self.get(url, **kwargs)
        return contents

    def jobs_node(self, id):
        url = self.base_url + "nodes/%s/jobs" % id
        contents = self.get(url)
        return contents

    def print_default_node(
        self,
        id,
        data=None,
        data_b64=None,
        name=None,
        type=None,
        format=None,
        options=None,
        fonts=None,
    ):
        url = self.base_url + "nodes/%s/print" % id
        contents = self.post(
            url,
            params=dict(
                data=data,
                data_b64=data_b64,
                name=name,
                type=type,
                format=format,
                options=json.dumps(options) if options else None,
                fonts=json.dumps(fonts) if fonts else None,
            ),
        )
        return contents

    def print_hello_default_node(
        self,
        id,
        type=None,
        format=None,
        options=None,
    ):
        url = self.base_url + "nodes/%s/print_hello" % id
        contents = self.post(
            url,
            params=dict(
                type=type,
                format=format,
                options=json.dumps(options) if options else None,
            ),
        )
        return contents

    def print_printer_node(
        self,
        id,
        printer=None,
        data=None,
        data_b64=None,
        name=None,
        type=None,
        format=None,
        options=None,
        fonts=None,
    ):
        url = self.base_url + "nodes/%s/printers/print" % id
        contents = self.post(
            url,
            params=dict(
                printer=printer,
                data=data,
                data_b64=data_b64,
                name=name,
                type=type,
                format=format,
                options=json.dumps(options) if options else None,
                fonts=json.dumps(fonts) if fonts else None,
            ),
        )
        return contents

    def print_hello_printer_node(
        self, id, printer=None, type=None, format=None, options=None
    ):
        url = self.base_url + "nodes/%s/printers/print_hello" % id
        contents = self.post(
            url,
            params=dict(
                printer=printer,
                type=type,
                format=format,
                options=json.dumps(options) if options else None,
            ),
        )
        return contents

    def fonts_node(self, id):
        url = self.base_url + "nodes/%s/fonts" % id
        contents = self.get(url)
        return contents

    def install_fonts_node(self, id, fonts, name=None):
        url = self.base_url + "nodes/%s/fonts" % id
        contents = self.post(url, params=dict(fonts=json.dumps(fonts), name=name))
        return contents


def font_entry(name, path, style=None):
    """
    Builds the entry of a font to be sent with a print job (or to be
    installed in a node) from the font file of the provided path, with
    its data (base64 encoded) and its MD5, verified by the node.

    :type name: String
    :param name: The family name of the font, as used by the document
    and defined by the font file.
    :type path: String
    :param path: The path to the (true type) font file.
    :type style: String
    :param style: The style of the font (eg: bold), read from the font
    file by the node when not provided.
    :rtype: Dictionary
    :return: The entry of the font to be sent to the server.
    """

    with open(path, "rb") as file:
        data = file.read()
    font = dict(
        name=name,
        data_b64=base64.b64encode(data).decode("utf-8"),
        md5=hashlib.md5(data).hexdigest(),
    )
    if style:
        font["style"] = style
    return font


class Node(dict):
    pass


class NodeFont(dict):
    pass
