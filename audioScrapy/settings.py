# -*- coding: utf-8 -*-

# Scrapy settings for audioScrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
# import os, sys
# os.environ.setdefault("DJANGO_SETTINGS_MODULE","djangoaudio.settings")
# path = os.path.join(os.path.dirname(__file__),'../djangoaudio')
# sys.path.append(os.path.abspath(path))
import sys
sys.path.append('/home/deshraj/Documents/audioScraper/djangoaudio')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoaudio.settings'
from django.conf import settings

BOT_NAME = 'audioScrapy'

SPIDER_MODULES = ['audioScrapy.spiders']
NEWSPIDER_MODULE = 'audioScrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'audioScrapy (+http://www.yourdomain.com)'


ITEM_PIPELINES = {
  'audioScrapy.pipelines.AudioscrapyPipeline': 300,
}

