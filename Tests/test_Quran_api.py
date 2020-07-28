#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: test_Quran_api.py
# Created: Tuesday, 28th July 2020 3:24:47 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Wednesday, 29th July 2020 1:27:22 am
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import requests as rq

from quran import Quran

# res = quran.get_recitations()
# res = quran.get_translations()
# res = quran.get_languages(language='ur')
# res = quran.get_tafsirs()
# res = quran.get_chapters(6, language="ur")
# res = quran.get_verses(6, recitation=1, translations=21, language="en", text_type="words")
# res = quran.get_verse(6, 6)
# res = quran.get_juzs()

qur = Quran()

def test_get_recitations():
    assert qur.get_recitations() == rq.get(
        "http://api.quran.com:3000/api/v3/options/recitations").json()

def test_get_translations():
    assert qur.get_translations() == rq.get(
        "http://api.quran.com:3000/api/v3/options/translations").json()

def test_get_languages():
    assert qur.get_languages(language='ur') == rq.get(
        "http://api.quran.com:3000/api/v3/options/languages?language=bn").json()

def test_get_tafsirs():
    assert qur.get_tafsirs() == rq.get(
        "http://api.quran.com:3000/api/v3/options/tafsirs").json()

def test_get_chapter():
    assert qur.get_chapter(1, language="en") == rq.get(
        "http://api.quran.com:3000/api/v3/chapters/1?language=en").json()

def test_get_chapters():
    qur.get_chapter(language="en") # == rq.get(
    #     "http://api.quran.com:3000/api/v3/chapters?language=en").json()

def test_get_chapter_info():
    assert qur.get_chapter(1, info=True, language="en") == rq.get(
        "http://api.quran.com:3000/api/v3/chapters/1/info?language=en").json()

def test_get_verses():
    assert qur.get_verses(1, text_type="words") == rq.get(
        "http://api.quran.com:3000/api/v3/chapters/1/verses?text_type=words").json()

def test_get_verse():
    assert qur.get_verse(chapter_id=1, verse_id=1) == rq.get(
        "http://api.quran.com:3000/api/v3/chapters/1/verses/1").json()

def test_get_juzs():
    assert qur.get_juzs() == rq.get(
        "http://api.quran.com:3000/api/v3/juzs").json()

def test_get_tafsirs_from_verse_id():
    assert qur.get_tafsirs_from_verse_id(chapter_id=1, verse_id=1) == rq.get(
        "http://api.quran.com:3000/api/v3/chapters/1/verses/1/tafsirs").json()

def test_get_tafsir_from_verse_id():
    assert qur.get_tafsir_from_verse_id(chapter_id=1, verse_id=1, tafsirs="ar_baghawy") == rq.get(
        "http://api.quran.com:3000/api/v3/chapters/1/verses/1/tafsirs?tafsirs=ar_baghawy").json()

def test_search():
    assert qur.search(q="imran", size=20, page=0, language="en") == rq.get(
        "http://api.quran.com:3000/api/v3/search?q=imran&size=20&page=0&language=en").json()


print(test_get_chapters())
