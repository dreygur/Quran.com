#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: exceptions.py
# Created: Tuesday, 28th July 2020 4:33:53 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Wednesday, 29th July 2020 12:11:31 am
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

class LanguageNotAvailable(Exception):
    pass

class ChapterNumberNotFound(Exception):
    pass

class CollectionNameNotFound(Exception):
    pass

class CollectionNameOrIdNotFound(Exception):
    pass