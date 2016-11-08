# -*- coding: utf-8 -*-
from email.header import Header
from email import Charset, utils
import smtplib


class SimpleMailTransferProtocol(object):

    ENCODE = 'utf-8'

    @staticmethod
    def from_xml(xml):
        smtp = SimpleMailTransferProtocol()
        smtp._to = xml._to
        smtp._from = xml._from
        smtp._subject = xml._subject
        smtp._content = xml._content
        return smtp

    def is_valid(self):
        if self._to == None:
            return False
        elif self._from == None:
            return False
        elif self._subject == None:
            return False
        elif self._content == None:
            return False
        return True

    def verify_address(self, address):
        from_name, from_address = utils.parseaddr(address)
        if len(from_name) > 0:
            return utils.formataddr(from_name, from_address)
        else:
            return from_address

    def send(self):
        # Charset.add_charset('utf-8', Charset.QP, Charset.QP, 'utf-8')
        # util.parseaddr, util.formataddr
        # "\"%s\" <%s>" % (Header('CobrançaTeste', 'utf-8'), 'here@globo.com')

        sender =  self.verify_address(self._from)
        receiver = self.verify_address(self._to)

        message = "From: %s\r\n" % sender \
                + "To: %s\r\n" % receiver \
                + "Subject: %s\r\n" % self._subject \
                + "\r\n" \
                + self._content

        server = smtplib.SMTP('smtp.local.com')
        server.set_debuglevel(1)
        server.sendmail(sender, receiver, message)
        server.quit()