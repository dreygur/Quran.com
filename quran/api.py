#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: api.py
# Created: Tuesday, 28th July 2020 12:31:21 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Tuesday, 28th July 2020 1:19:33 pm
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
        return self.rq.get(f"{self.base}options/recitations")

    def get_translations(self):
        """
        Get list of available translations.
        """
        return self.rq.get(f"{self.base}options/translations")

    def get_languages(self, **lang):
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
            return self.rq.get(self.uri, lang["language"])
        return self.rq.get(self.uri)

    def get_tafsirs(self):
        return self.rq.get(f"{self.base}options/tafsirs")

    def get_chapters(self, *id, **lang):
        """
        Get list of chapters. Use language query to get translated names of chapters in specific language
        (e.g language=bn will send translation names in Bangla).

        args:
            language  Target Language
        """
        if id:
            if lang:
                return self.rq.get(f"{self.base}chapters/{id[0]}", lang["language"])
            return self.rq.get(f"{self.base}chapters/{id[0]}")

        if lang:
            return self.rq.get(f"{self.base}chapters", lang["language"])

        return self.rq.get(f"{self.base}chapters")

# Test
if __name__ == "__main__":
    quran = Quran()
    # res = quran.get_recitations()
    # res = quran.get_translations()
    # res = quran.get_languages(language='ur')
    # res = quran.get_tafsirs()
    res = quran.get_chapters(6)

    print(res)
