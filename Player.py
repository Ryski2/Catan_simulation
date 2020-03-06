from enum import Enum
import math
import random

#for storing player states
class Player:
    def __init__(self, id, strategies, build_ratio = 0):
        self.id = id

        # The player's game strategy, default strategy being None
        self.strategies = strategies

        if Strategies.RoadSettlementRatio in strategies:
            if build_ratio != 0:
                self.build_ratio = build_ratio
            else:
                raise ValueError("If using RoadSettlementRatio need to provide a build ratio for each player")

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
    def trade_with_player(self, other):
        max_res, min_res = self.__get_max_min_resource()
        if max_res != min_res:
            if other.resources[max_res] < other.resources[min_res]:
                self.resources[max_res] -= 1
                self.resources[min_res] += 1
                other.resources[max_res] += 1
                other.resources[min_res] -= 1

    def trade_four_one(self):
        max_res, min_res = self.__get_max_min_resource()
        if self.resources[max_res] > self.resources[min_res] + 4:
            self.resources[max_res] -= 4
            self.resources[min_res] += 1

    def __get_max_min_resource(self):
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

class Strategies(Enum):
    #Basic = 1
    Dummy = 1
    Trade = 2
    PrioritizeSettlements = 3 #if there is a place to build a settlement, don't build a road
    RoadSettlementRatio = 4 #don't build a road if the ratio of roads to settlements and cities exceeds a threshold
