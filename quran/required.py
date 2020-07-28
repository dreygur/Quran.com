#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: required.py
# Created: Tuesday, 28th July 2020 12:34:09 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Tuesday, 28th July 2020 1:03:25 pm
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import requests

class Request:
    def __init__(self):
        self.headers = {'content-type': "application/json"}
        self.payload = {}
    def get(self, uri, *body):
        if body:
            self.res = requests.get(uri, params={body[0]})
            self.obj = self.res.json()
            return self.obj
        self.res = requests.get(uri)
        self.obj = self.res.json()
        return self.obj
