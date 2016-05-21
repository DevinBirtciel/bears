class Tile(object):
    """docstring for Tile"""
    _tile_width = 10
    _tile_height = 10

    def __init__(self, tile_id, tile_location, tile_img=None):
        self.tile_id = tile_id
        self.tile_location = tile_location  # Upper left corner
        self.tile_img = tile_img

    @property
    def tile_width(self):
        return type(self)._tile_width

    @property
    def tile_height(self):
        return type(self)._tile_height


if __name__ == '__main__':
    # Debugging, don't fucking worry about it!
    t = Tile(1, (0., 0.))
    t2 = Tile(2, (1., 0.))
