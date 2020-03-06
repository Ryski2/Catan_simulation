from Connectors import *
from Player import *
import random
import itertools

class Board:
    # player_strategies = [1, None, None, None] means Player 1 uses strategy 1 while players 2 to 4 use the default strategy.
    # board_layout = 'basic' generates the layout shown in basic_layout.jpg.
    # board_layout = "random" would generate a random board layout.

    def __init__(self, player_strategies, board_layout):
        self.layout = []
        self.players = []
        self.edges = []
        self.nodes = []
        self.robber_tile = None
        self.setup(player_strategies, board_layout)
        # Keep track of edges and nodes on the board that can be built upon
        self.buildable_edges = set(self.edges)
        self.buildable_nodes = set(self.nodes)
        self.turns = 0

    def dice_roll(self, player):
        roll = random.randint(1,6) + random.randint(1,6)
        print("\t\tRolled a " + str(roll))
        return roll

    def distribute(self, roll): # new version
        for tile in self.layout:
            tile.distribute(roll)

    # Build a road for player on edge
    def build_road(self, player, edge):
        if edge.player is not None:
            raise Exception('Cannot build road, edge.player was not None')
        player.build_road()
        edge.player = player
        self.buildable_edges.discard(edge)
        player.edges.add(edge)
        for player1 in self.players:
            player1.buildable_edges.discard(edge)
        for edge1 in itertools.chain(edge.node1.edges, edge.node2.edges):
            if edge1 is not None and edge1 != edge and edge1 in self.buildable_edges:
                player.buildable_edges.add(edge1)
        for node in [edge.node1, edge.node2]:
            if node in self.buildable_nodes:
                player.buildable_nodes.add(node)
        print("\t\tPlayer " + str(player.id) + " built a road from " + edge.node1.get_coords() + " to " + edge.node2.get_coords())

    # Build a settlement for player at node
    def build_settlement(self, player, node):
        if node.player is not None:
            raise Exception('Cannot build settlement, node.player was not None')
        player.build_settlement()
        node.type = BuildType.Settlement
        node.player = player
        player.nodes.add(node)
        player.settlements.add(node)
        nodes = {node}
        for edge in node.edges:
            if edge is not None:
                nodes.add(edge.get_other_node(node))
        for node1 in nodes:
            self.buildable_nodes.discard(node1)
            for player1 in self.players:
                player1.buildable_nodes.discard(node1)
        for tile in node.resources:
            if tile is not None:
                player.resource_rates[tile.resource.value] += tile.chance
        print("\t\tPlayer " + str(player.id) + " built a settlement at " + node.get_coords())

    # Replace a settlement of player with a city at node
    def build_city(self, player, node):
        if node.player is not player:
            raise Exception('Cannot build city, node.player did not equal player')
        player.build_city()
        node.type = BuildType.City
        player.settlements.discard(node)
        for tile in node.resources:
            if tile is not None:
                player.resource_rates[tile.resource.value] += tile.chance

    def move_robber(self, new_robber_tile):
        self.robber_tile.disabled = False
        self.robber_tile = new_robber_tile
        self.robber_tile.disabled = True
        print("\t\t\tRobber was moved to tile " + str(self.layout.index(self.robber_tile)))

    def setup(self, player_strategies, board_layout):
        for i in range(len(player_strategies)):
            player_id = i + 1
            self.players.append(Player(player_id, player_strategies[i]))
        self.players = random.sample(self.players, len(self.players))
        for player in self.players:
            print(player.id)
        if board_layout == 'random':
            resources = [Resource.Lumber, Resource.Wool, Resource.Grain] * 4 + [Resource.Brick, Resource.Ore] * 3 + [Resource.Desert]
            number_tokens = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
            resources = random.sample(resources, len(resources))
            number_tokens = random.sample(number_tokens, len(number_tokens))
        elif board_layout == 'basic':
            resources = [Resource.Lumber, Resource.Wool, Resource.Grain, \
            Resource.Brick, Resource.Ore, Resource.Brick, Resource.Wool, \
            Resource.Desert, Resource.Lumber, Resource.Grain, Resource.Lumber, Resource.Grain, \
            Resource.Brick, Resource.Wool, Resource.Wool, Resource.Ore, \
            Resource.Ore, Resource.Grain, Resource.Lumber]
            number_tokens = [11, 12, 9, 4, 6, 5, 10, 3, 11, 4, 8, 8, 10, 9, 3, 5, 2, 6]

        edges_dict = {}
        nodes_dict = {}
        upper_left = [(1, 2), (1, 4), (1, 6), (3, 1), (3, 3), (3, 5), (3, 7), (5, 0), (5, 2), (5, 4), (5, 6), (5, 8), (7, 1), (7, 3), (7, 5), (7, 7), (9, 2), (9, 4), (9, 6) ]
        edge_order = [(1, 2), (0, 2), (0, 1), (1, 0), (2, 0), (2, 1)]
        self.layout = [None] * len(upper_left)
        desert_count = 0
        for k in range(len(upper_left)):
            x = upper_left[k][0]
            y = upper_left[k][1]
            node_keys = [(x, y), (x - 1, y + 1), (x, y + 2), (x + 1, y + 2), (x + 2, y + 1), (x + 1, y)]
            edge_keys = [None] * 6;
            number = None
            if resources[k] == Resource.Desert:
                desert_count = 1
                number = 7
                self.layout[k] = Tile(resources[k], number, [None] * 6, True)
                self.robber_tile = self.layout[k]
            else:
                number = number_tokens[k - desert_count]
                self.layout[k] = Tile(resources[k], number, [None] * 6)

            for i in range(6):
                j = (i + 1) % 6
                edge_keys[i] = (node_keys[i][0] + node_keys[j][0], node_keys[i][1] + node_keys[j][0]);
                node = None;
                if (node_keys[i] not in nodes_dict):
                    node = Node(set(), [None] * 3, node_keys[i][0], node_keys[i][1])
                    nodes_dict.update({node_keys[i]: node})
                else:
                    node = nodes_dict.get(node_keys[i])
                self.layout[k].nodes[i] = node
            for i in range(6):
                if (edge_keys[i] not in edges_dict):
                    j = (i + 1) % 6
                    edge = Edge()
                    edge.add_nodes(nodes_dict.get(node_keys[i]), nodes_dict.get(node_keys[j]))
                    edges_dict.update({edge_keys[i]: edge})
            for i in range(6):
                j = (i - 1) % 6
                node = nodes_dict.get(node_keys[i])
                node.resources.add(self.layout[k])
                node.edges[edge_order[i][0]] = edges_dict.get(edge_keys[j])
                node.edges[edge_order[i][1]] = edges_dict.get(edge_keys[i])
        self.edges = list(edges_dict.values())
        self.nodes = list(nodes_dict.values())

class EdgeType(Enum):
    Left = 1
    Center = 2
    Right = 3

class Tile:
    def __init__(self, resource, value, adj_nodes, disabled = False):
        self.resource = resource
        self.value = value
        self.nodes = adj_nodes
        #if the robber is on the tile, disable it
        self.disabled = disabled
        # chance of rolling the tile value
        self.chance = 0
        if value <= 7:
            self.chance = value - 1
        else:
            self.chance = 13 - value

    def distribute(self, roll_value):
        if self.value == roll_value:
            if self.disabled:
                for node in self.nodes:
                    if node.type == BuildType.Settlement:
                        print("\t\t\tPlayer " + str(node.player.id) + " would have gotten 1 of resource " + str(self.resource) + " but the robber was placed on the tile")
                    elif node.type == BuildType.City:
                        print("\t\t\tPlayer " + str(node.player.id) + " would have gotten 2 of resource " + str(self.resource) + " but the robber was placed on the tile")
            else:
                for node in self.nodes:
                    if node.type == BuildType.Settlement:
                        print("\t\t\tPlayer " + str(node.player.id) + " got 1 of resource " + str(self.resource))
                        node.player.resources[self.resource] += 1
                    elif node.type == BuildType.City:
                        print("\t\t\tPlayer " + str(node.player.id) + " got 2 of resource " + str(self.resource))
                        node.player.resources[self.resource] += 2
