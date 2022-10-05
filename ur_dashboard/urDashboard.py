import socket


class URDashboard:
    """
    Salut JC Mobile, tu lis ma doc ?

    Create a communication using TCP/IP with the dashboard server interface of a Universal Robot e-series.

    :param ipAddress: the ip address of the Universal Robot.
    :type ipAddress: string
    """

    def __init__(self, ipAddress):
        self.ipAddress = ipAddress
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Connect to the Universal Robot dashboard Server

        :return: The status of the connection
        :rtype: string
        """

        self.server.connect((self.ipAddress, 29999))

        return self.server.recv(1024)
