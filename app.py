#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: app.py
# Created: Tuesday, 28th July 2020 2:16:58 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Tuesday, 28th July 2020 8:30:49 pm
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

# from quran import Quran

# q = Quran()
# # res = q.get_juzs()
# # res = q.get_verse(6, 6)
# res = q.get_chapter(6, info=True, language="ur")
# print(res)

from quran import Sunnah

s = Sunnah()
res = s.collections(limit=50, page=1)
print(res)
