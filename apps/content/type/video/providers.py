#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.utils import all_subclasses


class VideoProvider(object):
    def __init__(self, content):
        self.content = content

    @classmethod
    def type(cls):
        return cls.__name__.replace(cls.__base__.__name__, '').lower()

    @staticmethod
    def get_types():
        return {provider.type(): provider for provider in all_subclasses(VideoProvider)}


class VideoProviderYouTube(VideoProvider):
    def __repr__(self):
        return '<iframe width="420" height="315" src="https://www.youtube-nocookie.com/embed/sNPnbI1arSE"' \
               'frameborder="0" allowfullscreen></iframe>'


class VideoProviderCustom(VideoProvider):
    def __repr__(self):
        return self.content