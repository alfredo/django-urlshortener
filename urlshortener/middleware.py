from django.http import HttpResponsePermanentRedirect
from django.core.cache import cache

from urlshortener.extras import get_setting
from urlshortener.models import ShortUrl

class UrlShortenerMiddleware(object):

    def process_response(self, request, response):
        # we query once nothing else responded
        if response.status_code == 404:
            try:
                alias = request.path.split('/')
                page = ShortUrl.objects.get(alias=alias[1])
                ips = get_setting('EXCLUDE_IPS', [])
                # Don't track if excluded
                track = not request.META['REMOTE_ADDR'] in ips
                if track:
                    page.clicked()
                # track links per hour if setting enabled
                # requires cache enabled for performance
                if get_setting('HISTORICAL'):
                    prefix = get_setting('CACHE_KEY', 'URLSHORTENER')
                    last = '%slastsave' % prefix
                    current = '%scurrent' % prefix
                    cache.get(last)
                    cache.set(last,'')
                return HttpResponsePermanentRedirect(page.url)
            except ShortUrl.DoesNotExist:
                # response is a 404
                return response
        return response
