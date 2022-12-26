#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ian'
SITENAME = 'Logfok'
# SITEURL = 'https://dyang504.github.io/site'

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

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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