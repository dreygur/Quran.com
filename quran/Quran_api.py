#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: api.py
# Created: Tuesday, 28th July 2020 12:31:21 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Wednesday, 29th July 2020 1:34:28 am
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import quran as q
from typing import Dict

class Quran:
    """
    quran.com api class

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
        self.base: str = "http://api.quran.com/api/v3/"
        self.rq: str = q.Request()

    def get_recitations(self, **kwargs) -> Dict:
        """
        Get list of available Recitations.
        Use language query to get translated names of reciters in specific language(e.g language=ur will send translation names in Urdu).

        args
            language

        returns
            json Object
        """
        return self.rq.get(f"{self.base}options/recitations", kwargs)

    def get_translations(self, **kwargs) -> Dict:
        """
        Get list of available translations.
        args
            None

        returns
            json Object
        """
        return self.rq.get(f"{self.base}options/translations", kwargs)

    def get_languages(self, **kwargs) -> Dict:
        """
        Get all languages.
        You can get translated names of languages in specific language using language query parameter.
        For example:
            obj.get_languages(bn)
        will return language names translated into Bangla

        args:
            language    Specific Laguage in ISO

        returns:
            json Object
        """
        return self.rq.get(f"{self.base}options/languages", kwargs)

    def get_tafsirs(self) -> Dict:
        """
        args:
            None

        returns:
            json Object
        """
        return self.rq.get(f"{self.base}options/tafsirs")

    def get_chapter(self, *args, **kwargs) -> Dict:
        """
        Get list of chapter. Use language query to get translated names of chapter in specific language
        (e.g language=bn will send translation names in Bangla).

        args:
            info      Show insformation (True/False)
            language  Target Language

        returns:
            json Object
        """
        if args:
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

    def get_verses(self, chapter_id, **kwargs) -> Dict:
        """
        Get all the verse from specific chapter_id

        args:
            chapter_id
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

        returns:
            json Object
        """
        return self.rq.get(f"{self.base}chapters/{chapter_id}/verses", kwargs)

    def get_verse(self, chapter_id, verse_id) -> Dict:
        """
        Get a single verse_id from a specific chapter_id

        args:
            chapter_id      Integer
            verse_id        Integer
        """
        return self.rq.get(f"{self.base}chapters/{chapter_id}/verses/{verse_id}")

    def get_juzs(self) -> Dict:
        return self.rq.get(f"{self.base}juzs")

    def get_tafsirs_from_verse_id(self, chapter_id, verse_id) -> Dict:
        """
        Returns all Tafsir from a verse_id

        args:
            chapter_id
            verse_id

        returns:
            json Object
        """
        return self.rq.get(f"{self.base}chapters/{chapter_id}/verses/{verse_id}/tafsirs")

    def get_tafsir_from_verse_id(self, chapter_id, verse_id, **kwargs) -> Dict:
        """
        Returns a single Tafsir from a verse_id

        args:
            chapter_id
            verse_id
            tafsirs     Optional

        returns:
            json Object
        """
        return self.rq.get(f"{self.base}chapters/{chapter_id}/verses/{verse_id}/tafsirs", kwargs)

    def search(self, **kwargs) -> Dict:
        """
        args:
            q           Search query, you can use query as well (optional)
            size        Results per page. s is also valid parameter. (default: 20, optional)
            page        Page number, well for pagination. You can use p as well (default: 0, optional
            language    ISO code of language, use this query params if you want to boost translations for specific language. (default: en, optional)

        returns:
            json Object
        """
        return self.rq.get(f"{self.base}search", kwargs)

