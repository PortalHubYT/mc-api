
from container_driver import ServerInstance


mc = ServerInstance(222, 'boon')

import time
for _ in range(250):
    time.sleep(1)
    mc.post(f"say boon says {_}")

print("stoping instance")
mc.stop()
