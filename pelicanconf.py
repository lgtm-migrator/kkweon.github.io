#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Set to False when Publish
RELATIVE_URLS = False

AUTHOR = 'Mo'
SITENAME = 'Machine Learning Study Blog'
SITETITLE = 'ML Study Blog'
SITESUBTITLE = 'I write what I have learned today'
SITEDESCRIPTION = 'What I learn today'
SITEURL = 'https://kkweon.github.io'
# SITELOGO = SITEURL + '/images/profile.png'
SITELOGO = "https://avatars3.githubusercontent.com/u/2981167?v=3&s=460"
FAVICON = SITEURL + '/images/favicon.ico'
PYGMENTS_STYLE = 'default'


# THEME
BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
COPYRIGHT_YEAR = 2017

MAIN_MENU = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
GOOGLE_ANALYTICS = "UA-69116729-1"
GOOGLE_TAG_MANAGER = 'GTM-ABCDEF'
####


PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'ko'

THEME = 'pelican-themes/Flex'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/%s.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (
    # ('Pelican', 'http://getpelican.com/'),
    # ('Python.org', 'http://python.org/'),
    # ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('github', 'http://github.com/kkweon'),
    ('facebook', 'http://facebook.com/kkweon'),
    ('rss', 'http://kkweon.github.io/feeds/all.atom.xml'),
)

DEFAULT_PAGINATION = 10
USE_FOLDER_AS_CATEGORY = True

# Markup
MARKUP = ('md', 'ipynb')

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['pelican-ipynb.markup',
           "render_math",
           'sitemap',
           'rmd_reader',
           'gravatar']

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
REVERSE_CATEGORY_ORDER = True
DISQUS_SITENAME = "kyungmokweon"
DISPLAY_PAGES_ON_MENU = True

TYPOGRIFY = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

RMD_READER_RENAME_PLOT = 'directory'
RMD_READER_KNITR_OPTS_CHUNK = {'fig.path': 'figure/'}
STATIC_PATHS = ['figure', 'images', 'static']
EXTRA_PATH_METADATA = {
    'static/css/mo.css': {'path': 'static/mo.css'},
}

CUSTOM_CSS = 'static/mo.css'
ADD_THIS_ID = "ra-5932152d13edaf2f"

