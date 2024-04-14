from src.__utils.SingletonMeta import SingletonMeta


class ResponseBuilder(metaclass=SingletonMeta):
    codes = {
        "success": 1
    }

    def build_succes(self, response) -> bytes:
        success = "success"
        resp = f"STATUS:{self.codes[success]};"
        if response != (None or [[]] or []):
            data_repr = f"DATA:{str(response)}"
            resp += data_repr
        return resp.encode()
