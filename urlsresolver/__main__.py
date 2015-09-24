import argparse

import urlsresolver

if __name__ == '__main__':
    args = argparse.ArgumentParser(
        prog='python -m urlsresolver',
        description='Urls resolver library. Allow you get real url of shortened.',
        version=".".join(map(str, urlsresolver.__version__)),
    )
    args.add_argument('url')
    args.add_argument('-V', '--verbose', help='Verbose output', action='store_true')
    args.add_argument('-A', '--user-agent', help='Custom user agent')
    args.add_argument('-S', '--chunk-size', default=1500, metavar='SIZE',
                      help='Length of fetched html block for testing meta redirects. Default 1500')
    args.add_argument(
        '--remove_noscript',
        action='store_true',
        help='Remove <noscript>...</noscript> blocks from header html for meta redirects'
    )
    args = args.parse_args()

    result = urlsresolver.resolve_url(
        args.url,
        user_agent=args.user_agent,
        chunk_size=args.chunk_size,
        history=args.verbose,
        remove_noscript=args.remove_noscript
    )

    if not args.verbose:
        print result
    else:
        print 'Source:\n    %s\n' % args.url
        print 'Expanded:\n    %s\n' % result[0]

        if len(result[1]) > 1:
            print 'Redirects history:'
            for i, url in enumerate(result[1], start=1):
                print '    %s. %s' % (i, url)

            print '\nTotal %s redirects' % (len(result[1]) - 1)
