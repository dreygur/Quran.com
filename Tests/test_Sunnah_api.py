#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: test_Sunnah_api.py
# Created: Tuesday, 28th July 2020 8:24:41 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Wednesday, 29th July 2020 1:42:14 am
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import requests as rq
from quran import Sunnah

s = Sunnah()

headers = {
    'content-type': "application/json",
    'X-API-Key': 'SqD712P3E82xnwOAEOkGd5JZH8s9wRR24TqNFzjk'
    }

def test_get_root():
    assert s.get_root() == rq.get(
        "https://api.sunnah.com/v1/", headers=headers).json()

def test_get_collections():
    assert s.get_collections(limit=50, page=1) == rq.get(
        "https://api.sunnah.com/v1/collections?limit=50&page=1", headers=headers).json()

def test_get_collections_by_name():
    assert s.get_collections_by_name("bukhari", limit=50, page=1) == rq.get(
        "https://api.sunnah.com/v1/collections/bukhari?limit=50&page=1", headers=headers).json()

def test_get_list_chapters():
    assert s.get_list_chapters("bukhari", 1, limit=50, page=1) == rq.get(
        " https://api.sunnah.com/v1/collections/bukhari/books/1/chapters?limit=50&page=1", headers=headers).json()

def test_get_list_hadith():
    assert s.get_list_hadith("bukhari", 1, lang="en", limit=50, page=1) == rq.get(
        "https://api.sunnah.com/v1/collections/bukhari/books/1/hadiths?limit=50&page=1&lang=en", headers=headers).json()

def test_get_hadith():
    assert s.get_hadith("bukhari", 1) == rq.get(
        "https://api.sunnah.com/v1/collections/bukhari/hadiths/1", headers=headers).json()

def test_get_random_hadith():
    assert type(s.get_random_hadith()) is type(rq.get(
        "https://api.sunnah.com/v1/hadiths/random", headers=headers).json())

def test_get_book():
    print(s.get_book("bukhari", 1)) #== rq.get(
    #    "https://api.sunnah.com/v1/collections/bukhari/books/1", headers=headers).json()

def test_get_books():
    assert s.get_books("bukhari") == rq.get(
        "https://api.sunnah.com/v1/collections/bukhari/books?limit=50&page=1", headers=headers).json()

test_get_book()