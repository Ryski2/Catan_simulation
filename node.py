class Node:
    def __init__(self, resources, coords):
        self.player = None          # None:empty, -1:blocked, players 1, 2, 3, 4
        self.building = None        # None, settlement, city
        self.resources = resources  # {adjacent resources : dice values}
        self.coords = coords        # (row, col)