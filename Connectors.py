from enum import Enum

# For settlements, cities
class Node:
    def __init__(self, adj_resources, edges, rowNum, columnNum):
        #dictionary of resources and attached rolls?
        self.resources = adj_resources

        #edges convention: use enum in Board.py
        self.edges = edges

        self.row = rowNum
        self.column = columnNum
        self.player = None

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

    def build_road(self, player):
        self.player = player

    def get_other_node(self, node):
        if self.node1 is not node:
            return self.node1
        else:
            return self.node2

    def add_nodes(self, start, end):
        self.node1 = start
        self.node2 = end
    #possibly add a method to include node location in the edge?
    #should be able to extract it from self.node1.row and self.node1.column

class BuildType(Enum):
    Empty = 0
    Settlement = 1
    City = 2
