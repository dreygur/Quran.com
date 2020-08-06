#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: extractMethids.py
# Created: Thursday, 6th August 2020 12:24:03 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Thursday, 6th August 2020 12:52:57 pm
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import os

with open(os.path.join(os.path.dirname(__file__), 'Sunnah_api.py'), "r") as sunnah:
    for line in sunnah.readlines():
        if line.startswith('    def'):
            name = line.split(" ")[5].split("(")[0]
            with open("Sunnah_methods.txt", "a") as s_methods:
                s_methods.write(name + "\n")

with open(os.path.join(os.path.dirname(__file__), 'Quran_api.py'), "r") as sunnah:
    for line in sunnah.readlines():
        if line.startswith('    def'):
            name = line.split(" ")[5].split("(")[0]
            with open("Quran_methods.txt", "a") as s_methods:
                s_methods.write(name + "\n")
