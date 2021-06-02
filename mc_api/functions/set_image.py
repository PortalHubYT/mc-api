import urllib3
import json
import os
import math
import time
from typing import Union

from PIL import Image

from mc_api.components.Block import Block
from mc_api.components.Zone import Zone
from mc_api.components.BlockCoordinates import BlockCoordinates
from mc_api.components.BlockHandler import BlockHandler
from mc_api.functions.base_functions import *


def _set_image(url: str, coords: BlockCoordinates, orientation: str) -> list:

    opposite_orientation = ["side", "top", "bottom"]

    for index, value in enumerate(opposite_orientation):
        if value == orientation:
            opposite_orientation.pop(index)

    http = urllib3.PoolManager()
    r = http.request("GET", url, preload_content=False)

    with open("image.jpg", "wb") as out:
        while True:
            data = r.read(1024)
            if not data:
                break
            out.write(data)

    r.release_conn()

    image = Image.open("image.jpg")
    image = image.quantize(colors=256, method=2)
    image_rgb = image.convert("RGB")
    pixels = list(image_rgb.getdata())
    width, height = image_rgb.size
    pixels = [pixels[i * width : (i + 1) * width] for i in range(height)]
    image_len = len(pixels[0])

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "blocks_color.json")

    start = time.time()
    block_list = []
    with open(path) as json_file:
        data = json.load(json_file)

        for line in pixels:
            for pixel in line:

                best_delta = 9999999
                block_name = None

                for block in data["averages"]:

                    if (
                        f"_{opposite_orientation[0]}" in block["image"]
                        or f"_{opposite_orientation[1]}" in block["image"]
                    ):
                        continue

                    delta = math.sqrt(
                        (pixel[0] - block["rgba"][0]) ** 2
                        + (pixel[1] - block["rgba"][1]) ** 2
                        + (pixel[2] - block["rgba"][2]) ** 2
                    )

                    if delta < best_delta:
                        best_delta = delta
                        block_name = block["image"][:-4]
                        block_name = block_name.strip(f"_{orientation}")
                else:
                    block_list.append(block_name)

    end = time.time()
    print(block_list)
    print(end - start)
    return []


def set_image(
    url: str, coords: Union[BlockCoordinates, tuple], orientation: str = "side"
):
    """
    This function takes an image URL, downloads it, and sends back the
    setblocks instruction to print the image in the provided orientation

    Orientation can either be "side", "top", "bottom" depending from where
    you want people to look at the image.
    """

    check_output_channel()

    coords = format_arg(coords, BlockCoordinates)

    if orientation not in ["side", "top"]:
        raise ValueError(f"Orientation must either be side or top for set_image()")

    instructions = _set_image(url, coords, orientation)

    for line in instructions:
        post(line)
