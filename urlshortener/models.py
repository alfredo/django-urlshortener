from django.db import models
from django.contrib.sites.models import Site

from urlshortener.extras import get_alias

class ShortUrl(models.Model):
    """
    Short urls with counts
    """
    url = models.URLField(verify_exists=False)
    alias = models.CharField(max_length=15,
                             blank=True)
    clicks = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'Visits to: %s' % self.url

    def get_absolute_url(self):
        site = Site.objects.get_current()
        return u'http://%s/%s/' % (site.domain, self.alias)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        super(ShortUrl, self).save(*args, **kwargs)
        if not self.alias:
            # We use the id as unique number to generate
            # a unique alias
            self.alias = get_alias(self.id)
            self.save()

class ShortUrlHistory(models.Model):
    """
    Historical url count
    It will require some cache backend enabled
    to work properly in order not to stress the DB
    """
    short_url = models.ForeignKey('urlshortener.ShortUrl')
    created = models.DateTimeField()
    clicks = models.PositiveIntegerField(default=0)
