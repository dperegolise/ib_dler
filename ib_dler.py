#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Image Board Downloader
ibdl [OPTION] URL OUTPUTDIR
The default action is to identify every anchor found at URL whose reference
contains an image extension type, and download it to OUTPUTDIR.
"""
import re
import sys

from urllib.error import *
import urllib.request

from exceptions import *
from messages import *
import utilities

# Declare constants
EXTS = ['jpg', 'jpeg', 'png', 'gif']

def main():
    ''' Main function, where all the fun happens'''

    # Check for human error
    utilities.validate_args(sys.argv)

    # Grab arguments from sysv
    url, od = sys.argv[1], sys.argv[2]
    if not od.endswith('/'):
        od += '/'
    info.environment(url, od)

    # send GET to URL
    try:
        # Fake user agent
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) '\
		'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 '\
		'Safari/537.36'}
        req = urllib.request.Request(url, None, headers)
        r = urllib.request.urlopen(req)
        html = r.read()
        info.headers(r, url)
    except (HTTPError, URLError) as e:
        raise InitialRequestException(e, type(e).__name__)

    # Parse response, find anchors, filter to imgs
    ilp = []
    ilr = re.compile('<a.*?href=[\'|"](.*?)[\'"]').findall(str(html))
    extp = '^.*(' + '|'.join(EXTS) + ')$'
    for i in ilr:
        # Clean anchor hrefs
        if not i.startswith('http') and not i.startswith('https'):
            if i.startswith('//'):
                i = 'http:' + i
            elif not i.startswith('/'):
                    i = re.search('^.+/', url).group(0) + i
        # Check extension
        if re.match(extp, i):
            if not ilp.__contains__(i):
                ilp.append(i)

    # Loop URLs, GET, and persist
    n = 0
    for i in ilp:
        try:
            name = od + re.search('(?=\w+\.\w{3,4}$).+', i).group(0)
            urllib.request.urlretrieve(i, name)
            print('Retrieved ' + i + ' as ' + name)
        except Exception as e:
            raise Exception('Error occured during target retrieval: '\
            + type(e).__name__ + ': ' + str(e))
        finally:
            n += 1

try:
    main()
except ArgumentException as ae:
    print(str(ae))
    info.help()
except InitialRequestException as ie:
    print(ie.message)
except Exception as e:
    raise e