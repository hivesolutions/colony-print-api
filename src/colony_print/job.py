#!/usr/bin/python
# -*- coding: utf-8 -*-


class JobAPI(object):

    def list_jobs(self, *args, **kwargs):
        url = self.base_url + "jobs"
        contents = self.get(url, **kwargs)
        return contents

    def get_job(self, id):
        url = self.base_url + "jobs/%s" % id
        contents = self.get(url)
        return contents


class JobInfo(dict):
    pass


class JobsResult(dict):
    pass


class PrintResult(dict):
    pass
