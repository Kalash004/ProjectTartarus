import socket
import traceback

# Importing specific classes and methods from various modules
from src.__utils.socket_utils import socket_open
from src.exception_handler.ExceptionHandler import ExceptionHandler
from src.logger.MyLogger import MyLogger

class Answerer:
    """
    This class is responsible for answering the requester.
    It is created from ConnectionManager.
    """

    def __init__(self, connection: socket.socket, address: str, connection_manager):
        """
        Initializes the Answerer with the provided connection, address, and connection manager.

        Args:
        - connection (socket.socket): The socket object representing the client connection.
        - address (str): The address of the client.
        - connection_manager: The connection manager object associated with this answerer.
        """
        self.connection: socket.socket = connection  # Client socket connection
        self.address = address  # Client address
        self.message = None  # Message to be sent
        self.stop_flag = False  # Flag to control the answerer's termination
        self.connection_manager = connection_manager  # Connection manager associated with this answerer

    def run(self):
        """Main method that runs the answerer."""
        with self.connection as conn:
            while not self.stop_flag:
                try:
                    self.__main_loop()  # Enters the main loop to send messages
                except Exception as e:
                    # Handles exceptions and informs the client through the connection manager
                    ExceptionHandler().handle_exception_inform_client(e, self.connection_manager)
            conn.close()  # Closes the connection
            return

    def __main_loop(self):
        """Main loop for sending messages."""
        if self.message is None:
            return  # Exits if there's no message to send
        self._send_and_clean()  # Sends the message and cleans up afterwards

    def stop(self):
        """Stops the answerer."""
        self.send_specific_message("Service was stopped, bye.")  # Sends a specific stop message
        self.stop_flag = True  # Sets the stop flag to terminate the answerer

    def _send_and_clean(self):
        """Sends the message and cleans up afterwards."""
        self.message = "\n\r" + self.message  # Prepares the message
        if not socket_open(self.connection):  # Checks if the socket is open
            self.stop_flag = True  # Sets the stop flag if the socket is closed
            return
        self.connection.send(self.message.encode())  # Sends the message
        self.message = None  # Resets the message after sending

    def send_specific_message(self, message):
        """
        Sends a specific message to the client.

        Args:
        - message (str): The message to be sent.
        """
        msg = "\n\r" + message  # Prepares the message
        if not socket_open(self.connection):  # Checks if the socket is open
            return
        try:
            self.connection.send(msg.encode())  # Sends the message
        except Exception as e:
            # Logs the exception if sending the message fails
            MyLogger().log_exception(e, traceback.format_exc())
