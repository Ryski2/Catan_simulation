from Board import Board
from Connectors import BuildType
from Player import Resource
import random


max_turns = 200

class Simulation:
    def __init__(self):
        self.board = Board()
        
    def run(self):
        print()
        print("Players placing initial settlements and roads")
        print("---------------------------------------------")
        print()
        
        self.first_turn()
        
        
        
        
        print()
        print("Moving on to main game section")
        print("---------------------------------------------")
        print()
        
        
        winner = False
        for i in range(0, max_turns):
            print("Turn " + str(i + 1))
            winner = self.game_turn()
            if winner is not None:
                break
                
        print()
        print("---------------------------------------------")
        print("Game Ended")
        
        
        for player in self.board.players:
            #print every players settlements, roads, and cities
            print("Player " + str(player.id) + ": ")
            print("\tSettlement Locations:")
            for node in self.board.nodes:
                if node.player == player and node.type == BuildType.Settlement:
                    print("\t\t" + node.get_coords())
            print("\tCity Locations:")
            for node in self.board.nodes:
                if node.player == player and node.type == BuildType.City:
                    print("\t\t" + node.get_coords())
            
            print("\tEdge Between:")
            for edge in self.board.edges:
                if edge.player == player:
                    print("\t\t" + edge.node1.get_coords() + " to " + edge.node2.get_coords())
        
        if winner is not None:
            print("Player " + str(winner.id) + " Won")
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
            
    def get_random_empty_node(self):
        #taking random sample now stupid cause we don't loop through? maybe? idk
        for node in random.sample(self.board.nodes, len(self.board.nodes)):
            if (node.player == None):
                return node

    def get_random_empty_edge(self, node):
        for edge in random.sample(node.edges, len(node.edges)):
            if edge is not None and edge.player is None:
                return edge
                
    def initial_settlement_road_placement(self, player, collect_resources):
        #first two settlements and roads are free, don't subtract from resources
        #create a new list that contains all the nodes randomized (we don't actually randomize the original list here)
        #loop through the list until you find one that's empty

        found_node_edge = False
        while not found_node_edge:
            node = self.get_random_empty_node()
            if node is None:
                raise ValueException("No empty nodes found -- this shouldn't happen in the first round so if you're seeing this the code's wrong")
            edge = self.get_random_empty_edge(node)
            
            #note: a node could be empty but all surrounding edges could be taken; if this happesn, we need to pick a new node
            if edge is not None:
                found_node_edge = True
                node.type = BuildType.Settlement
                node.player = player
                edge.player = player                        
                        
                print("Player " + str(player.id) + " built a settlement at coordinates" +\
                              node.get_coords() + ", and a road to " +\
                              #make sure we're giving the coordinates to the other node, not the node where the settlement is
                              (edge.node1.get_coords() if edge.node2 is node else edge.node2.get_coords()))
                              
                #on second round of placement, give each player one resource of each of the bordering tiles
                if (collect_resources):
                    print("\tPlayer " + str(player.id) + " collected the following: " + ", ".join(str(resource) for resource in node.resources.values()))
                    for resource in node.resources.values():
                        if resource == Resource.Desert:
                            continue
                        node.player.resources[resource] += 1
                        
    def find_node_with_settlement(self, player):
        for node in random.sample(self.board.nodes, len(self.board.nodes)):
            if node.player == player and node.type == BuildType.Settlement:
                return node
                              
    def first_turn(self):
        for player in self.board.players:
            self.initial_settlement_road_placement(player, False)    
            
        #on second placement, players get the resources bordering their settlement
        for player in reversed(self.board.players):
            self.initial_settlement_road_placement(player, True)
    
    def find_valid_settlement_location(self, player):
        for node in random.sample(self.board.nodes, len(self.board.nodes)):
            #if no one has already built on the node
            if node.player is None:
                adj_to_own_road = False
                dist_criteria = True
                for edge in node.edges:
                    #and the player owns an adjacent road
                    if edge is not None and edge.player == player:
                        adj_to_own_road = True
                    #and there is no settlement directly adjacent to it
                    if edge is not None and edge.get_other_node(node).player is not None:
                        dist_criteria = False
                if dist_criteria and adj_to_own_road:
                    #build the settlement
                    return node

    def find_valid_road_location(self, player):
        for edge in random.sample(self.board.edges, len(self.board.edges)):
            if edge.player is None:
                #if we own node1 or node2, we good.
                #otherwise, we must own an edge off of either node1 or node2
                if edge.node1.player == player or edge.node2.player == player:
                    return edge
                else:
                    for node_edge in edge.node1.edges:
                        if node_edge is not None and node_edge.player == player:
                            return edge
                    for node_edge in edge.node2.edges:
                        if node_edge is not None and node_edge.player == player:
                            return edge
            
    #each player rolls dice and acquires resources/places settlements
    #this is the bulk of the game, and includes building and rolling the dice
    def game_turn(self):
        for player in self.board.players:
            print("\tPlayer " + str(player.id) + "'s Turn")
            self.board.dice_roll()
            
            #if possible, build            
            if player.can_build_city():
                #pick location to build
                city_node = self.find_node_with_settlement(player)
                if city_node is None:
                    print("\t\tPlayer " + str(player.id) + " had resources to bulid a city but no valid location was found")
                else:
                    player.build_city()
                    city_node.type = BuildType.City
                    print("\t\tPlayer " + str(player.id) + " built a city at " + city_node.get_coords())
                    
            if player.can_build_settlement():
                settlement_node = self.find_valid_settlement_location(player)
                if settlement_node is None:
                    print("\t\tPlayer " + str(player.id) + " had resources to bulid a settlement but no valid location was found")
                else:
                    settlement_node.player = player
                    settlement_node.type = BuildType.Settlement
                    player.build_settlement()
                    print("\t\tPlayer " + str(player.id) + " built a settlement at " + settlement_node.get_coords())               
                    
            if player.can_build_road():
                road_edge = self.find_valid_road_location(player)
                if road_edge is None:
                    print("\t\tPlayer " + str(player.id) + " had resources to bulid a road but no valid location was found")
                else:
                    player.build_road()
                    road_edge.player = player
                    print("\t\tPlayer " + str(player.id) + " built a road from " + road_edge.node1.get_coords() + " to " + road_edge.node2.get_coords())

            #check if anyone is winning
            if player.points() >= 10:
                return player
        