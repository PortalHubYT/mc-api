import logging
import signal
import time

import docker
from mcstatus import MinecraftServer

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class ServerInstanceHandler:
    def __init__(self):
        self.socket = None

    def signal_handler(self, sig, frame):
        self.stop()

    def post(self, cmd):
        if isinstance(cmd, str):
            logging.debug(f'sending: {cmd}')
            cmd += "\n"
            self.socket._sock.send(cmd.encode('utf-8'))
        else:
            logging.warning(f'cmd must be a str, got: {cmd}')
            
    def wait(self, timeout=120):
        logging.info(f"Waiting for server to be up ...")
        ## TODO secure this
        server = MinecraftServer("localhost", self.port)

        for n in range(timeout):
            logging.debug(f'Trying to ping localhost:{self.port}')
            try:
                status = server.status()
                logging.info(f"Success ping in {status.latency} after {n}s")
                return
            except:
                logging.debug(f"Failed status ping {n}")
            time.sleep(1)
        
        logging.warning(f"Coulnd't reach server after {timeout}s")
        logging.info(f"Triggering stop")
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
                stdin_open = True,
                ports=[25565],
                host_config=self.client.create_host_config(port_bindings={25565:port}),
                environment = ['EULA=TRUE'],
                name = container_name,
            )
            
            self.client.start(self.container)
        except Exception as e:
            raise e
        self.socket = self.client.attach_socket(self.container, params={'stdin': 1, 'stream': 1})
        if wait == True:
            self.wait()

    def stop(self):
        logging.info(f'Stopping ...')
        self.socket.close()
        self.client.stop(self.container)        
        self.client.wait(self.container)
        self.client.remove_container(self.container)
        logging.info(f'Removed container')
        

class Attach(ServerInstanceHandler):
    def __init__(self, port=25565, wait=True, container_id=None):
        self.client = docker.APIClient()
        signal.signal(signal.SIGINT, self.signal_handler)
        self.port = port
        if container_id == None:
            try:
                self.container = self.client.containers()[0]
            except Exception as e:
                raise e
        else:
            self.container = container_id

        self.socket = self.client.attach_socket(self.container, params={'stdin': 1, 'stream': 1})
        
        if wait == True:
            self.wait()

    def stop(self):
        logging.info(f'Closing socket')
        self.socket.close()