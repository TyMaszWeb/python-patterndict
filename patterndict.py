try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict
import fnmatch


VERSION = (0, 0, 0)


def fnmatch_getkey(d, key):
    """
    Get the first dictionary key that passed key matches. This can be used to retrieve the real value.

    >>> d = {'192.168.0.*': 'LAN', '192.168.1.*': 'WLAN'}
    >>> fnmatch_getkey(d, '192.168.0.100')
    '192.168.0.*'

    :param d: dict|OrderedDict|defaultdict to scan
    :param key: value to compare keys against
    :raises KeyError when nothing matches key
    :return: concrete key
    """
    for k in d:
        if fnmatch.fnmatchcase(key, k):
            return k
    raise KeyError('{0} does not match any glob defined'.format(key))


def fnmatch_getitem(d, key):
    """
    Get the first (key, value) tuple from dictionary for which the passed key is a match.

    If you are subclassing dict don't use this method in __getitem__ or you'll run into recursive loop.

    >>> d = {'192.168.0.*': 'LAN', '192.168.1.*': 'WLAN'}
    >>> fnmatch_getitem(d, '192.168.0.100')
    ('192.168.0.*', 'LAN')

    :param d: dict|OrderedDict|defaultdict to scan
    :param key: value to compare keys against
    :raises KeyError when nothing matches key
    :return: tuple (key, value)
    """
    k = fnmatch_getkey(d, key)
    v = d[k]
    return k, v


class FnMatchDict(OrderedDict):
    """
    A dict-like object that matches keys using fnmatch_getkey. Order of key, item pairs is important.

    >>> fmd = FnMatchDict([
    ...     ('192.168.0.1', 'Router'),
    ...     ('192.168.0.*', 'LAN'),
    ...     ('192.168.1.*', 'WLAN'),
    ... ])
    >>> fmd['192.168.0.1']
    'Router'
    >>> fmd['192.168.0.100']
    'LAN'
    """

    def __contains__(self, item):
        try:
            fnmatch_getkey(self, item)
        except KeyError:
            return False
        else:
            return True

    def __delitem__(self, key):
        super(FnMatchDict, self).__delitem__(fnmatch_getkey(self, key))

    def __getitem__(self, item):
        return super(FnMatchDict, self).__getitem__(fnmatch_getkey(self, item))
