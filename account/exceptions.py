
class SessionException(Exception):
    """
    This exception should be raised when the exception occurs at session environment
    """

    def __init__(self,reason):
        self.reason = reason

class RegisterException(Exception):
    """
    This exception should be raised when register error
    """
    def __init__(self,reason):
        self.reason = reason