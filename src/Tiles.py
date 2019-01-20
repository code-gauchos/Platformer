class Tile():
    Index=0
    def __init__(self, file, walkable, color):
        self.file=file
        self.walkable=walkable
        self.color=color
        self.number=Tile.Index
        Tile.Index+=1