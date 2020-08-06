#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: Sunnah_api.py
# Created: Tuesday, 28th July 2020 8:07:54 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Thursday, 6th August 2020 12:41:23 pm
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import quran as q
from typing import Dict

class Sunnah:
    """
    sunnah.com api class

    Methods:
        get_root
        get_collections
        get_collections_by_name
        get_list_chapters
        get_list_hadith
        get_hadith
        get_random_hadith
        get_book
        get_books
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

    def get_root(self) -> Dict:
        """
        Returns the root of sunnah.com api

        args:
            None

        return
            json Object
        """
        return self.rq.get(f"{self.base}", header=True)

    def get_collections(self, **kwargs) -> Dict:
        """
        Paginated list of available collections

        args:
            limit   Maximum number of items
            page    Offset for pagination

        returns:
            json Object
        """
        return self.rq.get(f"{self.base}collections", kwargs, header=True)

    def get_collections_by_name(self, name, **kwargs) -> Dict:
        """
        Paginated list of available collections by name

        args:
            name    Name of the collection(Bukhari, Muslim etc)
            limit   Maximum number of items
            page    Offset for pagination

        returns:
            json Object
        """
        if not name:
            raise q.CollectionNameNotFound
        return self.rq.get(f"{self.base}collections/{name}", kwargs, header=True)

    def get_list_chapters(self, name, id, **kwargs) -> Dict:
        """
        Get the list of chapters of a book for a collection

        args:
        """
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
