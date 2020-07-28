#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: Sunnah_api.py
# Created: Tuesday, 28th July 2020 8:07:54 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Wednesday, 29th July 2020 1:43:15 am
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import quran as q
from typing import Dict

class Sunnah:
    """
    sunnah.com api class

    Contains:
        get_recitations
    """

    def __init__(self) -> None:
        """
        Constructor class

        args
            None

        returns
            None
        """
        self.base: str = "https://api.sunnah.com/v1/"
        self.rq: str = q.Request()

    def get_root(self):
        return self.rq.get(f"{self.base}", header=True)

    def get_collections(self, **kwargs):
        return self.rq.get(f"{self.base}collections", kwargs, header=True)

    def get_collections_by_name(self, name, **kwargs):
        if not name:
            raise q.CollectionNameNotFound
        return self.rq.get(f"{self.base}collections/{name}", kwargs, header=True)

    def get_list_chapters(self, name, id, **kwargs):
        if not name or not id:
            raise q.CollectionNameOrIdNotFound
        return self.rq.get(f"{self.base}collections/{name}/books/{id}/chapters", kwargs, header=True)

    def get_list_hadith(self, name, id, **kwargs):
        if not name or not id:
            raise q.CollectionNameOrIdNotFound
        return self.rq.get(f"{self.base}collections/{name}/books/{id}/hadiths", kwargs, header=True)

    def get_hadith(self, name, id, **kwargs):
        if not name or not id:
            raise q.CollectionNameOrIdNotFound
        return self.rq.get(f"{self.base}collections/{name}/hadiths/{id}", kwargs, header=True)

    def get_random_hadith(self):
        return self.rq.get(f"{self.base}hadiths/random", header=True)

    def get_book(self, name, id):
        if not name and id:
            raise q.CollectionNameOrIdNotFound
        return self.rq.get(f"{self.base}collections/{name}/books/{id}", header=True)

    def get_books(self, name, **kwargs):
        if not name:
            raise q.CollectionNameNotFound
        return self.rq.get(f"{self.base}collections/{name}/books", kwargs, header=True)
