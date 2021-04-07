from django.test import TestCase

from .wsgi import application as appwsgi
from .asgi import application as appasgi

# Create your tests here.
class MutantiTestCase(TestCase):
    
    def app_shouldnt_be_false(self):
        """app should be false"""
        self.assertTrue(appasgi)
        self.assertTrue(appwsgi)