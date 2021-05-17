class ServerInstance():
    def __init__(self):
        self.ready = False
    
    def check_status(self):
        if 'interface' in dir(self):
            return True
        else:
            return False
    
    def add_interface(self, interface):
        self.interface = interface

    def post(self, cmd):
        if hasattr(self, 'interface') and callable(self.interface):
            return self.interface(cmd)
        else:
            raise NoInterfaceProvided(f'ServerInstance did not received a correct interface. Add it with add_interface')

interface = ServerInstance()

class NoInterfaceProvided(Exception):
    pass