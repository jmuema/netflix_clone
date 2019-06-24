# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import tmdbsimple as tmdb
import json
from time import mktime
import time
from datetime import datetime, date
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#API KEYS and Request Parameters
tmdb.API_KEY = '2b012f9ecbbab97ec21f8accbe05ca9ed'
DEVELOPER_KEY = 'AIzaSyB8Gzt0-50t3HoBDv_WNSgo9OhrBG_dwLE'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# Create your views here.

def movies(request):
    popular_movies_tmdb = tmdb.Movies('popular')
    popular_movies = popular_movies_tmdb.info()['results']

    upcoming_movies_tmdb = tmdb.Movies('upcoming')
    upcoming_movies = upcoming_movies_tmdb.info()['results']

    return render(request, 'movies.html', {'popular':popular_movies, 'upcoming':upcoming_movies})

