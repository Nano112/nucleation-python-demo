import time
import os
from nucleation import Schematic, ResourcePack, SchematicBuilder, RenderConfig
import nucleation
resource_pack = ResourcePack.from_file("pack.zip")
schem = Schematic("stone")

XOR = ""
with open("xor.txt", "r") as f:
    XOR = f.read()

schematic = (
    SchematicBuilder()
    .name("out")
    .from_template(XOR)
    .map("l", "minecraft:lever[face=floor,powered=false,facing=north]")
    .map("░", "minecraft:redstone_lamp[lit=false]")
    .build()
)


world = schematic.create_simulation_world()
world.on_use_block(0, 1, 3)
world.tick(4)

world.sync_to_schematic()
schem = world.get_schematic()
schem.to_mesh(resource_pack).save("artifacts/out.glb")
schem.save("artifacts/out.schem")
schem.save("artifacts/out.litematic")
schem.render_to_file(
    resource_pack,
    "artifacts/out.png",
    RenderConfig(
        width=3840,
        height=2160,
        yaw=45.0, 
        pitch=45.0, 
        zoom=0.7,
        fov=45.0,
    ),
)

