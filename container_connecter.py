import docker
import time
from pprint import pprint

import logging
import signal
import sys
import time

import docker
from mcstatus import MinecraftServer

# docker run --name template -it -p 25565:25565 -e EULA=TRUE ghcr.io/portalhubyt/template_server:latest
class ServerInstance():
    def __init__(self, port=25565, wait=True):
        self.client = docker.APIClient()
        self.port = port
        try:
            self.container = self.client.containers()[0]
        except Exception as e:
            raise e

        self.socket = self.client.attach_socket(self.container, params={'stdin': 1, 'stream': 1})
        signal.signal(signal.SIGINT, self.signal_handler)
        if wait == True:
            self.wait()

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
            time.sleep(1)
            logging.debug(f'Trying to ping localhost:{self.port}')
            try:
                status = server.status()
                logging.info(f"Success ping in {status.latency} after {n}s")
                return
            except:
                logging.debug(f"Failed status ping {n}")
        
        logging.warning(f"Coulnd't reach server after {timeout}s")
        logging.info(f"Triggering stop")
        self.stop()

    def stop(self):
        logging.info(f'Closing socket')
        self.socket.close()
        sys.exit(0)

        


