import json
import math
import os

from palettes import palette_full, palette_small

import shulker as mc

path = os.path.dirname(os.path.abspath(__file__))
with open(f"{path}/mc_data/palette.json") as f:
    palette = json.load(f)


def block_from_rgb(pixel, picker="small"):
    if picker == "old":
        r = int(pixel[0] / 32)
        g = int(pixel[1] / 32)
        b = int(pixel[2] / 32)

        index = r * 64 + g * 8 + b
        return palette[str(index)]
    elif picker == "full" or picker == "small":
        closest = math.inf
        if picker == "full":
            palette = palette_full
        else:
            palette = palette_small
        for p in palette:
            mult = 255 / 100
            r = palette[p][0] * mult
            g = palette[p][1] * mult
            b = palette[p][2] * mult

            distance = math.sqrt(
                (pixel[0] - r) ** 2 + (pixel[1] - g) ** 2 + (pixel[2] - b) ** 2
            )

            if distance < closest:
                closest = distance
                closest_color = p

        return closest_color


def print_palette(picker=False, size=50):
    for x in range(size):
        for y in range(size):
            for z in range(size):
                mult = 255 / size
                color_to_match = (
                    math.floor(x * mult),
                    math.floor(y * mult),
                    math.floor(z * mult),
                )
                pixel = (x * 2, y * 2, z * 2)
                closest_color = block_from_rgb(color_to_match, picker=picker)
                mc.set_block(pixel, closest_color)
                light_pos = (pixel[0], pixel[1] + 1, pixel[1])
                mc.set_block(light_pos, "light")


def remove_shulkers():
    cmd = "kill @e[type=minecraft:shulker]"
    print(mc.post(cmd))


def print_glowing_palette(palette):
    for k in palette:
        x, y, z = palette[k]
        cmd = f"""summon shulker {x} {y} {z} {{Invulnerable:1b,Glowing:1b,CustomNameVisible:1b,NoAI:1b,AttachFace:0b,CustomName:'{{"text":"{k}"}}',ActiveEffects:[{{Id:14,Amplifier:1b,Duration:2000000}}]}}"""
        mc.post(cmd)
