
NEIGHBOR_OFFSET = [(-1, 0), (-1, -1), (0, -1), (-1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tile_map = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tile_map[str(3 + i) + ";10"] = {"type": "grass", "variant": 1, "pos": (3 + i, 10)}
            self.tile_map["10;" + str(5 + i)] = {"type": "stone", "variant": 1, "pos": (10, 5 + i)}

    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))

        for offset in NEIGHBOR_OFFSET:
            check_loc = str(tile_loc[0] + offset[0]) + ";" + str(tile_loc[1] + offset[1]);

            if check_loc in self.tile_map:
                tiles.append(self.tile_map[check_loc])
                
        return tiles

    def render(self, surf):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile["type"]][tile["variant"]], (tile["pos"]))
            
        for location in self.tile_map:
            tile = self.tile_map[location]
            surf.blit(self.game.assets[tile["type"]][tile["variant"]], (tile["pos"][0] * self.tile_size, tile["pos"][1] * self.tile_size))

                      
