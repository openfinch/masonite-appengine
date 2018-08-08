""" The Mail ServiceProvider for AppEngine Mail API """

from masonite.provider import ServiceProvider
from .driver import MailAppEngineDriver


class MailAppEngineProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('MailAppEngineDriver', MailAppEngineDriver)

    def boot(self):
        pass
