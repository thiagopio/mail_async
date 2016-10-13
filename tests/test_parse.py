# -*- coding: utf-8 -*-
from model.mail_parse import Parse
from model.exception import FieldsException
from model.util import Util
from datetime import datetime
import pytest


MAIL_XML = """
        <fila>
            <usuarioId>1234</usuarioId>
            <emailRemetente>remetente@mail.com</emailRemetente>
            <emailDestinatario>destinatario@mail.com</emailDestinatario>
            <emailTitulo>titulo</emailTitulo>
            <dataAgendada>2016-06-09T15:42:00-03:00</dataAgendada>
            <emailCorpo>corpo do e-mail</emailCorpo>
        </fila>
    """

MAIL_XML_NO_DATE = """
        <fila>
            <usuarioId>1234</usuarioId>
            <emailRemetente>remetente@mail.com</emailRemetente>
            <emailDestinatario>destinatario@mail.com</emailDestinatario>
            <emailTitulo>titulo</emailTitulo>
            <emailCorpo>corpo do e-mail</emailCorpo>
        </fila>
    """


def test_parse_wrong():
    with pytest.raises(FieldsException):
        Parse("<invalid_xml")


def test_parse_ok():
    parse_mail = Parse(MAIL_XML)
    assert parse_mail._subject == 'titulo'
    assert parse_mail._from == 'remetente@mail.com'
    assert parse_mail._to == 'destinatario@mail.com'
    assert parse_mail._content == 'corpo do e-mail'


def test_schedule_date_ok():
    parse_mail = Parse(MAIL_XML)
    date = Util.text2date('2016-06-09T15:42:00-03:00', Util.UTC_FORMAT)
    assert parse_mail._scheduled == date


def test_schedule_date_blank():
    parse_mail = Parse(MAIL_XML_NO_DATE)
    assert parse_mail._scheduled.date() == datetime.now().date()
