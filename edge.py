class Edge:
    def __init__(self, src, dst):
        self.player = None     # None:empty, players 1, 2, 3, 4
        self.src = src
        self.dst = dst

    def build_road(self, player_id):
        self.player = player_id