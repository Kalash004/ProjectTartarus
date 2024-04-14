import abc


class IHandleClientException:

    @abc.abstractmethod
    def handle_exception_inform_client(self, exception: BaseException, connection_manager):
        raise NotImplemented
