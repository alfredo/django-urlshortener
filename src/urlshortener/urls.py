from django.conf.urls.defaults import *


urlpatterns = patterns('urlshortener.views',
                       url(r'^(?P<slug>[-\w]+)/$',
                           'redirect_url', {},
                           name='urlshortener_redirect'),
                       )
