# Resource container classes


class info:
    # Help Prompt
    def help():
        print("""Image Board Downloader (Fri Dec 11 21:52:52 EST 2015)
    ibdl [OPTION] URL OUTPUTDIR
    The default action is to identify every anchor found at URL whose reference contains an
    image extension type, and download it to OUTPUTDIR.
    -e      [TODO] Extension list in the form of ext1,ext2...
    -h      [TODO] Show response headers
    -b      [TODO] Show response body""")

    # Argument info
    def environment(url, od) :
        print('Using URL: ' + url + '\nUsing Output Dir: ' + od + '\n')

    # HTTP headers
    def headers(r, url):
        print(str(r.info()) + '\n' + 'URL Fetched: ' + url)