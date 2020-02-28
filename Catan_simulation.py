#!/usr/bin/env python
# coding: utf-8

import random

game_board = []
players = []

# For settlements, cities
class node:
    def __init__(self, nearby, leftEdge, centerEdge, rightEdge, rowNum, columnNum):
        #dictionary of resources and attached rolls?
        self.resources = nearby
        #leftward edge?
        self.left = leftEdge
        #rightward edge
        self.right = rightEdge
        #could be going up or down
        self.center = centerEdge
        self.row = rowNum
        self.column = columnNum

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
        self.points = 0

    def build_set():
        self.lumberCount -= 1
        self.brickCount -= 1
        self.woolCount -= 1
        self.grainCount -= 1
        self.setCount += 1
        self.points += 1

    def build_road():
        self.lumberCount -= 1
        self.brickCount -= 1

    def build_city():
        self.oreCount -= 3
        self.grainCount -= 2
        self.points += 1

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
    edgeArray = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, edge13, edge14, edge15, edge16
    node12 = node({11 : "Lumber"}, None, edge0, edge1, 1, 2)
    node03 = node({11 : "Lumber"}, edge1, None, edge2, 0, 3)
    node14 = node({11 : "Lumber", 12: "Wool"}, edge2, edge3, edge4, 1,4)
    node05 = node({12 : "Wool"}, edge4, None, edge5, 0,5)
    node16 = node({12 : "Wool", 9 : "Grain"}, edge5, edge6, edge7, 1,6)
    node07 = node({9 : "Grain"}, edge7, None, edge8, 0,7)
    node18 = node({9 : "Grain"}, edge8, edge9, None, 1, 8)
    node28 = node({9 : "Grain", 10 : "Wool"}, edge10, edge9, edge34,2,8)
    node37 = node({9 : "Grain", 10 : "Wool", 5 : "Brick"},edge12,edge11, edge10,3,7)
    node26 = node({12: "Wool", 9 : "Grain", 5 : "Brick"},edge13, edge6,edge12,2,6)
    node35 = node({6 : "Ore", 12 : "Wool", 5 : "Brick"},edge15,edge14,edge14,3,5)
    node24 = node({11 : "Lumber", 12: "Wool", 6 : "Ore"},edge16, edge3,edge15,2,4)
    node33 = node({6 : "Ore", 11 : "Lumber", 4 : "Brick"},edge18,edge17,edge16,3,3)
    node22 = node({4 : "Brick", 11 : "Lumber"},edge19,edge0,edge18,2,2)
    node31 = node({4 : "Brick"},None,edge20,edge19,3,1)
    node41 = node({4 : "Brick", 7 : "Desert"},edge52,edge20,edge21,4,1)
    node52 = node({7 : "Desert", 4 : "Brick", 3 : "Lumber"},edge21,edge22,edge23,5,2)
    node43 = node({4 : "Brick", 3 : "Lumber", 6 : "Ore"},edge23,edge17,edge24,4,3)
    node54 = node({3 : "Lumber", 6  : "Ore", 11 : "Grain"},edge24,edge25,edge26,5,4)
    node45 = node({6 : "Ore", 11 : "Grain", 5 : "Brick"},edge26,edge14,edge27,4,5)
    node56 = node({11 : "Grain", 4 : "Lumber", 5 : "Brick"},edge27,edge28,edge29,5,6)
    node47 = node({4 : "Lumber", 10 : "Wool", 5 : "Brick"},edge29,edge11,edge30,4,7)
    node58 = node({4 : "Lumber", 10 : "Wool", 8 : "Grain"},edge30,edge31,edge32,5,8)
    node49 = node({10 : "Wool", 8 : "Grain"},edge32,edge33,edge34,4,9)
    node510 = node({8 : "Grain"},edge35,None,edge36,5,10)
    node610 = node({8 : "Grain"},edge37,edge36,None,6,10)
    node79 = node({8 : "Grain", 3 : "Ore"}, edge39,edge38,edge37,7,9)
    node68 = node({8 : "Grain", 4 : "Lumber", 3 : "Ore"}, edge40, edge31,edge39,6,8)
    node77 = node({9 : "Wool", 4 : "Lumber", 3 : "Ore"},edge42, edge41,edge40,7,7)
    node66 = node({11 : "Grain", 9 : "Wool", 4 : "Lumber"},edge43, edge28, edge42,6,6)
    node75 = node({11 : "Grain", 9 : "Wool", 10 : "Wool"},edge45,edge44,edge43,7,5)
    node64 = node({11 : "Grain", 10 : "Wool", 3 : "Lumber"},edge46,edge25,edge45,6,4)
    node73 = node({8 : "Brick", 10 : "Wool", 3 : "Lumber"},edge48,edge47,edge46,7,3)
    node62 = node({8 : "Brick", 7 : "Desert", 3 : "Lumber"},edge49,edge22,edge48,6,2)
    node71 = node({8 : "Brick", 7 : "Desert"},edge50,edge53,edge49,7,1)
    node60 = node({7 : "Desert"}, None,edge51,edge50,6,0)
    node50 = node({7 : "Desert"}, None,edge51,edge52,5,0)
    node81 = node({8 : "Brick"}, None, edge53,edge54,8,1)
    node92 = node({8 : "Brick", 5 : "Ore"},edge54,edge55,edge56,9,2)
    node83 = node({8 : "Brick", 5 : "Ore", 10 : "Wool"},edge56,edge47,edge57,8,3)
    node94 = node({2 : "Grain", 5 : "Ore", 10 : "Wool"},edge57,edge58,edge59,9,4)
    node85 = node({2 : "Grain", 9 : "Wool", 10 : "Wool"},edge59,edge44,edge60,8,5)
    node96 = node({2 : "Grain", 6 : "Lumber", 9 : "Wool"},edge60,edge61,edge62,9,6)
    node87 = node({3 : "Ore", 6 : "Lumber", 9 : "Wool"}, edge62,edge41,edge63,8,7)
    node98 = node({3 : "Ore", 6 : "Lumber"},edge63,edge65,edge64,9,8)
    node89 = node({3 : "Ore"},edge64,edge38,None,8,9)
    node108 = node({6 : "Lumber"},edge66,edge65,None,10,8)
    node117 = node({6 : "Lumber"},edge67,None,edge66,11,7)
    node106 = node({2 : "Grain", 6 : "Lumber"}, edge68,edge61,edge67,10,6)
    node115 = node({2 : "Grain"},edge69,None,edge68,11,5)
    node104 = node({2 : "Grain", 5 : "Ore"},edge70,edge58,edge69,10,4)
    node113 = node({5 : "Ore"},edge71,None,edge70,11,3)
    node102 = node({5 : "Ore"},None,edge55,edge71,10,2)

def dice_roll():
    roll = random.randint(1,6) + random.randint(1,6)
    if roll == 7:
        for player in players:
            if player.total_resources() > 7:
                player.discard_half()

    else:
        for hexagon in basic.layout:
            hexagon.distribute(roll)
        
	
#each player rolls dice and acquires resources/places settlements
def game_round():
    for player in players:
        dice_roll()
        #if possible, build
        #check if anyone is winning
    
def first_turn():
    for player in players:
        #place settlement and road
        pass
    for player in reversed(players):
        #place settlement and road
        pass

def __main__():
    #place initial settlements and roads
    first_turn()
    #loop through turns in the game
    for i in range(0, 200):
        game_turn()
    #end when one player has score of 10 (implement limit to number of turns if simulation takes too long)
