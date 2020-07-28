#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: api.py
# Created: Tuesday, 28th July 2020 12:31:21 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Tuesday, 28th July 2020 1:08:09 pm
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import sys
sys.dont_write_bytecode = True

from required import Request

class Quran:
    """
    quran.com api class

    Contains:
        get_recitations
    """
    def __init__(self):
        """
        Constructor class

        args

        returns
            None
        """
        self.base = "http://api.quran.com:3000/api/v3/"

        self.rq = Request()

    def get_recitations(self):
        """
        Get list of available Recitations.
        Use language query to get translated names of reciters in specific language(e.g language=ur will send translation names in Urdu).
        """
        self.recite_end = "options/recitations"
        self.obj = self.rq.get(f"{self.base}{self.recite_end}")
        return self.obj

    def get_translations(self):
        """
        Get list of available translations.
        """
        self.trans_end = "options/translations"
        self.obj = self.rq.get(f"{self.base}{self.trans_end}")
        return self.obj

    def get_languages(self, *lang):
        """
        Get all languages.
        You can get translated names of languages in specific language using language query parameter.
        For example:
            obj.get_languages(bn)
        will return language names translated into Bangla
        """
        self.language_end = "options/languages"
        self.uri = f"{self.base}{self.language_end}"
        if lang:
            self.obj = self.rq.get(self.uri, lang[0])
            return self.obj
        self.obj = self.rq.get(self.uri)
        return self.obj

    def get_tafsirs(self):
        self.tafsir_end = "options/tafsirs"
        self.obj = self.rq.get(f"{self.base}{self.tafsir_end}")
        return self.obj

    def get_chapters(self):
        return self.rq.get(f"{self.base}chapters")

# Test
if __name__ == "__main__":
    quran = Quran()
    # res = quran.get_recitations()
    # res = quran.get_translations()
    # res = quran.get_languages('ur')
    # res = quran.get_tafsirs()
    res = quran.get_chapters()

    print(res)
