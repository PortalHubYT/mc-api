import time
var = time.time()
from mcapy_lib import *
print(time.time() - var)




pos1 = Coordinates(0, 4, 0)
pos2 = Coordinates(10, 4, 10)
to_place =  Block("bedrock")
to_replace = Block("air")

fill(pos1, pos2, to_place)
