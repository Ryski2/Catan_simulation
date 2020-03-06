from Simulation import Simulation
from Player import Strategies
import Globals as G
import numpy as np
import random
import sys

# run simulation once with four players who have no strategies with the basic board layout (basic_layout.jpg).

# each player can carry a set of strategies
# Multiple stratgies can coexist.
# For example, a building strategy and a trading strategy don't comflict

strats = [{Strategies.Build_High_Probability_Tiles, Strategies.Prioritize_Settlements}] * 2 + [{Strategies.Prioritize_Settlements}] * 2
ratios = [1, 2, 3, 4]

sims = 100000

if sims > 1:
    G.print_level = 0
else:
    G.print_level = 5

total_turns = np.zeros((sims, 1))
total_points = np.zeros((sims, 4))
bar_len = 50

for i in range(0, sims):
    #progress bar
    if (i % 5 == 0):
        equals = round(i / sims * bar_len)
        spaces = bar_len - equals
        print("\r[" + "=" * equals + " " * spaces + "]\t" + str(i) + "/" + str(sims) + "\t" + "{:.2f}".format(i * 100 / sims)+ "% Done\t\t", end="")
    
    seed = random.randrange(sys.maxsize)
    random.seed(seed)
    #print("Seed: " + str(seed))
    sim = Simulation(strats, "basic", ratios)
    turns, points = sim.run()
    total_turns[i] = turns
    total_points[i] = points
    #print(str(turns) + " Turns")
    #print(points)
print("\r[" + "=" * bar_len + "]\t" + str(sims) + "/" + str(sims) + "\t" + "100% Done\t\t\t")

print("Turns:")
print("\tMean: " + str(np.mean(total_turns, 0)))
print("\tSt. Dev.: " + str(np.std(total_turns, 0)))
print("Points:")
print("\tMean: " + str(np.mean(total_points, 0)))
print("\tSt. Dev.: " + str(np.std(total_points, 0)))
print("Strategies Used: " + str(strats))


"""
blockPrint()
enablePrint()
"""
