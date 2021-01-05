# Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile
# it would take to cover a floor plan of width and height, using a cost entered
# by the user.

FLOOR_HEIGHT = int(input("Total floor height (cm): "))
FLOOR_WIDTH = int(input("Total floor width (cm): "))

TILE_HEIGHT = int(input("Tile height (cm): "))
TILE_WIDTH = int(input("Tile width (cm): "))
TILE_COST = int(input("Tile cost: $"))

floor_area = FLOOR_WIDTH * FLOOR_HEIGHT
tile_area = TILE_WIDTH * TILE_WIDTH

tile_needed = floor_area / tile_area
total_tile_cost = tile_needed * TILE_COST

print("Total tile cost: $", total_tile_cost,
      " | Amount of tiles needed: ", tile_needed)
