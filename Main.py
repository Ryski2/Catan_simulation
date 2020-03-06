from Simulation import *
from Player import Strategies
from Globals import v_print
import random
import sys

seed = random.randrange(sys.maxsize)
random.seed(seed)
print("Seed: " + str(seed))

# run simulation once with four players who have no strategyes with the basic board layout (basic_layout.jpg).

# each player can carry a set of strategies
# Multiple stratgies can coexist.
# For example, a building strategy and a trading strategy don't comflict
resource_rates = [0, 1, 1, 1, 1, 1]
strat = {Strategies.Build_All : None, Strategies.Road_Settlement_Ratio : 4, Strategies.Adjust_Resource_Rates: [resource_rates, 1]}
strats = [strat] * 4
sim = Simulation(strats, "basic")
sim.run()
print("Seed: " + str(seed))
"""
blockPrint()
enablePrint()
"""
