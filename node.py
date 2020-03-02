class Node:
    def __init__(self, resources):
        self.player = 0             # 0-empty, -1-blocked, players 1, 2, 3, 4
        self.building = None        # None, settlement, city
        self.resources = resources  # {adjacent resource tiles : dice values}