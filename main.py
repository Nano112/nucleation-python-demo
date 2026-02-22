import time
import os
from nucleation import Schematic, ResourcePack, SchematicBuilder
resource_pack = ResourcePack.from_file("pack.zip")
schem = Schematic("stone")

XOR = ""
with open("xor.txt", "r") as f:
    XOR = f.read()
    
schematic = (SchematicBuilder()
    .name("out")
    .from_template(XOR)
    .map('l', 'minecraft:lever[face=floor,powered=false]')
    .map('░', 'minecraft:redstone_lamp[lit=false]')
    .build())


world = schematic.create_simulation_world()
world.on_use_block(0, 1, 3) 
world.tick(4)

world.sync_to_schematic()
schem = world.get_schematic()
schem.to_mesh(resource_pack).save("artifacts/out.glb")
schem.save("artifacts/stone.schem")
schem.save("artifacts/stone.litematic")

# for i in range(10):
#     time.sleep(1)
#     world.on_use_block(3, 1, 3) 
#     world.tick(4)
#     world.sync_to_schematic()
#     world.get_schematic().to_mesh(resource_pack).save("artifacts/out.glb")
