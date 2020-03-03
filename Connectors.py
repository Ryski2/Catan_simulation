from enum import Enum

# For settlements, cities
class Node:
    def __init__(self, nearby, edges, rowNum, columnNum, player=None):
        #dictionary of resources and attached rolls?
        self.resources = nearby

        #edges convention: 0th index is left, 1st index is center, 2nd index is right
        self.edges = edges
        
        self.row = rowNum
        self.column = columnNum
        self.player = player
        
        self.type = BuildType.Empty

    def get_coords(self):
        return "(" + str(self.row) + ", " + str(self.column) + ")"

#edge class for roads
class Edge:
    def __init__(self):
        #if player is assigned, road exists, possibly add additional variables if checking for null is problematic
        self.player = None
        self.node1 = None
        self.node2 = None

    def build_road(self, playerid):
        self.player = playerid

    def add_nodes(self, start, end):
        self.node1 = start
        self.node2 = end
    #possibly add a method to include node location in the edge?
    #should be able to extract it from self.node1.row and self.node1.column
    
class BuildType(Enum):
    Empty = 0
    Settlement = 1
    City = 2