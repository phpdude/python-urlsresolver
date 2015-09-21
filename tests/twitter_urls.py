from random import shuffle, choice
import unittest
import re

import requests

from urlsresolver import URL_REGEX, resolve_url


class TestTwitterTrendsUrls(unittest.TestCase):
    def setUp(self):
        trends = requests.get('https://twitter.com/twitter')

        urls = re.findall(URL_REGEX, trends.content)
        urls = list(x for x in urls if re.match('https?://t.co/[a-z0-9]+$', x, re.IGNORECASE))
        shuffle(urls)

        self.urls = urls

    def test_twitter_urls(self):
        for u in self.urls[:3]:
            self.assertNotEqual(u, resolve_url(u))

    def test_url_history(self):
        test_url = choice(self.urls)

        url, history = resolve_url(test_url, history=True)

        self.assertNotEqual(url, test_url)
        self.assertIsInstance(history, list)
