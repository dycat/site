#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://dyang504.github.io/site'
# RELATIVE_URLS = False


FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'


DELETE_OUTPUT_DIRECTORY = True


AUTHOR = 'ian'
SITENAME = 'Logfok'

# # can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

PATH = 'content'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['neighbors']

THEME = 'theme_yellow'
THEME_STATIC_DIR = 'static'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'main.css'

TIMEZONE = 'Asia/Chongqing'

DEFAULT_LANG = 'en'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),)

DEFAULT_PAGINATION = 10

GOOGLE_ANALYTICS = "UA-134156222-1"

GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'auto'

STATIC_PATHS=[
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME':{'path':'CNAME'},
}

TYPOGRIFY = True