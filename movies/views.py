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

# Create your views here.
