
import glob
import math
import os
import time

import shulker as mc
from shulker.functions.color_picker import block_from_rgb

mc.connect("86.221.217.211", password="test")

print(block_from_rgb((255, 0, 0)))

SIZE = 50
def print_palette(x_offset, picker=False):
    print(mc.post(f"sudo StarlightmOB //pos1 {x_offset},0,0"))
    print(mc.post(f"sudo StarlightmOB //pos2 {x_offset + 100},100,100"))
    print(mc.post(f"sudo StarlightmOB //cut"))
    time.sleep(1)

    for x in range(SIZE):
        for y in range(SIZE):
            for z in range(SIZE):
                mult = 255 / SIZE
                color_to_match = (
                    math.floor(x * mult),
                    math.floor(y * mult),
                    math.floor(z * mult),
                )
                pixel = (x * 2 + x_offset, y * 2, z * 2)
                closest_color = block_from_rgb(color_to_match, picker=picker)
                ret = mc.set_block(pixel, closest_color)
                print(ret)
                light_pos = (pixel[0], pixel[1] + 1, pixel[1])
                mc.set_block(light_pos, "light")


def remove_shulkers():
    cmd = "kill @e[type=minecraft:shulker]"
    print(mc.post(cmd))


def print_original_palette(palette, x_offset):
    for k in palette:
        x, y, z = palette[k]
        cmd = f"""summon shulker {x + x_offset} {y} {z} {{Invulnerable:1b,Glowing:1b,CustomNameVisible:1b,NoAI:1b,AttachFace:0b,CustomName:'{{"text":"{k}"}}',ActiveEffects:[{{Id:14,Amplifier:1b,Duration:2000000}}]}}"""
        mc.post(cmd)


SPACE_BETWEEN = 120


import random

pickers = ["small", "full"]
pickers_to_try = ["small", "full"]


while True:

    for p in pickers_to_try:
        for i, _ in enumerate(pickers):
            if p == _:
                x_offset = (1 + i) * SPACE_BETWEEN
                print("picker=", p)
                print_palette(x_offset, picker=p)
                # draw_picture(x_offset, path, picker=p)

    # time.sleep(10)
    input("Press Enter for next image...")
