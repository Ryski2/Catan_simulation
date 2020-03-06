from Board import Board
from Connectors import BuildType
from Player import Resource
from Player import Strategies
from Globals import v_print
import numpy as np
import random
import itertools

max_turns = 200

class Simulation:
    def __init__(self, player_strategies, board_layout, random_order):
        self.board = Board(player_strategies, board_layout, random_order)


    def run(self):
        winner = None
        while self.board.turns <= max_turns and winner is None:
            winner = self.game_turn()
        self.print_results(winner)
        points = np.zeros(4)
        for player in self.board.players:
            points[player.id - 1] = player.points()
        return self.board.turns, points

    def game_turn(self):
        turns = self.board.turns
        if turns == 0:
            v_print("", 2)
            v_print("Players placing initial settlements and roads", 2)
            v_print("---------------------------------------------", 2)
            v_print("", 2)
            for player in self.board.players:
                self.build(player);
            # on second placement, players get the resources bordering their settlement
            for player in reversed(self.board.players):
                self.build(player);
            for roll in range(2, 13):
                if roll != 7:
                    self.board.distribute(roll)
            v_print("", 2)
            v_print("Moving on to main game section", 2)
            v_print("---------------------------------------------", 2)
            v_print("", 2)
        else:
            v_print("Round " + str(self.board.turns), 2)
            for player in self.board.players:
                v_print("\tPlayer " + str(player.id) + "'s Turn", 2)
                roll = self.board.dice_roll(player)
                if roll == 7:
                    for player1 in self.board.players:
                        resources = player1.total_resources()
                        if player1.total_resources() > 7:
                            self.discard_half(player1)
                            v_print("\t\t\tPlayer " + str(player1.id) + " had " + str(resources) + " resources and now has " + str(player1.total_resources()), 4)
                        else:
                            v_print("\t\t\tPlayer " + str(player1.id) + " has " + str(resources) + " resources. No cards are discarded", 4)
                    self.move_robber(player)
                    self.steal(player)
                else:
                    self.board.distribute(roll)
                self.trade(player)
                if Strategies.Build_All in player.strategies:
                    settlementCount = player.settlementCount
                    cityCount = player.cityCount
                    roadCount = player.roadCount
                    count = 0
                    while (settlementCount != player.settlementCount) \
                            or (cityCount != player.cityCount) \
                            or (roadCount != player.roadCount) or count == 0:
                        settlementCount = player.settlementCount
                        cityCount = player.cityCount
                        roadCount = player.roadCount
                        self.build(player)
                        count += 1
                else:
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


        # Default strategy: no trading

    def build(self, player):
        owned_nodes = player.nodes
        owned_edges = player.edges
        strategies = player.strategies
        if self.board.turns == 0:
            buildable_nodes = self.board.buildable_nodes;
            buildable_edges = self.board.buildable_edges;
            node_to_build = None
            edge_to_build = None
            while edge_to_build is None:
                node_to_build = self.find_valid_settlement_or_city_location(player, buildable_nodes)
                for edge in random.sample(node_to_build.edges, len(node_to_build.edges)):
                    if edge is not None and edge.player is None:
                        edge_to_build = edge
                        break
            self.board.build_road(player, edge_to_build)
            self.board.build_settlement(player, node_to_build)
        else:
            buildable_nodes = player.buildable_nodes;
            buildable_edges = player.buildable_edges;
            possible_cities = set()
            possible_settlements = set()
            if player.can_build_city():
                possible_cities = player.settlements
            if player.can_build_settlement():
                possible_settlements = buildable_nodes
            possible_nodes = possible_cities.union(possible_settlements)
            if len(possible_nodes) != 0:
                node = self.find_valid_settlement_or_city_location(player, possible_nodes)
                if node is not None:
                    if node.player is player:
                        self.board.build_city(player, node)
                    else:
                        self.board.build_settlement(player, node)
            build_road = player.can_build_road()
            if Strategies.Prioritize_Settlements in strategies:
                build_road = build_road and len(player.buildable_nodes) == 0
            if Strategies.Road_Settlement_Ratio in strategies:
                road_settlement_ratio = strategies.get(Strategies.Road_Settlement_Ratio)
                build_road = build_road and player.cityCount > player.roadCount / road_settlement_ratio
            if build_road:
                if len(buildable_edges) != 0:
                    rode_edge = self.find_valid_road_location(player, buildable_edges)
                    self.board.build_road(player, rode_edge)
                else:
                    v_print("\t\tPlayer " + str(player.id) + " had resources to bulid a road but no valid location was found", 3)

    def build_road_or_not(self, player):
        build_road = player.can_build_road()
        strategies = player.strategies
        if Strategies.Prioritize_Settlements in strategies:
            build_road = build_road and len(player.buildable_nodes) == 0
        if Strategies.Road_Settlement_Ratio in strategies:
            road_settlement_ratio = strategies.get(Strategies.Road_Settlement_Ratio)
            build_road = build_road and player.cityCount > player.roadCount / road_settlement_ratio
        return build_road

    def find_valid_settlement_or_city_location(self, player, buildable_nodes):
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
        elif Strategies.Adjust_Resource_Rates in strategies:
            node_choice = None
            max_value = - float("inf") # larger value is better
            for node in buildable_nodes:
                value = self.__calculate_value_of_node(player, node)
                if value > max_value:
                    max_value = value
                    node_choice = node
            return node_choice
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
        elif Strategies.Adjust_Resource_Rates in strategies:
            # index 0 stores the best of edges with unbuildable new nodes
            # index 1 stores the best of edges with buildable new nodes
            edge_choices = [None] * 2
            max_values = [- float("inf")] * 2
            for edge in buildable_edges:
                new_node = edge.node1
                for neighbor_edge in edge.node1.edges:
                    if neighbor_edge is not None and neighbor_edge.player is player:
                        new_node = edge.node1
                value = self.__calculate_value_of_node(player, new_node)
                index = 0
                if new_node in self.board.buildable_nodes:
                    index = 1
                if value > max_values[index]:
                    max_values[index] = value
                    edge_choices[index] = edge
                if edge_choices[1] is not None:
                    return edge_choices[1]
                else:
                    return edge_choices[0]
        else:
            return random.sample(buildable_edges, 1)[0]

    # function for Strategies.Adjust_Resource_Rates
    def __calculate_value_of_node(self, player, node):
        strategy_data = player.strategies.get(Strategies.Adjust_Resource_Rates)
        ideal_ratio = strategy_data[0] # assumed ideal ratio of resource rates
        k = strategy_data[1] # some arbtriary constant
        new_ratio = list.copy(player.resource_rates)
        # how good the new ratio agrees with the ideal ratio
        # the lower, the better
        ratio_value = 0
        # sum of rate of obtaining each resource, excluding desert
        rate = 0
        for tile in node.resources:
            if tile is not None and tile.resource is not Resource.Desert:
                new_ratio[tile.resource.value] += tile.chance
                rate += tile.chance
        s = sum(new_ratio)
        if s == 0:
            return - float("inf")
        normalizer =  sum(ideal_ratio) / s
        ratio_value = 0 # Goodness of the current node. The smaller the value, the better the node.
        for i in range(1, 5): # ingore desert
            diff = ideal_ratio[i] - new_ratio[i] * normalizer
            ratio_value += diff * diff
        rate = rate / 36 # now rate becomes the expected nnmber of resources the player gets each round
        value = rate * rate - k * ratio_value / 5 # here k is an arbtriary value
        return value

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
            v_print("\t\t\tPlayer " + str(player.id) + " stole one " + str(res) + " from Player " + str(other_player.id), 4)
        else:
            v_print("\t\t\tNo resource to steal", 4)

    def print_results(self, winner):
        v_print("Game Ended", 2)
        v_print("---------------------------------------------", 2)
        for player in self.board.players:
            #print every players settlements, roads, and cities
            v_print("Player " + str(player.id) + ": ", 2)
            v_print("\tSettlement Locations:", 2)
            for node in player.nodes:
                if node.type == BuildType.Settlement:
                    v_print("\t\t" + node.get_coords(), 2)
            v_print("\tCity Locations:", 2)
            for node in player.nodes:
                if node.type == BuildType.City:
                    v_print("\t\t" + node.get_coords(), 2)
            v_print("\tEdge Between:", 2)
            for edge in player.edges:
                v_print("\t\t" + edge.node1.get_coords() + " to " + edge.node2.get_coords(), 2)

        if winner is not None:
            v_print("Player " + str(winner.id) + " Won After " + str(self.board.turns) + " Turns", 1)
        else:
            v_print("After " + str(max_turns) + " turns, no one has reached 10 points", 1)
            highest_score = -1
            for player in self.board.players:
                if player.points() >= highest_score:
                    highest_score = player.points()
            winners = []
            for player in self.board.players:
                if player.points() == highest_score:
                    winners.append(player.id)
            v_print("Player(s) " + ", ".join(str(p) for p in winners) + " had the most points, with " + str(highest_score) + " points", 1)
        v_print("", 1)
        for player in self.board.players:
            v_print("Player " + str(player.id), 2)
            for resource in player.resources:
                v_print("\t" + str(resource)+ ": " + str(player.resources[resource]), 2)
