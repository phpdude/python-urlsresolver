from unittest import TestCase

from urlsresolver import get_tags


class TestTagsExtraction(TestCase):
    def test_meta_tags_extraction(self):
        tags = get_tags("""
            <meta attribute1="11211"
             attribute2=10
             attribute3

             attribute4='asdasda
             asdasd'>
            """, 'meta')

        tag = next(tags)

        self.assertEqual(tag['attribute1'], '11211')
        self.assertEqual(tag['attribute2'], '10')
        self.assertEqual(tag['attribute3'], 'attribute3')
        self.assertEqual(tag['attribute4'], """asdasda
             asdasd""")

    def test_meta_tags(self):
        tags = list(get_tags("""
        <meta charset="utf-8"/>
        <meta http-equiv="refresh" content="0;test=&rarr;; URL=https://mobile.twitter.com/i/nojs_router?path=%2Ftwitter%2Fstatus%2F644156390211125249%2Fvideo%2F1"></meta>
        """, 'meta'))

        for t in tags:
            if 'charset' in t:
                self.assertEqual(t['charset'], 'utf-8')
            if 'http-equiv' in t:
                self.assertEqual(t['http-equiv'], 'refresh')
                self.assertEqual(t['content'], u'0;test=\u2192; URL=https://mobile.twitter.com/i/nojs_router?'
                                               u'path=%2Ftwitter%2Fstatus%2F644156390211125249%2Fvideo%2F1')
