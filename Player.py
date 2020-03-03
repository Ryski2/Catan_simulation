from enum import Enum
import random

#for storing player states
class Player:
    def __init__(self, id = None):
        self.id = id
        
        self.resources = \
        {
          Resource.Lumber : 0,
          Resource.Wool : 0,
          Resource.Ore : 0,
          Resource.Grain : 0,
          Resource.Brick : 0
        }
        
        self.settlementCount = 0
        self.cityCount = 0
        self.longestRoad = 0
        self.locations = []

    def points(self):
        return self.settlementCount + self.cityCount * 2 + self.longestRoad

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

    def can_build_city(self):
        return self.resources[Resource.Ore] >= 3 and self.resources[Resource.Grain] >= 2 and self.settlementCount >= 1
        
    def build_city(self):
        self.resources[Resource.Ore] -= 3
        self.resources[Resource.Grain] -= 2
        self.settlementCount -= 1
        self.cityCount += 1

    def total_resources(self):
        return sum(self.resources.values())

    def discard_half(self):
        num_discards = self.total_resources() // 2
        discarded = 0
        while (discarded < num_discards):
            res = Resource(random.randint(1,5))
            if self.resources[res] > 0:
                self.resources[res] -= 1
                discarded += 1

                
class Resource(Enum):
    Desert = 0
    Lumber = 1
    Wool = 2
    Ore = 3
    Grain = 4
    Brick = 5
    def __str__(self):
        return self.name