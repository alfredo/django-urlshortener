from django.http import HttpResponsePermanentRedirect

from urlshortener.extras import get_setting, set_historical
from urlshortener.models import ShortUrl

class UrlShortenerMiddleware(object):

    def process_response(self, request, response):
        # we query once nothing else responded
        if response.status_code == 404:
            try:
                alias = request.path.split('/')
                page = ShortUrl.objects.get(alias=alias[1])
            except ShortUrl.DoesNotExist:
                # response is a 404
                return response
            ips = get_setting('EXCLUDE_IPS', [])
            # Don't track if excluded
            track = not request.META['REMOTE_ADDR'] in ips
            if track:
                page.clicked()
            # track links per hour if setting enabled
            # requires cache enabled for performance
            if get_setting('HISTORICAL', False) and track:
                set_historical(page)
            return HttpResponsePermanentRedirect(page.url)
        return response
