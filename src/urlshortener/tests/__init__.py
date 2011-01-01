from django.test import TestCase
from django.test.client import Client
from urlshortener.models import ShortUrl

class SimpleTest(TestCase):

    def setUp(self):
        """Actions to be performed before each test"""
        self.data = {'url': 'http://www.google.com',
                     'slug': 'a'}

    def tearDown(self):
        """Actions to be performed after each test"""
        ShortUrl.objects.all().delete()

    def testUrl(self):
        """Test that the url got created properly"""
        short_url = ShortUrl.objects.create(**self.data)
        self.assertEquals(short_url.slug, 'a')
        self.assertEquals(short_url.clicks, 0)
        result = ShortUrl.objects.all().count()
        self.assertEquals(result, 1)

    def testRedirection(self):
        """Tests it redirects properly"""
        ShortUrl.objects.create(**self.data)
        c = Client()
        response = c.get('/a/')
        self.assertEqual(response['Location'], 'http://www.google.com')
        # check the tracking
        short_url = ShortUrl.objects.get(slug='a')
        self.assertEqual(short_url.clicks, 1)

