#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base


class ColonyPrintApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(self, name="colony_print", *args, **kwargs)

    @appier.route("/", "GET")
    def index(self):
        return self.ping()

    @appier.route("/ping", "GET")
    def ping(self):
        api = self.get_api()
        result = api.ping()
        return result

    @appier.route("/nodes", "GET")
    def nodes(self):
        api = self.get_api()
        result = api.list_nodes()
        return result

    def get_api(self):
        api = base.get_api()
        return api


if __name__ == "__main__":
    app = ColonyPrintApp()
    app.serve()
else:
    __path__ = []
