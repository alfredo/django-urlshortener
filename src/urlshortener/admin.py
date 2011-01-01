from django.contrib import admin
from urlshortener.models import ShortUrl, ShortUrlHistory

class ShortUrlAdmin(admin.ModelAdmin):
    readonly_fields = ['clicks',]
    list_fields = ['slug', 'url', 'clicks']
    date_hierarchy = 'created'

class ShortUrlHistoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShortUrl, ShortUrlAdmin)
admin.site.register(ShortUrlHistory, ShortUrlHistoryAdmin)
