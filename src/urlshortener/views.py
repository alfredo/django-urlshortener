from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404

from urlshortener.extras import get_setting, set_historical
from urlshortener.models import ShortUrl

def redirect_url(request, slug):
    """Translates the given url into an slug"""
    url = get_object_or_404(ShortUrl, slug=slug)
    exclude_list = get_setting('EXCLUDE_IPS', [])
    is_tracked = not request.META['REMOTE_ADDR'] in exclude_list
    if is_tracked:
        url.add_click()
        if get_setting('HISTORICAL', False):
            set_historical(url)
    return HttpResponsePermanentRedirect(url.url)
