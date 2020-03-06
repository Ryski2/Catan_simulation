from Simulation import Simulation
from Player import Strategies
import Globals as G
import numpy as np
import random
import sys
import time
import datetime
import os
from os import path

if not path.exists("Data"):
    os.mkdir("Data")

if os.path.exists("Data/turns.dat") or os.path.exists("Data/points.dat"):
    print("Make sure to rename the saved files before continuing")
    while True:
        text = input("Type y to continue anyways, n to exit: ")
        if text == "y":
           break
        if text == "n":
            sys.exit("Quitting.")

# run simulation once with four players who have no strategies with the basic board layout (basic_layout.jpg).

# each player can carry a set of strategies
# Multiple stratgies can coexist.
# For example, a building strategy and a trading strategy don't comflict

resource_rates = [0, 1, 1, 1, 1, 1]
strat = {Strategies.Build_All : None, Strategies.Road_Settlement_Ratio : 4, Strategies.Adjust_Resource_Rates: [resource_rates, 1]}
strats = [strat] * 4

random_order = True
sims = 1000

if sims > 1:
    G.print_level = 0
else:
    G.print_level = 5

total_turns = np.zeros((sims, 1))
total_points = np.zeros((sims, 4))
bar_len = 50

start = time.process_time()
for i in range(0, sims):
    #progress bar
    if (i % 5 == 0):
        equals = round(i / sims * bar_len)
        spaces = bar_len - equals
        print("\r[" + "=" * equals + " " * spaces + "]\t" + str(i) + "/" + str(sims) + "\t" + "{:.2f}".format(i * 100 / sims)+ "% Done\t\t", end="")
    
    seed = random.randrange(sys.maxsize)
    random.seed(seed)
    #print("Seed: " + str(seed))
    sim = Simulation(strats, "basic", random_order)
    turns, points = sim.run()
    total_turns[i] = turns
    total_points[i] = points
    #print(str(turns) + " Turns")
    #print(points)
end = time.process_time()
print("\r[" + "=" * bar_len + "]\t" + str(sims) + "/" + str(sims) + "\t" + "100% Done\t\t\t")

print("Turns:")
print("\tMean: " + str(np.mean(total_turns, 0)))
print("\tSt. Dev.: " + str(np.std(total_turns, 0)))
print("Points:")
print("\tMean: " + str(np.mean(total_points, 0)))
print("\tSt. Dev.: " + str(np.std(total_points, 0)))
print("Strategies Used: " + str(strats))
print("Random Player Order: " + str(random_order))

print("Total Elapsed: " + str(datetime.timedelta(seconds=end - start)))

total_turns.tofile("Data/turns.dat")
total_points.tofile("Data/points.dat")

"""
blockPrint()
enablePrint()
"""
