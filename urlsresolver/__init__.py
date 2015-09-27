# coding=utf-8
from HTMLParser import HTMLParser
from collections import OrderedDict
from contextlib import closing
import re
from urlparse import urljoin

__version__ = (1, 1, 4)
__author__ = 'Alexandr Shurigin (https://github.com/phpdude/)'

# HTML tags syntax http://www.w3.org/TR/html-markup/syntax.html
TAG_ATTRIBUTES_REGEX = \
    "(?:\s+%(attr)s\s*=\s*\"%(dqval)s\")|" \
    "(?:\s+%(attr)s\s*=\s*'%(sqval)s')|" \
    "(?:\s+%(attr)s\s*=\s*%(uqval)s)|" \
    "(?:\s+%(attr)s)" % {
        'attr': "([^\s\\x00\"'>/=]+)",
        'uqval': "([^\s\"'=><`]*)",
        'sqval': "([^'\\x00]*)",
        'dqval': "([^\"\\x00]*)"
    }


def get_tags(html, tag_name):
    parser = HTMLParser()
    for m in re.findall('<%s(\s+[^>]*)/*>' % tag_name, html, re.IGNORECASE):
        attrs = {}

        for x in re.findall('(?:(%s))' % TAG_ATTRIBUTES_REGEX, m, re.UNICODE):
            if x[1]:
                attrs[x[1]] = parser.unescape(x[2].decode('utf-8'))
            elif x[3]:
                attrs[x[3]] = parser.unescape(x[4].decode('utf-8'))
            elif x[5]:
                attrs[x[5]] = parser.unescape(x[6].decode('utf-8'))
            elif x[7]:
                attrs[x[7]] = parser.unescape(x[7].decode('utf-8'))

        yield attrs


def resolve_url(
        start_url,
        user_agent=False,
        chunk_size=1500,
        max_redirects=30,
        history=False,
        remove_noscript=False,
        **kwargs):
    """
    Helper function for expanding shortened urls.

    :param start_url: Shortened url to expand
    :param user_agent: Custom User-Agent header.
    :param chunk_size: Size of header to fetch from response body for searching meta refresh tags.
    :param max_redirects: Maximum meta refresh redirects
    :param history: If True, function will return tuple with (url, history) where history is list of redirects
    :param remove_noscript: Remove <noscript></noscript> blocks from head HTML (skip redirects for old browsers versions)
    :param kwargs: Custom kwargs for requests.get(**kwargs) function.
    :return: str|tuple
    """
    import requests

    s = requests.session()

    urls_history = OrderedDict()
    # disable compression for streamed requests.
    s.headers['Accept-Encoding'] = ''

    if user_agent:
        s.headers['User-Agent'] = user_agent

    def follow_meta_redirects(url, redirects, **kwargs):
        urls_history[url] = True

        if redirects < 0:
            raise ValueError("Cannot resolve real url with max_redirects=%s" % max_redirects)

        redirects -= 1

        with closing(s.get(url, allow_redirects=True, stream=True, **kwargs)) as resp:
            if resp.history:
                for r in resp.history:
                    urls_history[r.url] = True

            head, real_url = next(resp.iter_content(chunk_size, decode_unicode=False)), resp.url

        # Removing html blocks in <noscript></noscript>
        if remove_noscript:
            head = re.sub('<noscript[^>]*>.*</noscript[^>]*>', '', head, flags=re.DOTALL)

        redirect = None
        if 'refresh' in resp.headers:
            redirect = resp.headers['refresh']
        elif not redirect:
            for tag in get_tags(head, 'meta'):
                if tag.get('http-equiv', '') == 'refresh':
                    redirect = tag.get('content', None)

        if redirect:
            m = re.search('url\s*=\s*([^\s;]+)', redirect, re.I)
            if m:
                m = m.group(1)

                # fixing case url='#url here#'
                if m.startswith(('"', "'")) and m.endswith(('"', "'")):
                    m = m[1:-1]

                real_url = follow_meta_redirects(urljoin(resp.url, m), redirects)

        urls_history[real_url] = True

        return real_url

    real_url = follow_meta_redirects(start_url, max_redirects, **kwargs)
    if history:
        return real_url, urls_history.keys()
    else:
        return real_url
