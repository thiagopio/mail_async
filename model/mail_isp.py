# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


class Mail(object):
    pass

    @staticmethod
    def parse(xml):
        return BeautifulSoup(xml, 'html.parser')
