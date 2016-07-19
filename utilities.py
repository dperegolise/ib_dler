from exceptions import ArgumentException
from messages import *

# Utility methods

def validate_args(argv):
    if len(argv) == 1 or argv[1] == '--help': # No args is valid as help message
        raise ArgumentException('')
    elif len(argv) < 3:						  # Otherwise, two required
        raise ArgumentException(error.args_required)