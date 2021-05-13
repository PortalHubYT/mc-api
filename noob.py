import time
import logging

from container_driver import ServerInstance
logging.basicConfig(level=logging.INFO)


mc = ServerInstance(111, 'noob')


for _ in range(150):
    time.sleep(1)
    mc.post(f'say noob say {_}')

logging.info("Stopping instance after 150 cycles")
mc.stop()