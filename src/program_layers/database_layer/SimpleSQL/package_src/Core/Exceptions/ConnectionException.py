class ConnectionException(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        self.exception = "Exception happened during connecting to the database"
        self.message = message
        super().__init__(f"{self.exception} : {self.message}")

    def __repr__(self):
        return f"{self.exception} : {self.message}"
