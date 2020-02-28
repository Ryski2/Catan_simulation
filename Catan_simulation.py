#!/usr/bin/env python
# coding: utf-8

import random

game_board = []
players = []

# For settlements, cities
class node:
    def __init__(self, nearby):
        #dictionary of resources and attached rolls?
        self.resources = nearby
        #leftward edge?
        self.left = None
        #rightward edge
        self.right = None
        #could be going up or down
        self.center = None

#edge class for roads
class edge:
    def __init__(self):
        #if player is assigned, road exists, possibly add additional variables if checking for null is problematic
        self.player = None
        self.node1 = None
        self.node2 = None

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
        
def dice_roll():
    roll = random.randint(1,6) + random.randint(1,6)
    if roll == 7:
        for player in players:
            if player.total_resources() > 7:
                player.discard_half()

    else:
        for hexagon in basic.layout:
            hexagon.distribute(roll)
        
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

