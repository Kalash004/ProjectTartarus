class UnknownException(BaseException):
    def __init__(self, msg):
        self.msg = msg
