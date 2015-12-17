from exceptions import ArgumentException

# Utility methods

def validate_args(argv):
    # No args is valid as help message
    if len(argv) == 1 or argv[1] == '--help':
        pass
    elif len(argv) < 3:
        raise ArgumentException('URL and output dir arguments are required.')