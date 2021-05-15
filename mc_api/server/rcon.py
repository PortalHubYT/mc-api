from mcrcon import MCRcon

class Rcon():
    def __init__(self, ip, password, port=25575):
        self.mcr = MCRcon(ip, password)
        try:
            self.mcr.connect()
        except Exception as e:
            raise e
        
    def post(self, cmd):
        ret = self.mcr.command(cmd)
        return ret

    def stop(self):
        self.mcr.disconnect()     

    def signal_handler(self, sig, frame):
        self.stop()


