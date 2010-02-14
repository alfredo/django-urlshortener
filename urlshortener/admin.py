from django.contrib import admin
from urlshortener.models import ShortUrl, ShortUrlHistory

class ShortUrlAdmin(admin.ModelAdmin):
    pass

class ShortUrlHistoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShortUrl, ShortUrlAdmin)
admin.site.register(ShortUrlHistory, ShortUrlHistoryAdmin)
