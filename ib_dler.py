import re
import sys
import urllib.request

def main():
    ''' Main function, where all the fun happens'''

    # Check for human error
    if len(sys.argv) < 3:
        raise Exception('URL and output dir arguments are required.')

    # Grab arguments from sysv
    url = sys.argv[1]
    od = sys.argv[2]
    if not od.endswith('/'):
        od += '/'
    print('Using ' + url)

    # send GET to URL
    try:
        response = urllib.request.urlopen(url).read()
    except Exception as e:
        raise Exception('Error occured during initial request: ' \
            + type(e).__name__ + ': ' + str(e))

    # Parse response, find anchors, filter to imgs
    ilp = []
    p = re.compile('<a.*?href=[\'|"](.*?)[\'"]')
    ilr = p.findall(str(response))
    exts = ['jpg', 'jpeg', 'png', 'gif']
    for i in ilr:
        if exts.__contains__(re.search('\.*{3-4}$', i).group(0):
            if not ilp.__contains__('http:' + i):
                ilp.append('http:' + i)

    # Loop i URLs, GET, and per1sext2ist
    n = 0
    for i in ilp:
        urllib.request.urlretrieve(i, od + re.search('[0-9]+\..+$', i).group(0))
        n += 1

if __name__ == '__main__':
    try:
        if sys.argv[1] == '--help':
            print("""Image Board Downloader (Fri Dec 11 21:52:52 EST 2015)
ibdl [OPTION] URL OUTPUTDIR
    The default action is to identify every anchor found at URL whose reference contains an
    image extension type, and download it to OUTPUTDIR.
    -e      Extension list in the form of ext1,ext2...""")
        else:
            main()
    except Exception as e:
        print(type(e).__name__ + ': ' + str(e))
