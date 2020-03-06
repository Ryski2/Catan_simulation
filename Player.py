from enum import Enum
from Globals import v_print
import math
import random
import sys

#for storing player states
class Player:
    def __init__(self, id, strategies):
        self.id = id

        # The player's game strategy, default strategy being None
        self.strategies = strategies

        self.resources = \
        {
          Resource.Lumber : 4,
          Resource.Wool : 2,
          Resource.Ore : 0,
          Resource.Grain : 2,
          Resource.Brick : 4
        }

        self.roadCount = 0
        self.settlementCount = 0
        self.cityCount = 0
        self.longestRoad = 0
        self.locations = []

        # keep track of edges and nodes belonging to the player
        self.edges = set()
        self.nodes = set()
        self.settlements = set()

        # keep track of free edges and nodes available to the player
        self.buildable_edges = set()
        self.buildable_nodes = set()

        # rates of obtaining resources
        # 6 resources, including Desert
        self.resource_rates = [0] * 6


    def points(self):
        return self.settlementCount + self.cityCount * 2 + self.longestRoad

    def win(self):
        return self.points() >= 10

    def can_build_settlement(self):
        return self.resources[Resource.Lumber] >= 1 and self.resources[Resource.Brick] >= 1 and self.resources[Resource.Wool] >= 1 and self.resources[Resource.Grain] >= 1

    def build_settlement(self):
        self.resources[Resource.Lumber] -= 1
        self.resources[Resource.Brick] -= 1
        self.resources[Resource.Wool] -= 1
        self.resources[Resource.Grain] -= 1
        self.settlementCount += 1

    def can_build_road(self):
        return self.resources[Resource.Lumber] >= 1 and self.resources[Resource.Brick] >= 1

    def build_road(self):
        self.resources[Resource.Lumber] -= 1
        self.resources[Resource.Brick] -= 1
        self.roadCount += 1

    def can_build_city(self):
        return self.resources[Resource.Ore] >= 3 and self.resources[Resource.Grain] >= 2 and self.settlementCount >= 1

    def build_city(self):
        self.resources[Resource.Ore] -= 3
        self.resources[Resource.Grain] -= 2
        self.settlementCount -= 1
        self.cityCount += 1

    def total_resources(self):
        return sum(self.resources.values())

    # TRADING
    # trade most-had resource for least-had resource
    def trade_with_player(self, other, resource_out, resource_in, out_number, in_number):
        if self.resources[resource_out] < out_number or other.resources[resource_in] < in_number:
            sys.exit("trade_with_player: not enough resource to trade with player")
        v_print("Player " + str(self.id) + " Before - ", 4)
        for resource in self.resources:
                v_print("\t" + str(resource)+ ": " + str(self.resources[resource]), 4)

        v_print("Player " + str(other.id) + " Before - ", 4)
        for resource in other.resources:
                v_print("\t" + str(resource)+ ": " + str(other.resources[resource]), 4)

        self.resources[resource_out] -= out_number
        self.resources[resource_in] += in_number
        other.resources[resource_out] += out_number
        other.resources[resource_in] -= in_number

        v_print("\t\t\tPlayer " + str(self.id) + " traded " + str(out_number) + " " + str(resource_out) + " for " + str(in_number) + " " + str(resource_in) + " with Player " + str(other.id), 4)

        v_print("Player " + str(self.id) + " After - ", 4)
        for resource in self.resources:
                v_print("\t" + str(resource)+ ": " + str(self.resources[resource]), 4)

        v_print("Player " + str(other.id) + " After - ", 4)
        for resource in other.resources:
                v_print("\t" + str(resource)+ ": " + str(other.resources[resource]), 4)

    def trade_four_one(self, resource_out, resource_in, in_number):
        v_print("Player " + str(self.id) + " Before - ", 4)
        for resource in self.resources:
                v_print("\t" + str(resource)+ ": " + str(self.resources[resource]), 4)

        if self.resources[resource_out] < in_number * 4:
            sys.exit("trade_four_one: not enough resource to trade")
        self.resources[resource_out] -= in_number * 4
        self.resources[resource_in] += in_number

        v_print("\t\t\tPlayer " + str(self.id) + " traded " + str(in_number * 4) + " " + str(resource_out) + " for " + str(in_number) + " " + str(resource_in) + " with the Bank", 4)

        v_print("Player " + str(self.id) + " Before - ", 4)
        for resource in self.resources:
            v_print("\t" + str(resource)+ ": " + str(self.resources[resource]), 4)

    def get_max_min_resource(self):
        max_resource = None
        max_count = -math.inf
        min_resource = None
        min_count = math.inf
        for resource in self.resources:
            count = self.resources[resource]
            if count > max_count:
                max_resource = resource
                max_count = count
            if count < min_count:
                min_resource = resource
                min_count = count
        return (max_resource, min_resource)
    # TRADING

class Resource(Enum):
    Desert = 0
    Lumber = 1
    Wool = 2
    Ore = 3
    Grain = 4
    Brick = 5
    def __str__(self):
        return self.name
    __repr__ = __str__

class Strategies(Enum):
    Dummy = 1
    Trade = 2
    Prioritize_Settlements = 3 #if there is a place to build a settlement, don't build a road
    Road_Settlement_Ratio = 4 #don't build a road if the ratio of roads to settlements and cities exceeds a threshold
    Build_All = 5 #build as many times as possible every turn.
    Avoid_Shore_and_Desert = 6
    Adjust_Resource_Rates = 7 # not compatible with Avoid_Shore_and_Desert

    def __str__(self):
        return self.name
    __repr__ = __str__
