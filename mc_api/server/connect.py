import signal
import sys

from .singleton import singleton
from mctools import RCONClient


class RconClient:
    def __init__(self, ip, password, port=25575, mute: bool = True):
        self.ip = ip
        self.password = password
        self.port = port
        self.mcr = RCONClient(self.ip, port=self.port)

        try:
            self.mcr.login(self.password)
        except Exception as e:
            raise e
        signal.signal(signal.SIGINT, self.signal_handler)

        singleton.add_output_channel(self.mcr.command)

    def stop(self):
        self.mcr.disconnect()

    def signal_handler(self, sig, frame):
        self.stop()
        sys.exit()
