import socket

class URDashboard:
    """
    Create a communication using TCP/IP with the dashboard server interface of a Universal Robot e-series.

    :param ipAddress: the ip address of the Universal Robot.
    :type ipAddress: string
    """

    def __init__(self, ipAddress):
        self.ipAddress = ipAddress

    def connect(self):
        """
        Connect to the Universal Robot dashboard Server

        :return: The status of the connection
        :rtype: string
        """

        return "Connection OK"
