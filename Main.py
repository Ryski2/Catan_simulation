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
from multiprocessing import Pool

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
strat = {None}
strats = [strat] * 4

random_order = True
sims = 1000

if sims > 1:
    G.print_level = 0
else:
    G.print_level = 5

total_turns = np.zeros((sims, 1), dtype=np.uint8)
total_points = np.zeros((sims, 4), dtype=np.uint8)
bar_len = 50

def simulation(_):
    seed = random.randrange(sys.maxsize)
    random.seed(seed)
    #print("Seed: " + str(seed))
    sim = Simulation(strats, "basic", random_order)
    turns, points = sim.run()
    return (turns, points)

if __name__ == "__main__":
    start = time.perf_counter()
    p = Pool(8)
    for i, item in enumerate(p.imap_unordered(simulation, range(sims)), 0):
        if (i % 5 == 0):
            equals = round(i / sims * bar_len)
            spaces = bar_len - equals
            print("\r[" + "=" * equals + " " * spaces + "]\t" + str(i) + "/" + str(sims) + "\t" + "{:.2f}".format(i * 100 / sims)+ "% Done\t\t", end="")
        total_turns[i] = item[0]
        total_points[i] = item[1]
    print("\r[" + "=" * bar_len + "]\t" + str(sims) + "/" + str(sims) + "\t" + "100% Done\t\t\t")

    end = time.perf_counter()

    print("Turns:")
    print("\tMean: " + str(np.mean(total_turns, 0)))
    print("\tSt. Dev.: " + str(np.std(total_turns, 0)))
    print("Points:")
    print("\tMean: " + str(np.mean(total_points, 0)))
    print("\tSt. Dev.: " + str(np.std(total_points, 0)))
    print("Strategies Used: " + str(strats))
    print("Random Player Order: " + str(random_order))

    print("Total Elapsed: " + str(datetime.timedelta(seconds=end - start)))

    np.savetxt("Data/turns.csv", total_turns, fmt="%d", delimiter=",")
    np.savetxt("Data/points.csv", total_points, fmt="%d", delimiter=",")

    #total_turns = np.loadtxt("Data/turns.csv", dtype=np.unit8, delimiter=",")
    #total_points = np.loadtxt("Data/points.csv", dtype=np.unit8, delimiter=",")