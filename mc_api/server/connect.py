import signal
import sys

from .create import DockerInstance

from mcrcon import MCRcon

class Rcon():
    def __init__(self, ip, password, rcon_port=25575):
        self.mcr = MCRcon(ip, password, port=rcon_port)

        try:
            self.mcr.connect()
        except Exception as e:
            raise e
        signal.signal(signal.SIGINT, self.signal_handler)

    def post(self, cmd):
        ret = self.mcr.command(cmd)
        return ret

    def stop(self):
        self.mcr.disconnect()     

    def signal_handler(self, sig, frame):
        self.stop()
        sys.exit()