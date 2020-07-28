#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: required.py
# Created: Tuesday, 28th July 2020 12:34:09 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Tuesday, 28th July 2020 8:32:09 pm
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import requests

class Request:
    def __init__(self):
        self.headers = {'content-type': "application/json"}
        self.payload = {}

    def get(self, uri, *args, **kwargs):
        if args:
            if kwargs and kwargs['header']:
                self.headers['X-API-Key'] = 'SqD712P3E82xnwOAEOkGd5JZH8s9wRR24TqNFzjk' or kwargs['x_api_key']
                self.res = requests.get(uri, params=args[0], headers=self.headers)
            self.res = requests.get(uri, params=args[0], headers=self.headers)
            self.obj = self.res.json()
            return self.obj
        self.res = requests.get(uri)
        self.obj = self.res.json()
        return self.obj
