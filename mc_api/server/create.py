import logging
import signal

import docker

from . import ping

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class ServerInstanceHandler:

    def signal_handler(self, sig, frame):
        self.stop()

    def wait(self, timeout=120):
        if not ping(timeout):
            self.stop()

    def stop(self):
        raise NotImplementedError


class Run(ServerInstanceHandler):
    def __init__(self, 
                port=25565,
                container_name='mcpython',
                wait=True,
                image='ghcr.io/portalhubyt/template_server:latest'):
        
        signal.signal(signal.SIGINT, self.signal_handler)
        self.name = container_name
        self.port = port
        self.client = docker.APIClient()
        try:
            self.container = self.client.create_container(
                image,
                ports=[25565, 25575],
                host_config=self.client.create_host_config(port_bindings={25565:port, 25575:25575}),
                environment = ['EULA=TRUE'],
                name = container_name,
            )
            
            self.client.start(self.container)
        except Exception as e:
            raise e
        if wait == True:
            self.wait()

    def stop(self):
        logging.info(f'Stopping ...')
        self.socket.close()
        self.client.stop(self.container)        
        self.client.wait(self.container)
        self.client.remove_container(self.container)
        logging.info(f'Removed container')