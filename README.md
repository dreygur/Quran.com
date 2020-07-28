<p align="center">
  <img alt="" style="{max-height: 50px}" src="./images/banner.png">
</p>

# Quran.com API [![Build Status](https://travis-ci.com/dreygur/Quran.com.svg?token=eWxPbQig1xhUqhPrMFx5&branch=master)](https://travis-ci.com/dreygur/Quran.com)
This is a python wraper for [quran.com](https://quran.com) v3 api

API will respond with English content by default, but you can get content in other language for most api calls using language query parameters. You can pass language id or language iso code as query string value. For list of available language see [languages](https://quran.api-docs.io/v3/options/languages) endpoint.

### Using quran.com

__Installing__
```bash
python3 -m pip install git+https://github.com/dreygur/Quran.com.git
```
or
```bash
pip install git+https://github.com/dreygur/Quran.com.git
```

__Importing Quran:__
```python3
from quran import Quran
qur = Quran()
```

__Methods__
```python3
from quran import Quran
qur = Quran()

# All the methods returns a dictionary object

# Getting all Recitations
qur.get_recitations

# Getting all available Translations
qur.get_translations()

# Getting all avalailable Languages
qur.get_languages()

# Getting all Tafsirs available in this api
qur.get_tafsirs()

# Getting all Chapters names
qur.get_chapter(6, info=True, language='bn') # Keyworded arguments are optional

# Getting all the Verses from a chapter
qur.get_verses(6)
```