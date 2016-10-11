# -*- coding: utf-8 -*-
from model.mail_isp import Mail


def test_example():
    assert 1 == 1

def test_parse():
    xml_ok = """
        <?xml version="1.0"?>
        <!DOCTYPE PARTS SYSTEM "parts.dtd">
        <?xml-stylesheet type="text/css" href="xmlpartsstyle.css"?>
        <TITLE>Computer Parts</TITLE>
        <PART>
          <ITEM>Motherboard</ITEM>
          <MANUFACTURER>ASUS</MANUFACTURER>
          <MODEL>P3B-F</MODEL>
          <COST> 123.00</COST>
        </PART>
        <PART>
          <ITEM>Video Card</ITEM>
          <MANUFACTURER>ATI</MANUFACTURER>
          <MODEL>All-in-Wonder Pro</MODEL>
          <COST> 160.00</COST>
        </PART>
        <PART>
          <ITEM>Sound Card</ITEM>
          <MANUFACTURER>Creative Labs</MANUFACTURER>
          <MODEL>Sound Blaster Live</MODEL>
          <COST> 80.00</COST>
        </PART>
        <PART>
          <ITEM>inch Monitor</ITEM>
          <MANUFACTURER>LG Electronics</MANUFACTURER>
          <MODEL> 995E</MODEL>
          <COST> 290.00</COST>
        </PART>
    """
    xml = Mail.parse(xml_ok)
    assert xml.title.text == 'Computer Parts'
    assert len(xml.part()) == 4
