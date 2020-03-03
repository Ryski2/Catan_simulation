from Connectors import *
from Player import *
import random

class Board:
    def __init__(self):
        self.layout = []
        self.players = []
        self.edges = []
        self.nodes = []
        self.setup()
        
    def dice_roll(self):
        roll = random.randint(1,6) + random.randint(1,6)
        print("\t\tRolled a " + str(roll))
        if roll == 7:
            for player in self.players:
                resources = player.total_resources()
                if resources > 7:
                    player.discard_half()
                    print("\t\t\tPlayer " + str(player.id) + " had " + str(resources) + " resources and now has " + str(player.total_resources()))
                else:
                    print("\t\t\tPlayer " + str(player.id) + " has " + str(resources) + " resouces. No cards are discarded")
        else:
            for tile in self.layout:
                tile.distribute(roll)


    def setup(self):
        
        self.players.append(Player(1))
        self.players.append(Player(2))
        self.players.append(Player(3))
        self.players.append(Player(4))
        

        # Create a list for storing edges. Edge location shown in basic_layout.png
        self.edges = [Edge() for i in range(72)]
        
        
        node_1_2 = Node({11 : Resource.Lumber}, [None, self.edges[0], self.edges[1]], 1, 2)
        node_0_3 = Node({11 : Resource.Lumber}, [self.edges[1], None, self.edges[2]], 0, 3)
        node_1_4 = Node({11 : Resource.Lumber, 12: Resource.Wool}, [self.edges[2], self.edges[3], self.edges[4]], 1,4)
        node_0_5 = Node({12 : Resource.Wool}, [self.edges[4], None, self.edges[5]], 0,5)
        node_1_6 = Node({12 : Resource.Wool, 9 : Resource.Grain}, [self.edges[5], self.edges[6], self.edges[7]], 1,6)
        node_0_7 = Node({9 : Resource.Grain}, [self.edges[7], None, self.edges[8]], 0,7)
        node_1_8 = Node({9 : Resource.Grain}, [self.edges[8], self.edges[9], None], 1, 8)
        node_2_8 = Node({9 : Resource.Grain, 10 : Resource.Wool}, [self.edges[20], self.edges[9], self.edges[21]],2,8)
        node_3_7 = Node({9 : Resource.Grain, 10 : Resource.Wool, 5 : Resource.Brick},[self.edges[18],self.edges[19], self.edges[20]],3,7)
        node_2_6 = Node({12: Resource.Wool, 9 : Resource.Grain, 5 : Resource.Brick},[self.edges[16], self.edges[6],self.edges[18]],2,6)
        node_3_5 = Node({6 : Resource.Ore, 12 : Resource.Wool, 5 : Resource.Brick},[self.edges[15],self.edges[16],self.edges[17]],3,5)
        node_2_4 = Node({11 : Resource.Lumber, 12: Resource.Wool, 6 : Resource.Ore},[self.edges[14], self.edges[3],self.edges[15]],2,4)
        node_3_3 = Node({6 : Resource.Ore, 11 : Resource.Lumber, 4 : Resource.Brick},[self.edges[12],self.edges[13],self.edges[14]],3,3)
        node_2_2 = Node({4 : Resource.Brick, 11 : Resource.Lumber},[self.edges[11],self.edges[0],self.edges[12]],2,2)
        node_3_1 = Node({4 : Resource.Brick},[None,self.edges[10],self.edges[11]],3,1)
        node_4_1 = Node({4 : Resource.Brick, 7 : Resource.Desert},[self.edges[24],self.edges[10],self.edges[25]],4,1)
        node_5_2 = Node({7 : Resource.Desert, 4 : Resource.Brick, 3 : Resource.Lumber},[self.edges[25],self.edges[26],self.edges[27]],5,2)
        node_4_3 = Node({4 : Resource.Brick, 3 : Resource.Lumber, 6 : Resource.Ore},[self.edges[27],self.edges[13],self.edges[28]],4,3)
        node_5_4 = Node({3 : Resource.Lumber, 6  : Resource.Ore, 11 : Resource.Grain},[self.edges[28],self.edges[29],self.edges[30]],5,4)
        node_4_5 = Node({6 : Resource.Ore, 11 : Resource.Grain, 5 : Resource.Brick},[self.edges[30],self.edges[16],self.edges[31]],4,5)
        node_5_6 = Node({11 : Resource.Grain, 4 : Resource.Lumber, 5 : Resource.Brick},[self.edges[31],self.edges[32],self.edges[33]],5,6)
        node_4_7 = Node({4 : Resource.Lumber, 10 : Resource.Wool, 5 : Resource.Brick},[self.edges[33],self.edges[19],self.edges[34]],4,7)
        node_5_8 = Node({4 : Resource.Lumber, 10 : Resource.Wool, 8 : Resource.Grain},[self.edges[34],self.edges[35],self.edges[36]],5,8)
        node_4_9 = Node({10 : Resource.Wool, 8 : Resource.Grain},[self.edges[36],self.edges[22],self.edges[37]],4,9)
        node_5_10 = Node({8 : Resource.Grain},[self.edges[37],self.edges[38],None],5,10)
        node_6_10 = Node({8 : Resource.Grain},[self.edges[53],self.edges[38],None],6,10)
        node_7_9 = Node({8 : Resource.Grain, 3 : Resource.Ore}, [self.edges[51],self.edges[52],self.edges[53]],7,9)
        node_6_8 = Node({8 : Resource.Grain, 4 : Resource.Lumber, 3 : Resource.Ore}, [self.edges[50], self.edges[35],self.edges[51]],6,8)
        node_7_7 = Node({9 : Resource.Wool, 4 : Resource.Lumber, 3 : Resource.Ore},[self.edges[48], self.edges[49],self.edges[50]],7,7)
        node_6_6 = Node({11 : Resource.Grain, 9 : Resource.Wool, 4 : Resource.Lumber},[self.edges[47], self.edges[32], self.edges[48]],6,6)
        node_7_5 = Node({11 : Resource.Grain, 9 : Resource.Wool, 10 : Resource.Wool},[self.edges[45],self.edges[46],self.edges[47]],7,5)
        node_6_4 = Node({11 : Resource.Grain, 10 : Resource.Wool, 3 : Resource.Lumber},[self.edges[44],self.edges[29],self.edges[45]],6,4)
        node_7_3 = Node({8 : Resource.Brick, 10 : Resource.Wool, 3 : Resource.Lumber},[self.edges[42],self.edges[43],self.edges[44]],7,3)
        node_6_2 = Node({8 : Resource.Brick, 7 : Resource.Desert, 3 : Resource.Lumber},[self.edges[41],self.edges[26],self.edges[42]],6,2)
        node_7_1 = Node({8 : Resource.Brick, 7 : Resource.Desert},[self.edges[39],self.edges[40],self.edges[41]],7,1)
        node_6_0 = Node({7 : Resource.Desert}, [None,self.edges[23],self.edges[39]],6,0)
        node_5_0 = Node({7 : Resource.Desert}, [None,self.edges[23],self.edges[24]],5,0)
        node_8_1 = Node({8 : Resource.Brick}, [None, self.edges[40],self.edges[54]],8,1)
        node_9_2 = Node({8 : Resource.Brick, 5 : Resource.Ore},[self.edges[54],self.edges[55],self.edges[56]],9,2)
        node_8_3 = Node({8 : Resource.Brick, 5 : Resource.Ore, 10 : Resource.Wool},[self.edges[56],self.edges[43],self.edges[57]],8,3)
        node_9_4 = Node({2 : Resource.Grain, 5 : Resource.Ore, 10 : Resource.Wool},[self.edges[57],self.edges[58],self.edges[59]],9,4)
        node_8_5 = Node({2 : Resource.Grain, 9 : Resource.Wool, 10 : Resource.Wool},[self.edges[59],self.edges[46],self.edges[60]],8,5)
        node_9_6 = Node({2 : Resource.Grain, 6 : Resource.Lumber, 9 : Resource.Wool},[self.edges[60],self.edges[61],self.edges[62]],9,6)
        node_8_7 = Node({3 : Resource.Ore, 6 : Resource.Lumber, 9 : Resource.Wool}, [self.edges[62],self.edges[49],self.edges[63]],8,7)
        node_9_8 = Node({3 : Resource.Ore, 6 : Resource.Lumber},[self.edges[63],self.edges[65],self.edges[64]],9,8)
        node_8_9 = Node({3 : Resource.Ore},[self.edges[65],self.edges[52],None],8,9)
        node_10_8 = Node({6 : Resource.Lumber},[self.edges[71],self.edges[64],None],10,8)
        node_11_7 = Node({6 : Resource.Lumber},[self.edges[70],None,self.edges[71]],11,7)
        node_10_6 = Node({2 : Resource.Grain, 6 : Resource.Lumber}, [self.edges[69],self.edges[61],self.edges[70]],10,6)
        node_11_5 = Node({2 : Resource.Grain},[self.edges[68],None,self.edges[69]],11,5)
        node_10_4 = Node({2 : Resource.Grain, 5 : Resource.Ore},[self.edges[67],self.edges[58],self.edges[68]],10,4)
        node_11_3 = Node({5 : Resource.Ore},[self.edges[66],None,self.edges[67]],11,3)
        node_10_2 = Node({5 : Resource.Ore},[None,self.edges[55],self.edges[66]],10,2)
        node_3_9 = Node({10 : Resource.Wool}, [self.edges[21], self.edges[22], None], 3, 9)
        
        self.layout.append(Tile(Resource.Lumber, 11, [node_1_2, node_0_3, node_1_4, node_2_4, node_3_3, node_2_2]))
        self.layout.append(Tile(Resource.Wool, 12, [node_1_4,node_0_5,node_1_6,node_2_6,node_3_5,node_2_4]))
        self.layout.append(Tile(Resource.Grain, 9, [node_1_6,node_0_7,node_1_8,node_2_8,node_3_7,node_2_6]))
        self.layout.append(Tile(Resource.Brick, 4, [node_3_1,node_2_2,node_3_3,node_4_3,node_5_2,node_4_1]))
        self.layout.append(Tile(Resource.Ore, 6, [node_3_3,node_2_4,node_3_5,node_4_5,node_5_4,node_4_3]))
        self.layout.append(Tile(Resource.Brick, 5, [node_3_5,node_2_6,node_3_7,node_4_7,node_5_6,node_4_5]))
        self.layout.append(Tile(Resource.Wool, 10, [node_3_7,node_2_8,node_3_9,node_4_9,node_5_8,node_4_7]))
        self.layout.append(Tile(Resource.Desert, 7, [node_5_0,node_4_1,node_5_2,node_6_2,node_7_1,node_6_0]))
        self.layout.append(Tile(Resource.Lumber, 3, [node_5_2,node_4_3,node_5_4,node_6_4,node_7_3,node_6_2]))
        self.layout.append(Tile(Resource.Grain, 11, [node_5_4,node_4_5,node_5_6,node_6_6,node_7_5,node_6_4]))
        self.layout.append(Tile(Resource.Lumber, 4, [node_5_6,node_4_7,node_5_8,node_6_8,node_7_7,node_6_6]))
        self.layout.append(Tile(Resource.Grain, 8, [node_5_8,node_4_9,node_5_10,node_6_10,node_7_9,node_6_8]))
        self.layout.append(Tile(Resource.Brick, 8, [node_7_1,node_6_2,node_7_3,node_8_3,node_9_2,node_8_1]))
        self.layout.append(Tile(Resource.Wool, 10, [node_7_3,node_6_4,node_7_5,node_8_5,node_9_4,node_8_3]))
        self.layout.append(Tile(Resource.Wool, 9, [node_7_5,node_6_6,node_7_7,node_8_7,node_9_6,node_8_5]))
        self.layout.append(Tile(Resource.Ore, 3, [node_7_7,node_6_8,node_7_9,node_8_9,node_9_8,node_8_7]))
        self.layout.append(Tile(Resource.Ore, 5, [node_9_2,node_8_3,node_9_4,node_10_4,node_11_3,node_10_2]))
        self.layout.append(Tile(Resource.Grain, 2, [node_9_4,node_8_5,node_9_6,node_10_6,node_11_5,node_10_4]))
        self.layout.append(Tile(Resource.Lumber, 6, [node_9_6,node_8_7,node_9_8,node_10_8,node_11_7,node_10_6]))
        
        self.nodes = [node_1_2, node_0_3, node_1_4, node_0_5, node_1_6, node_0_7, node_1_8, node_2_8,\
            node_3_7, node_2_6, node_3_5, node_2_4, node_3_3, node_2_2, node_3_1, node_4_1, node_5_2,\
            node_4_3, node_5_4, node_4_5, node_5_6, node_4_7, node_5_8, node_4_9, node_5_10, node_6_10,\
            node_7_9, node_6_8, node_7_7, node_6_6, node_7_5, node_6_4, node_7_3, node_6_2, node_7_1, \
            node_6_0, node_5_0, node_8_1, node_9_2, node_8_3, node_9_4, node_8_5, node_9_6, node_8_7,\
            node_9_8, node_8_9, node_10_8, node_11_7, node_10_6, node_11_5, node_10_4, node_11_3, node_10_2, node_3_9]

        #adding the nodes each edge connects, generated by a different script.
        self.edges[0].add_nodes(node_2_2, node_1_2)
        self.edges[1].add_nodes(node_1_2, node_0_3)
        self.edges[2].add_nodes(node_0_3, node_1_4)
        self.edges[3].add_nodes(node_1_4, node_2_4)
        self.edges[4].add_nodes(node_1_4, node_0_5)
        self.edges[5].add_nodes(node_0_5, node_1_6)
        self.edges[6].add_nodes(node_1_6, node_2_6)
        self.edges[7].add_nodes(node_1_6, node_0_7)
        self.edges[8].add_nodes(node_0_7, node_1_8)
        self.edges[9].add_nodes(node_1_8, node_2_8)
        self.edges[10].add_nodes(node_3_1, node_4_1)
        self.edges[11].add_nodes(node_3_1, node_2_2)
        self.edges[12].add_nodes(node_2_2, node_3_3)
        self.edges[13].add_nodes(node_3_3, node_4_3)
        self.edges[14].add_nodes(node_3_3, node_2_4)
        self.edges[15].add_nodes(node_2_4, node_3_5)
        self.edges[16].add_nodes(node_3_5, node_4_5)
        self.edges[17].add_nodes(node_3_5, node_2_6)
        self.edges[18].add_nodes(node_2_6, node_3_7)
        self.edges[19].add_nodes(node_3_7, node_4_7)
        self.edges[20].add_nodes(node_3_7, node_2_8)
        self.edges[21].add_nodes(node_2_8, node_3_9)
        self.edges[22].add_nodes(node_3_9, node_4_9)
        self.edges[23].add_nodes(node_5_0, node_6_0)
        self.edges[24].add_nodes(node_5_0, node_4_1)
        self.edges[25].add_nodes(node_4_1, node_5_2)
        self.edges[26].add_nodes(node_5_2, node_6_2)
        self.edges[27].add_nodes(node_5_2, node_4_3)
        self.edges[28].add_nodes(node_4_3, node_5_4)
        self.edges[29].add_nodes(node_5_4, node_6_4)
        self.edges[30].add_nodes(node_5_4, node_4_5)
        self.edges[31].add_nodes(node_4_5, node_5_6)
        self.edges[32].add_nodes(node_5_6, node_6_6)
        self.edges[33].add_nodes(node_5_6, node_4_7)
        self.edges[34].add_nodes(node_4_7, node_5_8)
        self.edges[35].add_nodes(node_5_8, node_6_8)
        self.edges[36].add_nodes(node_5_8, node_4_9)
        self.edges[37].add_nodes(node_4_9, node_5_10)
        self.edges[38].add_nodes(node_5_10, node_6_10)
        self.edges[39].add_nodes(node_6_0, node_7_1)
        self.edges[40].add_nodes(node_7_1, node_8_1)
        self.edges[41].add_nodes(node_7_1, node_6_2)
        self.edges[42].add_nodes(node_6_2, node_7_3)
        self.edges[43].add_nodes(node_7_3, node_8_3)
        self.edges[44].add_nodes(node_7_3, node_6_4)
        self.edges[45].add_nodes(node_6_4, node_7_5)
        self.edges[46].add_nodes(node_7_5, node_8_5)
        self.edges[47].add_nodes(node_7_5, node_6_6)
        self.edges[48].add_nodes(node_6_6, node_7_7)
        self.edges[49].add_nodes(node_7_7, node_8_7)
        self.edges[50].add_nodes(node_7_7, node_6_8)
        self.edges[51].add_nodes(node_6_8, node_7_9)
        self.edges[52].add_nodes(node_7_9, node_8_9)
        self.edges[53].add_nodes(node_7_9, node_6_10)
        self.edges[54].add_nodes(node_8_1, node_9_2)
        self.edges[55].add_nodes(node_9_2, node_10_2)
        self.edges[56].add_nodes(node_9_2, node_8_3)
        self.edges[57].add_nodes(node_8_3, node_9_4)
        self.edges[58].add_nodes(node_9_4, node_10_4)
        self.edges[59].add_nodes(node_9_4, node_8_5)
        self.edges[60].add_nodes(node_8_5, node_9_6)
        self.edges[61].add_nodes(node_9_6, node_10_6)
        self.edges[62].add_nodes(node_9_6, node_8_7)
        self.edges[63].add_nodes(node_8_7, node_9_8)
        self.edges[64].add_nodes(node_9_8, node_10_8)
        self.edges[65].add_nodes(node_9_8, node_8_9)
        self.edges[66].add_nodes(node_10_2, node_11_3)
        self.edges[67].add_nodes(node_11_3, node_10_4)
        self.edges[68].add_nodes(node_10_4, node_11_5)
        self.edges[69].add_nodes(node_11_5, node_10_6)
        self.edges[70].add_nodes(node_10_6, node_11_7)
        self.edges[71].add_nodes(node_11_7, node_10_8)
    
class EdgeType(Enum):
    Left = 1
    Center = 2
    Right = 3
    
class Tile:
    def __init__(self, resource, value, adj_nodes):
        self.resource = resource
        self.value = value
        self.nodes = adj_nodes
        
    def distribute(self, roll_value):
        if self.value == roll_value:
            for node in self.nodes:
                if node.type == BuildType.Settlement:
                    print("\t\t\tPlayer " + str(node.player.id) + " got 1 of resource " + str(self.resource))
                    node.player.resources[self.resource] += 1
                elif node.type == BuildType.City:
                    print("\t\t\tPlayer " + str(node.player.id) + " got 2 of resource " + str(self.resource))
                    node.player.resources[self.resource] += 2
