# Nucleation

Python bindings for working with Minecraft schematics. Built with PyO3.

```bash
pip install nucleation
```

## Example: Build and Simulate a Redstone XOR Gate

```python
from nucleation import SchematicBuilder, ResourcePack

# Build a redstone circuit from ASCII art
schematic = (SchematicBuilder()
    .name("xor_gate")
    .from_template("""
# Base layer
cccc
cccc

# Logic layer
·│█·
┌▲▲┐
├┴┴┤
l··l

# Output layer
··░·
····
""")
    .map('l', 'minecraft:lever[face=floor,powered=false]')
    .map('░', 'minecraft:redstone_lamp[lit=false]')
    .build())

# Simulate the circuit
world = schematic.create_simulation_world()
world.on_use_block(0, 1, 3)  # Toggle a lever
world.tick(4)

# Export as 3D mesh
world.sync_to_schematic()
resource_pack = ResourcePack.from_file("pack.zip")
world.get_schematic().to_mesh(resource_pack).save("output.glb")
```

## Features

- **Format Support**: Litematic, Sponge Schematic, McStructure (Bedrock), MCA regions, world folders
- **Block Operations**: Get/set blocks, batch operations, fill shapes, copy regions
- **Transformations**: Rotate, flip, with full block state handling
- **Building Tools**: Shapes (sphere, cuboid) with color brushes and gradients
- **Simulation** *(feature-gated)*: MCHPRS-based redstone simulation with typed circuit I/O
- **Meshing** *(feature-gated)*: Generate 3D meshes (GLB/USDZ) from schematics using resource packs

## Documentation

See [api.md](api.md) for the full API reference.
