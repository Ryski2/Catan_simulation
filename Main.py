from Simulation import *
from Player import Strategies
from Globals import v_print
import numpy as np
import random
import sys

# run simulation once with four players who have no strategies with the basic board layout (basic_layout.jpg).

# each player can carry a set of strategies
# Multiple stratgies can coexist.
# For example, a building strategy and a trading strategy don't comflict
#strats = [{Strategies.Trade}] + [set()] * 3
strats = [{Strategies.PrioritizeSettlements, Strategies.Trade}] * 4
#ratios = [3.4, 3.45, 3.55, 3.6]


total_turns = 0
total_points = [0, 0, 0, 0]
sims = 200

for i in range(0, sims):
    if (i % 20 == 0):
        print(str(i * 100 // sims) + "% Done")
    seed = random.randrange(sys.maxsize)
    random.seed(seed)
    #print("Seed: " + str(seed))
    sim = Simulation(strats, "basic")
    turns, points = sim.run()
    total_turns += turns
    total_points += points
    #print(str(turns) + " Turns")
    #print(points)

print("Average Turns: " + str(total_turns / sims))
print("Average Points: " + str(total_points / sims))


"""
blockPrint()
enablePrint()
"""
