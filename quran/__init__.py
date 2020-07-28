#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: __init__.py
# Created: Tuesday, 28th July 2020 2:16:17 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Tuesday, 28th July 2020 4:47:09 pm
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import sys
sys.dont_write_bytecode = True

from .api import Quran
from .required import Request
from .exceptions import *

Request = Request
Quran = Quran
