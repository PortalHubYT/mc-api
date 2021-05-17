import signal
import sys

from mc_api.server.interface import interface
from mcrcon import MCRcon

class Rcon():
    def __init__(self, ip, password, port=25575):
        self.ip = ip
        self.password = password
        self.port = port
        self.mcr = MCRcon(self.ip, self.password, port=self.port)

        try:
            self.mcr.connect()
        except Exception as e:
            raise e
        signal.signal(signal.SIGINT, self.signal_handler)

        interface.add_interface(self.mcr.command)

    def stop(self):
        self.mcr.disconnect()     

    def signal_handler(self, sig, frame):
        self.stop()
        sys.exit()