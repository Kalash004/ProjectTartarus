import abc


class IHandleException:

    @abc.abstractmethod
    def handle_exceptions(self, exception: BaseException):
        raise NotImplemented
