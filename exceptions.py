from messages import error

# Custom Exception classes

class ArgumentException(Exception):
    pass

class InitialRequestException(Exception):
    def __init__(self, message, t):
        self.message = error.init_req + '\n' + t + ': ' + str(message)
        pass

class RetrievalException(Exception):
    pass