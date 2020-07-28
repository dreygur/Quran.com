#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: test_Quran_api.py
# Created: Tuesday, 28th July 2020 3:24:47 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Tuesday, 28th July 2020 3:40:17 pm
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
