
from container_driver import ServerInstance


mc = ServerInstance(111, 'noob')

import time
for _ in range(250):
    time.sleep(1)
    mc.post(f"say Noob says {_}")

print("stoping instance")
mc.stop()