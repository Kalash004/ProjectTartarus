import abc


class IHandleClientException:

    @abc.abstractmethod
    def handle_client_exception(self, exception: BaseException, connection_manager):
        raise NotImplemented
