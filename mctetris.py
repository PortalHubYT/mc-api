from mcpi.minecraft import Minecraft
from time import time, sleep



mc = Minecraft.create()
mc.postToChat("helowrld")


tps = 20
time_per_tick = 1000 / tps * (1 / 1000)


while True:
    mc.postToChat("a")
    sleep(time_per_tick)