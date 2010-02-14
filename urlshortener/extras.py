from django.conf import settings
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
