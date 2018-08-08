import requests
from masonite.contracts.MailContract import MailContract
from masonite.drivers.BaseMailDriver import BaseMailDriver
from masonite.drivers.BaseDriver import BaseDriver

from google.appengine.api import mail as appengine_mail

class MailAppEngineDriver(BaseMailDriver, MailContract):
    """
    Appengine driver
    """
    def send(self, subject, recipient=None, message=None):
        if not message:
            message = self.message_body

        if not recipient:
            recipient = self.config.FROM['address']
        sender = "%s <%s>" % (self.config.FROM['name'], self.config.FROM['address'])
        try:
            appengine_mail.send_mail(sender=sender, to=recipient, subject=subject, body=message)
            return True
        except:
            return False