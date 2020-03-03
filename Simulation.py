from Board import Board
import random

class Simulation:
    def __init__(self):
        self.board = Board()
            
    def get_random_empty_node(self):
        #taking random sample now stupid cause we don't loop through? maybe? idk
        rand_nodes = random.sample(self.board.nodes, len(self.board.nodes))
        for node in rand_nodes:
            if (node.player == None):
                return node

    def get_random_empty_edge(self, node):
        rand_edges = random.sample(node.edges, len(node.edges))
        for edge in rand_edges:
            if edge.player is None:
                return edge
                
    def initial_settlement_road_placement(self, player):
        #first two settlements and roads are free, don't subtract from resources
        #create a new list that contains all the nodes randomized (we don't actually randomize the original list here)
        #loop through the list until you find one that's empty

        found_node_edge = False
        while not found_node_edge:
            node = self.get_random_empty_node()
            if node is None:
                raise ValueException("No empty nodes found -- this shouldn't happen in the first round so if you're seeing this the code's wrong")
            edge = self.get_random_empty_edge(node)
            #note: a node could be empty but all surrounding edges could be taken (this probably will never happen in a real game)
            if edge is not None:
                found_node_edge = True
                node.player = player.ID
                edge.player = player.ID
                print("Player " + str(player.ID) + " built a settlement at coordinates" +\
                              node.get_coords() + ", and a road to " +\
                              #make sure we're giving the coordinates to the other node, not the node where the settlement is
                              (edge.node1.get_coords() if edge.node2 is node else edge.node2.get_coords()))
                              
    def first_turn(self):
        for player in self.board.players:
            self.initial_settlement_road_placement(player)    
            
        for player in reversed(self.board.players):
            self.initial_settlement_road_placement(player)
            
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


    def find_node_with_settlement(self, player):
        #TODO
        return None