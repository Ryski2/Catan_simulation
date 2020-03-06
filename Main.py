from Simulation import *
from Player import Strategies
import random
import sys

seed = random.randrange(sys.maxsize)
random.seed(seed)
print("Seed: " + str(seed))

# run simulation once with four players who have no strategyes with the basic board layout (basic_layout.jpg).

# each player can carry a set of strategies
# Multiple stratgies can coexist.
# For example, a building strategy and a trading strategy don't comflict
strats = [{Strategies.Adjust_Resource_Rates, Strategies.Trade}, {Strategies.Trade}, {Strategies.Trade}, {Strategies.Trade}]  
sim = Simulation(strats, "basic")
sim.run()
print("Seed: " + str(seed))
"""
blockPrint()
enablePrint()
"""
