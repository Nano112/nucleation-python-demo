from nucleation import Schematic
if __name__ == "__main__":
    schem = Schematic("stone")
    schem.set_block(0, 0, 0, "minecraft:stone")
    schem.save("artifacts/set_block.schem")