import socket


def socket_open(sock: socket.socket) -> bool:
    """
    Checks if socket is still open
    :param sock: socket connection
    :return: true if open
    """
    try:
        err = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
        return err == 0
    except Exception as e:
        return False
