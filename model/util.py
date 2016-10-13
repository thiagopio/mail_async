# -*- coding: utf-8 -*-
from datetime import datetime


class Util(object):

    ISO_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
    UTC_FORMAT = '%Y-%m-%dT%H:%M:%S-03:00'

    @staticmethod
    def text2date(text, format):
        try:
            return datetime.strptime(text, format)
        except Exception, e:
            raise e