from Board import Board
from Connectors import BuildType
from Player import Resource
from Player import Strategies
import random
import itertools

max_turns = 200

class Simulation:
    def __init__(self, player_strategies = [None] * 4, board_layout = "random"):
        self.board = Board(player_strategies, board_layout)

    def run(self):
        winner = None
        while self.board.turns <= max_turns and winner is None:
            winner = self.game_turn()
        self.print_results(winner)

    def game_turn(self):
        turns = self.board.turns
        if turns == 0:
            print()
            print("Players placing initial settlements and roads")
            print("---------------------------------------------")
            print()
            for player in self.board.players:
                self.build(player)
            # on second placement, players get the resources bordering their settlement
            for player in reversed(self.board.players):
                self.build(player)
            for roll in range(1, 12):
                if roll != 7:
                    self.board.distribute(roll)
            print()
            print("Moving on to main game section")
            print("---------------------------------------------")
            print()
        else:
            print("Round " + str(self.board.turns))
            for player in self.board.players:
                print("\tPlayer " + str(player.id) + "'s Turn")
                roll = self.board.dice_roll(player)
                if roll == 7:
                    for player1 in self.board.players:
                        resources = player1.total_resources()
                        if player1.total_resources() > 7:
                            self.discard_half(player1)
                            print("\t\t\tPlayer " + str(player1.id) + " had " + str(resources) + " resources and now has " + str(player1.total_resources()))
                        else:
                            print("\t\t\tPlayer " + str(player1.id) + " has " + str(resources) + " resources. No cards are discarded")
                    self.move_robber(player)
                    self.steal(player)
                else:
                    self.board.distribute(roll)
                self.trade(player)
                self.build(player)
                if player.win():
                    return player
        self.board.turns += 1

    def trade(self, player):
        strategies = player.strategies
        if Strategies.Trade in strategies:
            # trade with other players
            for other_player in self.board.players:
                if other_player is not player:
                    max_res, min_res = player.get_max_min_resource()
                    if max_res != min_res:
                        if other_player.resources[max_res] < other_player.resources[min_res]:
                            player.trade_with_player(other_player, max_res, min_res, 1, 1)
            # trade 4:1
            max_res, min_res = player.get_max_min_resource()
            if player.resources[max_res] > player.resources[min_res] + 4:
                player.trade_four_one(max_res, min_res, 1)

    def build(self, player):
        owned_nodes = player.nodes
        owned_edges = player.edges
        if self.board.turns == 0:
            buildable_nodes = self.board.buildable_nodes
            buildable_edges = self.board.buildable_edges
        else:
            buildable_nodes = player.buildable_nodes
            buildable_edges = player.buildable_edges
        if self.board.turns == 0:
            node_to_build = None
            edge_to_build = None
            while edge_to_build is None:
                node_to_build = self.find_valid_settlement_location(player, buildable_nodes)
                for edge in random.sample(node_to_build.edges, len(node_to_build.edges)):
                    if edge is not None and edge.player is None:
                        edge_to_build = edge
                        break
            self.board.build_road(player, edge_to_build)
            self.board.build_settlement(player, node_to_build)
        else:
            if player.can_build_city():
                #pick location to build
                if len(player.settlements) != 0:
                    city_node = random.sample(player.settlements, 1)[0]
                    self.board.build_city(player, city_node)
                else:
                    print("\t\tPlayer " + str(player.id) + " had resources to bulid a city but no valid location was found")
                #print("\t\tPlayer " + str(player.id) + " built a city at " + city_node.get_coords())
            if player.can_build_settlement():
                if len(buildable_nodes) != 0:
                    settlement_node = self.find_valid_settlement_location(player, buildable_nodes)
                    self.board.build_settlement(player, settlement_node)
                else:
                    print("\t\tPlayer " + str(player.id) + " had resources to bulid a settlement but no valid location was found")
            if player.can_build_road() and len(player.buildable_nodes) == 0: #####
                if len(buildable_edges) != 0:
                    rode_edge = self.find_valid_road_location(player, buildable_edges)
                    self.board.build_road(player, rode_edge)
                else:
                    print("\t\tPlayer " + str(player.id) + " had resources to bulid a road but no valid location was found")


    # defauld building strategy
    def build_default(self, player, owned_nodes, owned_edges, buildable_nodes, buildable_edges):
        if self.board.turns == 0:
            node_to_build = None
            edge_to_build = None
            while edge_to_build is None:
                node_to_build = random.sample(buildable_nodes, 1)[0]
                for edge in random.sample(node_to_build.edges, len(node_to_build.edges)):
                    if edge is not None and edge.player is None:
                        edge_to_build = edge
                        break
            self.board.build_road(player, edge_to_build)
            self.board.build_settlement(player, node_to_build)
        else:
            if player.can_build_city():
                #pick location to build
                if len(player.settlements) != 0:
                    city_node = random.sample(player.settlements, 1)[0]
                    self.board.build_city(player, city_node)
                else:
                    print("\t\tPlayer " + str(player.id) + " had resources to bulid a city but no valid location was found")
                #print("\t\tPlayer " + str(player.id) + " built a city at " + city_node.get_coords())
            if player.can_build_settlement():
                if len(buildable_nodes) != 0:
                    settlement_node = random.sample(buildable_nodes, 1)[0]
                    self.board.build_settlement(player, settlement_node)
                else:
                    print("\t\tPlayer " + str(player.id) + " had resources to bulid a settlement but no valid location was found")
            if player.can_build_road() and len(player.buildable_nodes) == 0: #####
                if len(buildable_edges) != 0:
                    rode_edge = random.sample(buildable_edges, 1)[0]
                    self.board.build_road(player, rode_edge)
                else:
                    print("\t\tPlayer " + str(player.id) + " had resources to bulid a road but no valid location was found")

    def find_valid_settlement_location(self, player, buildable_nodes):
        strategies = player.strategies
        if Strategies.Avoid_Shore_and_Desert in strategies:
            node_choices = [None] * 3
            for node in random.sample(buildable_nodes, len(buildable_nodes)):
                valid_tile_count = 0 # 0 <= valid_tile_count <= 3
                for tile in node.resources:
                    if tile.resource is not Resource.Desert:
                        valid_tile_count += 1
                if valid_tile_count == 3:
                    return node
                elif node_choices[valid_tile_count] is None:
                    node_choices[valid_tile_count] = node
            for node in reversed(node_choices):
                if node is not None:
                    return node
        else: # default strategy
            return random.sample(buildable_nodes, 1)[0]

    def find_valid_road_location(self, player, buildable_edges):
        strategies = player.strategies
        if Strategies.Avoid_Shore_and_Desert in strategies:
            edge_choices = [None] * 3
            for edge in random.sample(buildable_edges, len(buildable_edges)):
                new_node = edge.node1
                for neighbor_edge in edge.node1.edges:
                    if neighbor_edge is not None and neighbor_edge.player is player:
                        new_node = edge.node1
                valid_tile_count = 0
                for tile in new_node.resources:
                    if tile.resource is not Resource.Desert:
                        valid_tile_count += 1
                if valid_tile_count == 3:
                    return edge
                elif edge_choices[valid_tile_count] is None:
                    edge_choices[valid_tile_count] = edge
            for edge in reversed(edge_choices):
                if edge is not None:
                    return edge


        else:
            return random.sample(buildable_edges, 1)[0]

    def discard_half(self, player):
        strategies = player.strategies
        if Strategies.Dummy in strategies:
            """ADD STRATEGIES HERE"""
            raise NotImplementedError()

        else: # Default strategy
            num_discards = player.total_resources() // 2
            discarded = 0
            while (discarded < num_discards):
                res = Resource(random.randint(1,5))
                if player.resources[res] > 0:
                    player.resources[res] -= 1
                    discarded += 1

    def move_robber(self, player):
        strategies = player.strategies
        if Strategies.Dummy in strategies:
            """ADD STRATEGIES HERE"""
            raise NotImplementedError()

        else: # Default strategy
            new_robber_tile = self.board.robber_tile
            index = -1
            while new_robber_tile == self.board.robber_tile:
                new_robber_tile = random.choice(self.board.layout)
            self.board.move_robber(new_robber_tile)

    # "The person moving the robber must steal a card from a player adjacent to the robber if possible."
    def steal(self, player):
        stole_resource = False
        other_player = None
        res = None
        strategies = player.strategies
        if Strategies.Dummy in strategies:
            """ADD STRATEGIES HERE"""
            raise NotImplementedError()

        else: # Default strategy
            for node in random.sample(self.board.robber_tile.nodes, 6):
                other_player = node.player
                if other_player is not None and other_player is not player:
                    res = Resource(random.randint(1, 5))
                    if other_player.resources[res] > 0:
                        stole_resource = True
                        break
        if stole_resource:
            other_player.resources[res] -= 1
            player.resources[res] += 1
            print("\t\t\tPlayer " + str(player.id) + " stole one " + str(res) + " from Player " + str(other_player.id))
        else:
            print("\t\t\tNo resource to steal")

    def print_results(self, winner):
        print("Game Ended")
        print("---------------------------------------------")
        for player in self.board.players:
            #print every players settlements, roads, and cities
            print("Player " + str(player.id) + ": ")
            print("\tSettlement Locations:")
            for node in player.nodes:
                if node.type == BuildType.Settlement:
                    print("\t\t" + node.get_coords())
            print("\tCity Locations:")
            for node in player.nodes:
                if node.type == BuildType.City:
                    print("\t\t" + node.get_coords())
            print("\tEdge Between:")
            for edge in player.edges:
                print("\t\t" + edge.node1.get_coords() + " to " + edge.node2.get_coords())

        if winner is not None:
            print("Player " + str(winner.id) + " Won After " + str(self.board.turns) + " Turns")
        else:
            print("After " + str(max_turns) + " turns, no one has reached 10 points")
            highest_score = -1
            for player in self.board.players:
                if player.points() >= highest_score:
                    highest_score = player.points()
            winners = []
            for player in self.board.players:
                if player.points() == highest_score:
                    winners.append(player.id)
            print("Player(s) " + ", ".join(str(p) for p in winners) + " had the most points, with " + str(highest_score) + " points")
        print()
        for player in self.board.players:
            print("Player " + str(player.id))
            for resource in player.resources:
                print("\t" + str(resource)+ ": " + str(player.resources[resource]))
