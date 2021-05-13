import time
var = time.time()
from mcapy_lib import *
print(time.time() - var)

setblock(Coordinates(0, 4, 0), Block("bedrock"))
setblock(Coordinates(2, 4, 0), Block("bedrock"))
setblock(Coordinates(4, 4, 0), Block("bedrock"))

time.sleep(1)

setblock(Coordinates(4, 4, 0), Block("air"))
setblock(Coordinates(2, 4, 0), Block("air"))
setblock(Coordinates(0, 4, 0), Block("air"))