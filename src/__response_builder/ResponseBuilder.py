from src.__utils.SingletonMeta import SingletonMeta


class ResponseBuilder(metaclass=SingletonMeta):
    # TODO: make this better
    codes = {
        "success": 1,
        "unknown": 22,
        "client": 23,
        "server": 24,
        "fatal": 25
    }

    def build_succes(self, response) -> str:
        success = "success"
        resp = f"STATUS:{self.codes[success]};"
        if response != (None or [[]] or []):
            data_repr = f"DATA:{str(response)}"
            resp += data_repr
        return resp

    def build_error(self, err_type) -> str:
        resp = f"STATUS:{self.codes[err_type]};"
        return resp
