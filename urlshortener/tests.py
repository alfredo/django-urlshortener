from django.test import TestCase
from django.test.client import Client
from urlshortener.models import ShortUrl
from django.conf import settings

class SimpleTest(TestCase):

    def setUp(self):
        data = {'url': 'http://www.google.com',
                'alias': 'a'}
        self.short_url = ShortUrl.objects.create(**data)

    def tearDown(self):
        ShortUrl.objects.all().delete()

    def testUrl(self):
        """
        Test that the url got created properly
        """
        result = ShortUrl.objects.all().count()
        self.assertEquals(result, 1)
        self.assertEquals(self.short_url.alias, 'a')
        self.assertEquals(self.short_url.clicks, 0)

    def testRedirection(self):
        """
        Tests it redirects properly
        """
        c = Client()
        response = c.get('/a/', follow=True)
        self.assertEquals(response.redirect_chain[0][0],
                          'http://www.google.com')

