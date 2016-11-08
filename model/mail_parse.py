# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from model.exception import FieldsException
from model.util import Util
from datetime import datetime


class Parse(object):

    REQUIRED_FIELDS = ('usuarioid','emailremetente','emaildestinatario','emailtitulo','emailcorpo')

    def __init__(self, xml):
        self.xml = xml
        self.parse()
        super(Parse, self).__init__()

    def parse(self):
        self._params = BeautifulSoup(self.xml, 'html.parser')
        self.validate()
        self.set_attr()

    def validate(self):
        for key in self.REQUIRED_FIELDS:
            if len(self._params.findAll(key)) == 0:
                raise FieldsException('not found requirement key {}'.format(key))

    def set_attr(self):
        self._user_id = self._params.usuarioid.text
        self._subject = self._params.emailtitulo.text
        self._from = self._params.emailremetente.text
        self._to = self._params.emaildestinatario.text
        self._content = self._params.emailcorpo.text
        self._scheduled = self._convert_date()

    def _convert_date(self):
        date = datetime.now()
        if self._params.dataagendada is not None:
            try:
                date = Util.text2date(self._params.dataagendada.text, Util.UTC_FORMAT)
            except Exception, e:
                print e
        return date

