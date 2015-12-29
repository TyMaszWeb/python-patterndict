import collections
import fnmatch


VERSION = (0, 0, 0)


class GlobDict(collections.OrderedDict):
    """
    A dict-like object that matches keys using globs. Order of keys is important.
    """

    def _get_realkey(self, item):
        for key in self.keys():
            if fnmatch.fnmatchcase(item, key):
                return key
        raise KeyError('{} does not match any glob defined'.format(item))

    def __contains__(self, item):
        try:
            self._get_realkey(item)
            return True
        except KeyError:
            return False

    def __delitem__(self, key):
        super(GlobDict, self).__delitem__(self._get_realkey(key))

    def __getitem__(self, item):
        return super(GlobDict, self).__getitem__(self._get_realkey(item))
