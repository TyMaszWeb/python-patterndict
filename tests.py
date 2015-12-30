try:
    import unittest2 as unittest
except ImportError:
    import unittest

import mock

import patterndict


class FnMatchDictTestCase(unittest.TestCase):

    d = None

    def setUp(self):
        self.d = patterndict.FnMatchDict([
            ('/pages/home', mock.sentinel.HomeView,),
            ('/pages/*', mock.sentinel.PageView,),
            ('/blog/*', mock.sentinel.BlogView,),
        ])

    def test_del(self):
        del self.d['/pages/about']
        self.assertNotIn('/pages/about', self.d)

    def test_get(self):
        self.assertIs(self.d['/pages/home'], mock.sentinel.HomeView)
        self.assertIs(self.d['/pages/about'], mock.sentinel.PageView)
        self.assertIs(self.d['/blog/justin-bieber-married-putin'], mock.sentinel.BlogView)
        self.assertRaises(KeyError, lambda: self.d['/terms-and-conditions'])

    def test_items(self):
        self.assertEqual(list(self.d.items()), [
            ('/pages/home', mock.sentinel.HomeView),
            ('/pages/*', mock.sentinel.PageView),
            ('/blog/*', mock.sentinel.BlogView),
        ])

    def test_keys(self):
        self.assertEqual(list(self.d.keys()), [
            '/pages/home', '/pages/*', '/blog/*'
        ])

    def test_pop(self):
        self.assertIs(self.d.pop('/pages/about'), mock.sentinel.PageView)


class UtilityFunctionsTestCase(unittest.TestCase):

    d = None

    def setUp(self):
        self.d = patterndict.OrderedDict([
            ('/pages/home', mock.sentinel.HomeView,),
            ('/pages/*', mock.sentinel.PageView,),
            ('/blog/*', mock.sentinel.BlogView,),
        ])

    def test_fnmatch_getkey(self):
        self.assertEqual(patterndict.fnmatch_getkey(self.d, '/pages/home'), '/pages/home')
        self.assertEqual(patterndict.fnmatch_getkey(self.d, '/pages/about'), '/pages/*')
        self.assertEqual(patterndict.fnmatch_getkey(self.d, '/blog/justin-bieber-married-putin'), '/blog/*')

    def test_fnmatch_getitem(self):
        self.assertEqual(patterndict.fnmatch_getitem(self.d, '/pages/home'), ('/pages/home', mock.sentinel.HomeView))
        self.assertEqual(patterndict.fnmatch_getitem(self.d, '/pages/about'), ('/pages/*', mock.sentinel.PageView))
        self.assertEqual(patterndict.fnmatch_getitem(self.d, '/blog/justin-bieber-married-putin'),
                        ('/blog/*', mock.sentinel.BlogView))
