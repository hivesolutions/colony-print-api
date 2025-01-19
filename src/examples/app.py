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

    @appier.route("/send", "GET")
    def send(self):
        receivers = self.field("receivers", [], cast=list)
        subject = self.field("subject", "Test email")
        title = self.field("title", "Test email")
        contents = self.field("contents", "Test email")
        copyright = self.field("copyright", "Hive Solutions")
        payload = dict(
            receivers=receivers,
            subject=subject,
            title=title,
            contents=contents,
            copyright=copyright,
        )
        api = self.get_api()
        result = api.send(payload)
        return result

    def get_api(self):
        api = base.get_api()
        return api


if __name__ == "__main__":
    app = ColonyPrintApp()
    app.serve()
else:
    __path__ = []
