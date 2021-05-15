import logging
import time

from mcstatus import MinecraftServer

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def ping(port, ip, timeout=120):
    server = MinecraftServer("localhost", port)

    logging.info(f"Waiting for server to be up ...")
    for n in range(timeout):
        logging.debug(f'Trying to ping localhost:{port}')
        try:
            status = server.status()
            logging.info(f"Success ping in {status.latency} after {n}s")
            return status.latency
        except:
            logging.debug(f"Failed status ping {n}")
        time.sleep(1)
    
    return None