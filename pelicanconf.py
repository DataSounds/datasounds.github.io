#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Arnaldo Russo and Luiz Irber'
SITENAME = u'DataSounds'
SITEURL = 'http://localhost:8001/'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = 'Blog'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),)

THEME = 'theme/'

# Social widget
SOCIAL = (('GitHub', 'http://github.com/DataSounds'),
          ('Twitter', 'http://twitter.com/datasounds'),)

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
