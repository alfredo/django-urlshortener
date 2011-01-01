import time

from django.conf import settings
from django.core.cache import cache

VALID = 'abcdefghaijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def get_setting(key, override=None):
    key = 'URLSHORTENER_%s' % key
    try:
        return getattr(settings, key)
    except AttributeError:
        return override

def get_alias(num):
    """
    Generates an alias for a shortcut should be
    readable if possible
    """
    short = ''
    while num != 0:
        # modulo
        num, remainder = divmod(num - 1, len(VALID))
        short += VALID[remainder]
    return short


def set_historical(url):
    """
    Saves the current counter when the difference between
    clicks is more than an hour.
    Trying to avoid hitting the database
    """
    prefix = get_setting('CACHE_KEY', 'URLSHORTENER')
    last_key = '%slastsave' % prefix
    counter_key = '%scurrent' % prefix
    timeout = get_setting('TIMEOUT', 86400)
    now = int(time.time())
    last = cache.get(last_key)
    last = last if last else 0
    diff = now - int(last)
    counter = cache.get(counter_key)
    counter = counter if counter else 0
    counter += 1
    cache.set(counter_key, counter, timeout)
    if diff > get_setting('HISTORY_SAVE', 3600):
        # Database save
        url.shorturlhistory_set.create(clicks=counter)
        cache.set(last_key, last, timeout)
        cache.set(counter_key, 0, timeout)
    return
