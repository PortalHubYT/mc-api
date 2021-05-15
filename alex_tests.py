from mc_api.components.Coordinates import Coordinates
from mc_api.components.Block import Block
from mc_api.components.BlockState import BlockState
from mc_api import components, server

instance = server.create.DockerInstance()
server = server.connect.Rcon("localhost", 25575)
server.create()

mc = Attach()

coords = Coordinates(0, 4, 0)
stairs = Block("oak_stairs")
facing = BlockState("facing", "east")
half = BlockState("half", "bottom")


stairs.blockstate = [facing, half]

mc.post(f'setblock {coords.to_str()} {stairs.to_str()}')