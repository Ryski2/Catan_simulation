#!/usr/bin/env python
# coding: utf-8

import random

game_board = []
players = []
nodes = []
edges = []

# For settlements, cities
class node:
    def __init__(self, nearby, edges, rowNum, columnNum, player=None):
        #dictionary of resources and attached rolls?
        self.resources = nearby

        #edges convention: 0th index is left, 1st index is center, 2nd index is right
        self.edges = []
        
        self.row = rowNum
        self.column = columnNum
        self.player = player
        #0 for empty, 1 for settlement, 2 for city
        self.type = 0

    def get_coords():
        return "(" + str(self.row) + ", " + str(self.column) + ")"

#edge class for roads
class edge:
    def __init__(self):
        #if player is assigned, road exists, possibly add additional variables if checking for null is problematic
        self.player = None
        self.node1 = None
        self.node2 = None

    def build_road(playerid):
        self.player = playerid

    def add_nodes(start, end):
        self.node1 = start
        self.node2 = end
    #possibly add a method to include node location in the edge?
    #should be able to extract it from self.node1.row and self.node1.column

#possibly temporary, seems useful for quickly assigning resources
class tile:
    def __init__(self,resource, value):
        self.resource = resource
        self.value = value
        self.players = []

    def distribute(roll_value):
        if this.value == roll_value:
            for person in players:
                if self.resource == "Lumber":
                    person.lumberCount += 1
                elif self.resource == "Wool":
                    person.woolCount += 1
                elif self.resource == "Ore":
                    person.oreCount += 1
                elif self.resource == "Grain":
                    person.grainCount += 1
                elif self.resource == "Brick":
                    person.brickCount += 1

# Only if a data structure is needed to store tiles/ nodes + edges
class board:
    def __init__(self, dataval = None):
        self.layout = []

#for storing player states
class player:
    def __init__(self, dataval = None):
        self.ID = dataval
        self.lumberCount = 0
        self.woolCount = 0
        self.oreCount = 0
        self.grainCount = 0
        self.brickCount = 0
        self.setCount = 0
        self.cityCount = 0
        self.longestRoad = 0
        self.locations = []

    def points():
        return self.setCount + self.cityCount * 2 + self.longestRoad

    def can_build_set():
        return self.lumberCount >= 1 and self.brickCount >= 1 and self.woolCount >= 1 and self.grainCount >= 1

    def build_set():
        self.lumberCount -= 1
        self.brickCount -= 1
        self.woolCount -= 1
        self.grainCount -= 1
        self.setCount += 1

    def can_build_road():
        return self.lumberCount >= 1 and self.brickCont >= 1
    
    def build_road():
        self.lumberCount -= 1
        self.brickCount -= 1

    def can_build_city():
        return self.oreCount >= 3 and self.grainCount >= 2 and self.setCount >= 1
        
    def build_city():
        self.oreCount -= 3
        self.grainCount -= 2
        self.setCount -= 1
        self.cityCount += 1

    def total_resources():
        return self.lumberCount + self.woolCount + self.oreCount + self.grainCount + self.brickCount

    def discard_half():
        discards = player.total_resources() // 2
            for i in range(0, discards):
                resource = random.randint(1,5)
                if resource == 1:
                    lumberCount -= 1
                elif resource == 2:
                    woolCount -= 1
                elif resource == 3:
                    oreCount -= 1
                elif resouce == 4:
                    grainCount -= 1
                else:
                    brickCount -= 1

def setup():
    game_board = board()
    tile1 = tile("Lumber", 11)
    tile2 = tile("Wool", 12)
    tile3 = tile("Grain", 9)
    tile4 = tile("Brick", 4)
    tile5 = tile("Ore", 6)
    tile6 = tile("Brick", 5)
    tile7 = tile("Wool", 10)
    tile8 = tile("Desert", 7)
    tile9 = tile("Lumber", 3)
    tile10 = tile("Grain", 11)
    tile12 = tile("Lumber", 4)
    tile13 = tile("Grain", 8)
    tile14 = tile("Brick", 8)
    tile15 = tile("Wool", 10)
    tile16 = tile("Wool", 9)
    tile17 = tile("Ore", 3)
    tile18 = tile("Ore", 5)
    tile19 = tile("Grain", 2)
    tile20 = tile("Lumber", 6)
    order = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, tile10, tile11, tile12, tile13, tile14, tile15, tile16, tile17, tile18, tile19, tile20]
    basic.layout = order
    player1 = player(1)
    player2 = player(2)
    player3 = player(3)
    player4 = player(4)
    player = [player1, player2, player3, player4]

    # Create a list for storing edges. Edge location shown in basic_layout.png
    edges = [edge() for i in range(72)]
    node_1_2 = node({11 : "Lumber"}, None, edges[0], edges[1], 1, 2)
    node_0_3 = node({11 : "Lumber"}, edges[1], None, edges[2], 0, 3)
    node_1_4 = node({11 : "Lumber", 12: "Wool"}, edges[2], edges[3], edges[4], 1,4)
    node_0_5 = node({12 : "Wool"}, edges[4], None, edges[5], 0,5)
    node_1_6 = node({12 : "Wool", 9 : "Grain"}, edges[5], edges[6], edges[7], 1,6)
    node_0_7 = node({9 : "Grain"}, edges[7], None, edges[8], 0,7)
    node_1_8 = node({9 : "Grain"}, edges[8], edges[9], None, 1, 8)
    node_2_8 = node({9 : "Grain", 10 : "Wool"}, edges[20], edges[9], edges[21],2,8)
    node_3_7 = node({9 : "Grain", 10 : "Wool", 5 : "Brick"},edges[18],edges[19], edges[20],3,7)
    node_2_6 = node({12: "Wool", 9 : "Grain", 5 : "Brick"},edges[16], edges[6],edges[18],2,6)
    node_3_5 = node({6 : "Ore", 12 : "Wool", 5 : "Brick"},edges[15],edges[16],edges[17],3,5)
    node_2_4 = node({11 : "Lumber", 12: "Wool", 6 : "Ore"},edges[14], edges[3],edges[15],2,4)
    node_3_3 = node({6 : "Ore", 11 : "Lumber", 4 : "Brick"},edges[12],edges[13],edges[14],3,3)
    node_2_2 = node({4 : "Brick", 11 : "Lumber"},edges[11],edges[0],edges[12],2,2)
    node_3_1 = node({4 : "Brick"},None,edges[10],edges[11],3,1)
    node_4_1 = node({4 : "Brick", 7 : "Desert"},edges[24],edges[10],edges[25],4,1)
    node_5_2 = node({7 : "Desert", 4 : "Brick", 3 : "Lumber"},edges[25],edges[26],edges[27],5,2)
    node_4_3 = node({4 : "Brick", 3 : "Lumber", 6 : "Ore"},edges[27],edges[13],edges[28],4,3)
    node_5_4 = node({3 : "Lumber", 6  : "Ore", 11 : "Grain"},edges[28],edges[29],edges[30],5,4)
    node_4_5 = node({6 : "Ore", 11 : "Grain", 5 : "Brick"},edges[30],edges[16],edges[31],4,5)
    node_5_6 = node({11 : "Grain", 4 : "Lumber", 5 : "Brick"},edges[31],edges[32],edges[33],5,6)
    node_4_7 = node({4 : "Lumber", 10 : "Wool", 5 : "Brick"},edges[33],edges[19],edges[34],4,7)
    node_5_8 = node({4 : "Lumber", 10 : "Wool", 8 : "Grain"},edges[34],edges[35],edges[36],5,8)
    node_4_9 = node({10 : "Wool", 8 : "Grain"},edges[36],edges[22],edges[37],4,9)
    node_5_10 = node({8 : "Grain"},edges[37],edges[38],None,5,10)
    node_6_10 = node({8 : "Grain"},edges[53],edges[38],None,6,10)
    node_7_9 = node({8 : "Grain", 3 : "Ore"}, edges[51],edges[52],edges[53],7,9)
    node_6_8 = node({8 : "Grain", 4 : "Lumber", 3 : "Ore"}, edges[50], edges[35],edges[51],6,8)
    node_7_7 = node({9 : "Wool", 4 : "Lumber", 3 : "Ore"},edges[48], edges[49],edges[50],7,7)
    node_6_6 = node({11 : "Grain", 9 : "Wool", 4 : "Lumber"},edges[47], edges[32], edges[48],6,6)
    node_7_5 = node({11 : "Grain", 9 : "Wool", 10 : "Wool"},edges[45],edges[46],edges[47],7,5)
    node_6_4 = node({11 : "Grain", 10 : "Wool", 3 : "Lumber"},edges[44],edges[29],edges[45],6,4)
    node_7_3 = node({8 : "Brick", 10 : "Wool", 3 : "Lumber"},edges[42],edges[43],edges[44],7,3)
    node_6_2 = node({8 : "Brick", 7 : "Desert", 3 : "Lumber"},edges[41],edges[26],edges[42],6,2)
    node_7_1 = node({8 : "Brick", 7 : "Desert"},edges[39],edges[40],edges[41],7,1)
    node_6_0 = node({7 : "Desert"}, None,edges[23],edges[39],6,0)
    node_5_0 = node({7 : "Desert"}, None,edges[23],edges[24],5,0)
    node_8_1 = node({8 : "Brick"}, None, edges[40],edges[54],8,1)
    node_9_2 = node({8 : "Brick", 5 : "Ore"},edges[54],edges[55],edges[56],9,2)
    node_8_3 = node({8 : "Brick", 5 : "Ore", 10 : "Wool"},edges[56],edges[43],edges[57],8,3)
    node_9_4 = node({2 : "Grain", 5 : "Ore", 10 : "Wool"},edges[57],edges[58],edges[59],9,4)
    node_8_5 = node({2 : "Grain", 9 : "Wool", 10 : "Wool"},edges[59],edges[46],edges[60],8,5)
    node_9_6 = node({2 : "Grain", 6 : "Lumber", 9 : "Wool"},edges[60],edges[61],edges[62],9,6)
    node_8_7 = node({3 : "Ore", 6 : "Lumber", 9 : "Wool"}, edges[62],edges[49],edges[63],8,7)
    node_9_8 = node({3 : "Ore", 6 : "Lumber"},edges[63],edges[65],edges[64],9,8)
    node_8_9 = node({3 : "Ore"},edges[65],edges[52],None,8,9)
    node_10_8 = node({6 : "Lumber"},edges[71],edges[64],None,10,8)
    node_11_7 = node({6 : "Lumber"},edges[70],None,edges[71],11,7)
    node_10_6 = node({2 : "Grain", 6 : "Lumber"}, edges[69],edges[61],edges[70],10,6)
    node_11_5 = node({2 : "Grain"},edges[68],None,edges[69],11,5)
    node_10_4 = node({2 : "Grain", 5 : "Ore"},edges[67],edges[58],edges[68],10,4)
    node_11_3 = node({5 : "Ore"},edges[66],None,edges[67],11,3)
    node_10_2 = node({5 : "Ore"},None,edges[55],edges[66],10,2)

    #adding the nodes each edge connects, generated by a different script.
    edges[0].add_nodes(node_2_2, node_1_2)
    edges[1].add_nodes(node_1_2, node_0_3)
    edges[2].add_nodes(node_0_3, node_1_4)
    edges[3].add_nodes(node_1_4, node_2_4)
    edges[4].add_nodes(node_1_4, node_0_5)
    edges[5].add_nodes(node_0_5, node_1_6)
    edges[6].add_nodes(node_1_6, node_2_6)
    edges[7].add_nodes(node_1_6, node_0_7)
    edges[8].add_nodes(node_0_7, node_1_8)
    edges[9].add_nodes(node_1_8, node_2_8)
    edges[10].add_nodes(node_3_1, node_4_1)
    edges[11].add_nodes(node_3_1, node_2_2)
    edges[12].add_nodes(node_2_2, node_3_3)
    edges[13].add_nodes(node_3_3, node_4_3)
    edges[14].add_nodes(node_3_3, node_2_4)
    edges[15].add_nodes(node_2_4, node_3_5)
    edges[16].add_nodes(node_3_5, node_4_5)
    edges[17].add_nodes(node_3_5, node_2_6)
    edges[18].add_nodes(node_2_6, node_3_7)
    edges[19].add_nodes(node_3_7, node_4_7)
    edges[20].add_nodes(node_3_7, node_2_8)
    edges[21].add_nodes(node_2_8, node_3_9)
    edges[22].add_nodes(node_3_9, node_4_9)
    edges[23].add_nodes(node_5_0, node_6_0)
    edges[24].add_nodes(node_5_0, node_4_1)
    edges[25].add_nodes(node_4_1, node_5_2)
    edges[26].add_nodes(node_5_2, node_6_2)
    edges[27].add_nodes(node_5_2, node_4_3)
    edges[28].add_nodes(node_4_3, node_5_4)
    edges[29].add_nodes(node_5_4, node_6_4)
    edges[30].add_nodes(node_5_4, node_4_5)
    edges[31].add_nodes(node_4_5, node_5_6)
    edges[32].add_nodes(node_5_6, node_6_6)
    edges[33].add_nodes(node_5_6, node_4_7)
    edges[34].add_nodes(node_4_7, node_5_8)
    edges[35].add_nodes(node_5_8, node_6_8)
    edges[36].add_nodes(node_5_8, node_4_9)
    edges[37].add_nodes(node_4_9, node_5_10)
    edges[38].add_nodes(node_5_10, node_6_10)
    edges[39].add_nodes(node_6_0, node_7_1)
    edges[40].add_nodes(node_7_1, node_8_1)
    edges[41].add_nodes(node_7_1, node_6_2)
    edges[42].add_nodes(node_6_2, node_7_3)
    edges[43].add_nodes(node_7_3, node_8_3)
    edges[44].add_nodes(node_7_3, node_6_4)
    edges[45].add_nodes(node_6_4, node_7_5)
    edges[46].add_nodes(node_7_5, node_8_5)
    edges[47].add_nodes(node_7_5, node_6_6)
    edges[48].add_nodes(node_6_6, node_7_7)
    edges[49].add_nodes(node_7_7, node_8_7)
    edges[50].add_nodes(node_7_7, node_6_8)
    edges[51].add_nodes(node_6_8, node_7_9)
    edges[52].add_nodes(node_7_9, node_8_9)
    edges[53].add_nodes(node_7_9, node_6_10)
    edges[54].add_nodes(node_8_1, node_9_2)
    edges[55].add_nodes(node_9_2, node_10_2)
    edges[56].add_nodes(node_9_2, node_8_3)
    edges[57].add_nodes(node_8_3, node_9_4)
    edges[58].add_nodes(node_9_4, node_10_4)
    edges[59].add_nodes(node_9_4, node_8_5)
    edges[60].add_nodes(node_8_5, node_9_6)
    edges[61].add_nodes(node_9_6, node_10_6)
    edges[62].add_nodes(node_9_6, node_8_7)
    edges[63].add_nodes(node_8_7, node_9_8)
    edges[64].add_nodes(node_9_8, node_10_8)
    edges[65].add_nodes(node_9_8, node_8_9)
    edges[66].add_nodes(node_10_2, node_11_3)
    edges[67].add_nodes(node_11_3, node_10_4)
    edges[68].add_nodes(node_10_4, node_11_5)
    edges[69].add_nodes(node_11_5, node_10_6)
    edges[70].add_nodes(node_10_6, node_11_7)
    edges[71].add_nodes(node_11_7, node_10_8)

def dice_roll():
    roll = random.randint(1,6) + random.randint(1,6)
    if roll == 7:
        for player in players:
            if player.total_resources() > 7:
                player.discard_half()
    else:
        for hexagon in basic.layout:
            hexagon.distribute(roll)

def find_node_with_settlement(player):
    #TODO
    return None

#each player rolls dice and acquires resources/places settlements
def game_turn():
    for player in players:
        dice_roll()
        #if possible, build
        
        if player.can_build_city():
            #pick location to build
            settlement = find_node_with_settlement(player)
            player.build_city()
            settlement.type = 2
        if player.can_build_settlement():
            #need to check multiple conditions:
            #   1. adjacent to a road
            #   2. distance of at least 2 away from any settlement
            #   3. current node is empty (this is first thing to be done)
            pass
        if player.can_build_road():
            #check if connected to settlement or other road
            pass

        #check if anyone is winning


def get_random_empty_node()
    rand_nodes = random.sample(nodes, len(nodes))
    for node in rand_nodes:
        if (node.player == None):
            return node

def get_random_empty_edge(node):
    rand_edges = random.sample(node.edges, len(node.edges))
    for edge in rand_edges:
        if edge.player is None:
            return edge

def place_settlement_and_road(player):
    #first two settlements and roads are free, don't subtract from resources
    #create a new list that contains all the nodes randomized (we don't actually randomize the original list here)
    #loop through the list until you find one that's empty

    found_node_edge = False
        while (!found_node_edge):
            node = get_random_empty_node()
            if node is None:
                raise ValueException("No empty nodes found -- this shouldn't happen in the first round so if you're seeing this the code's wrong")
            edge = get_random_empty_edge()
            #note: a node could be empty but all surrounding edges could be taken (this probably will never happen in a real game)
            if edge is not None:
                node.player = player.ID
                edge.player = player.ID
                print("Player " + str(player.ID) + " built a settlement at coordinates" +\
                              node.get_coords() + ", and a road to " +\
                              #make sure we're giving the coordinates to the other node, not the node where the settlement is
                              (edge.node1.get_coords() if edge.node2 is node else edge.node2.get_coords()))
                
def first_turn():
    for player in players:
        place_settlement_and_road(player)    
        
    for player in reversed(players):
        place_settlement_and_road(player)

def __main__():
    #place initial settlements and roads
    first_turn()
    #loop through turns in the game
    for i in range(0, 200):
        game_turn()
    #end when one player has score of 10 (implement limit to number of turns if simulation takes too long)
