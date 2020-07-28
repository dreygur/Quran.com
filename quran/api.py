#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: api.py
# Created: Tuesday, 28th July 2020 12:31:21 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Tuesday, 28th July 2020 3:18:14 pm
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import sys
sys.dont_write_bytecode = True

from .required import Request

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

    def get_chapter(self, *args, **kwargs):
        """
        Get list of chapter. Use language query to get translated names of chapter in specific language
        (e.g language=bn will send translation names in Bangla).

        args:
            language  Target Language
        """
        if id:
            if kwargs:
                if kwargs.get("info") and kwargs.get("language"):
                    return self.rq.get(f"{self.base}chapters/{args[0]}/info", kwargs.get("language"))
                elif kwargs.get("info"):
                    return self.rq.get(f"{self.base}chapters/{args[0]}/info")
                elif kwargs.get("language"):
                    return self.rq.get(f"{self.base}chapters/{args[0]}", kwargs.get("language"))

            return self.rq.get(f"{self.base}chapters/{args[0]}")

        if kwargs:
            return self.rq.get(f"{self.base}chapters", kwargs["language"])

        return self.rq.get(f"{self.base}chapters")

    def get_verses(self, id, **kwargs):
        """
        Get all the verse from specific chapter_id

        args:
            recitation
            translations
            media
            language        default: en
            page            for paginating the results
            offset
            limit           Control number of verse you want to get with each api call. Max limit is 50
            text_type       could be image[to get image of verse_id] OR words[this will return list of words for verse_id].
                            Allowed Values: words, image
                            default: words
        """
        return self.rq.get(f"{self.base}chapter/{id}/verse", kwargs)

    def get_verse(self, chapter_id, verse_id):
        """
        Get a single verse_id from a specific chapter_id
        """
        return self.rq.get(f"{self.base}chapters/{chapter_id}/verses/{verse_id}")

    def get_juzs(self):
        return self.rq.get(f"{self.base}juzs")

    def get_tafsirs_from_verse_id(self, chapter_id, verse_id):
        """
        args:
            chapter_id
            verse_id
        """
        return self.rq.get(f"{self.base}chapters/{chapter_id}/verse_id_ids/{verse_id}/tafsirs")

    def get_tafsir_from_verse_id_id(self, chapter_id, verse_id, **kwargs):
        """

        args:
            chapter_id
            verse_id
            tafsirs     Optional
        """
        return self.rq.get(f"{self.base}chapters/{chapter_id}/verse_id_ids/{verse_id}/tafsirs", kwargs)

    def search(self, **kwargs):
        """
        q           Search query, you can use query as well (optional)
        size        Results per page. s is also valid parameter. (default: 20, optional)
        page        Page number, well for pagination. You can use p as well (default: 0, optional
        language    ISO code of language, use this query params if you want to boost translations for specific language. (default: en, optional)
        """
        return self.rq.get(f"{self.base}search", kwargs)


# Test
if __name__ == "__main__":
    quran = Quran()
    # res = quran.get_recitations()
    # res = quran.get_translations()
    # res = quran.get_languages(language='ur')
    # res = quran.get_tafsirs()
    # res = quran.get_chapters(6, language="ur")
    # res = quran.get_verses(6, recitation=1, translations=21, language="en", text_type="words")
    res = quran.get_verse(6, 6)
    # res = quran.get_juzs()

    print(res)
