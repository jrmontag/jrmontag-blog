#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Josh Montague'
SITENAME = u'lab notebook'
SITEURL = 'http://joshmontague.com'
MINI_BIO = u'I type into colored screens all day. Mostly about social data, often in Python.'
TIMEZONE = 'US/Mountain'
DEFAULT_LANG = u'en'

#THEME = 'notmyidea'
THEME = 'pure-single'

ARTICLE_URL= 'posts/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# from pure readme
COVER_IMG_URL = 'http://farm4.staticflickr.com/3805/8797136352_0e5474ee28.jpg'
PROFILE_IMAGE_URL = 'http://2.gravatar.com/avatar/357be3e0935e653ba5cdae493f3dfcaf'
TAGLINE = 'thoughts on data'

# social widget
if THEME == 'notmyidea':
    SOCIAL = ( 
            ('Github', 'https://github.com/jrmontag')
            , ('Twitter', 'https://twitter.com/jrmontag')
            , ('LinkedIn', 'https://linkedin.com/in/joshuamontague')
        )
elif THEME == 'pure-single':
    SOCIAL = (
            ('github', 'https://github.com/jrmontag')
            , ('twitter-square', 'https://twitter.com/jrmontag')
            , ('linkedin', 'https://linkedin.com/in/joshuamontague')
        )
else:
    SOCIAL = (
        )


## swap out of FILES_TO_COPY, re:
## https://github.com/getpelican/pelican/blob/master/docs/settings.rst#path-metadata 
#FILES_TO_COPY = (
#        ('extra/CNAME', 'CNAME')
#        , ('extra/favicon.ico', 'favicon.ico')
#    )
PATH = '/Users/jrm/blog/src/content'
STATIC_PATHS = [
        'extra/CNAME'
        , 'extra/favicon.ico'
    ]


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
