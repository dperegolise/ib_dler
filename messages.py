# Resource container classes

class info:
	# Help Prompt
    h = """Image Board Downloader (Fri Dec 11 21:52:52 EST 2015)
    ibdl [OPTION] URL OUTPUTDIR
    The default action is to identify every anchor found at URL whose reference
    contains an image extension type, and download it to OUTPUTDIR.
    -e      [TODO] Extension list in the form of ext1,ext2...
    -h      [TODO] Show response headers
    -b      [TODO] Show response body"""

    # Argument info
    e = 'Using URL: {}\nUsing Output Dir: {}\n'

    # HTTP headers
    hd = '{}\n' + 'URL Fetched: {}'

    def help():
        print(info.h)

    def environment(url, od) :
        print(info.e.format(url, od))

    def headers(r, url):
        print(info.hd.format(str(r.info()), url))

class error:
	# Missing arguments
    args_required = '\nURL and output dir arguments are required.\n'

    # Initial request error
    init_req = 'Error occured during initial request: '