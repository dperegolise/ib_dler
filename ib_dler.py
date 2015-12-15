import re
import sys
import urllib.request

# Custom Exception classes

class ArgumentException(Exception):
    pass


# Resource container classes

class Messages:
    # Help Prompt
    def HELP():
        return """Image Board Downloader (Fri Dec 11 21:52:52 EST 2015)
ibdl [OPTION] URL OUTPUTDIR
    The default action is to identify every anchor found at URL whose reference contains an
    image extension type, and download it to OUTPUTDIR.
    -e      [TODO] Extension list in the form of ext1,ext2...
    -h      [TODO] Show response headers
    -b      [TODO] Show response body"""

    # Argument info
    def ECHOENV(url, od) :
        return 'Using URL: ' + url + '\nUsing Output Dir: ' + od + '\n'

    # HTTP headers
    def HEADERS(r, url):
        return str(r.info()) + '\n' + 'URL Fetched: ' + url


def main():
    ''' Main function, where all the fun happens'''

    # Check for human error
    if len(sys.argv) < 3:
        raise ArgumentException('URL and output dir arguments are required.')

    # Grab arguments from sysv
    url, od = sys.argv[1], sys.argv[2]
    if not od.endswith('/'):
        od += '/'
    print(Messages.ECHOENV(url, od))

    # send GET to URL
    try:
        r = urllib.request.urlopen(url)
        response = r.read()
        print(Messages.HEADERS(r, url))
    except Exception as e:
        raise Exception('Error occured during initial request: ' \
            + type(e).__name__ + ': ' + str(e))

    # Parse response, find anchors, filter to imgs
    ilp = []
    p = re.compile('<a.*?href=[\'|"](.*?)[\'"]')
    ilr = p.findall(str(response))
    exts = ['jpg', 'jpeg', 'png', 'gif']
    extp = '^.*(' + '|'.join(exts) + ')$'
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


if __name__ == '__main__':
    try:
        if len(sys.argv) == 1 or sys.argv[1] == '--help':
            print(Messages.HELP())
        else:
            main()
    except ArgumentException as ae:
        print(str(ae) + '\n\n' + Messages.HELP())
    except Exception as e:
        print(str(e))
