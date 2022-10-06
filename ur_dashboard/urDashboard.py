import socket

DASHBOARD_PORT = 29999


class URDashboard:
    """
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

        self.server.connect((self.ipAddress, DASHBOARD_PORT))

        return self.server.recv(1024)

    def load(self, programName):
        """
        Load a myProgram.urp file already present on the robot.

        :param programName: name of the .urp program (without the .urp)
        :type programName: string

        :return:
        :rtype: string
        """

        self.server.sendall(programName + ".urp\n")

        return self.server.recv(1024)
