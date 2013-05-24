#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Arnaldo Russo and Luiz Irber'
SITENAME = u'DataSounds'
SITEURL = ''

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = 'blog'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),)
          

# Social widget
SOCIAL = (('github', 'http://github.com/DataSounds'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

FILES_TO_COPY = (('CNAME', 'CNAME'),)
