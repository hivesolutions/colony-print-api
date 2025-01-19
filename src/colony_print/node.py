#!/usr/bin/python
# -*- coding: utf-8 -*-


class NodeAPI(object):

    def list_nodes(self, *args, **kwargs):
        url = self.base_url + "nodes"
        contents = self.get(url, **kwargs)
        return contents


class Node(dict):
    pass
