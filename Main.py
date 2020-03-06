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

resource_rates = [0, 1, 1, 1, 1, 1]
strat = {Strategies.Build_All : None, Strategies.Road_Settlement_Ratio : 4, Strategies.Adjust_Resource_Rates: [resource_rates, 1]}
strats = [strat] * 4

strat = {None}
strats = [strat] * 4
random_order = False
sims = 10000

"""
# TEST IF PLAYER ORDER ADVANTAGE
strat = {None}
strats = [strat] * 4
random_order = False
sims = 4000000
"""

if sims > 1:
    G.print_level = 0
else:
    G.print_level = 5

total_turns = np.zeros((sims, 1), dtype=np.uint8)
total_wins = np.zeros((sims, 4))
total_points = np.zeros((sims, 4), dtype=np.uint8)
total_roads = np.zeros((sims, 4), dtype=np.uint8)
total_settlements = np.zeros((sims, 4), dtype=np.uint8)
total_cities = np.zeros((sims, 4), dtype=np.uint8)
bar_len = 50

def simulation(_):
    seed = random.randrange(sys.maxsize)
    random.seed(seed)
    #print("Seed: " + str(seed))
    sim = Simulation(strats, "val_const", random_order)
    turns, winners, points, roads, settlements, cities = sim.run()
    return (turns, winners, points, roads, settlements, cities)

if __name__ == "__main__":
    if not path.exists("Data"):
        os.mkdir("Data")

    if os.path.exists("Data/summary.csv") or os.path.exists("Data/turns.csv") \
            or os.path.exists("Data/wins.csv") or os.path.exists("Data/points.csv") \
            or os.path.exists("Data/roads.csv") or os.path.exists("Data/settlements.csv") \
            or os.path.exists("Data/cities.csv") or os.path.exists("Data/output.txt"):
        print("Make sure to rename the saved files before continuing")
        while True:
            text = input("Type y to continue anyways, n to exit: ")
            if text == "y":
                break
            if text == "n":
                sys.exit("Quitting.")

    start = time.perf_counter()
    p = Pool()
    for i, item in enumerate(p.imap_unordered(simulation, range(sims)), 0):
        if (i % 5 == 0):
            equals = round(i / sims * bar_len)
            spaces = bar_len - equals
            print("\r[" + "=" * equals + " " * spaces + "]\t" + str(i) + "/" + str(sims) + "\t" + "{:.2f}".format(i * 100 / sims)+ "% Done\t\t", end="")
        total_turns[i] = item[0]
        for winner in item[1]:
            total_wins[i, winner] = 1
        #total_wins[i, item[1]] = 1
        total_points[i] = item[2]
        total_roads[i] = item[3]
        total_settlements[i] = item[4]
        total_cities[i] = item[5]
    print("\r[" + "=" * bar_len + "]\t" + str(sims) + "/" + str(sims) + "\t" + "100% Done\t\t\t")

    turns = np.mean(total_turns, 0)
    wins = np.sum(total_wins, 0)
    points = np.mean(total_points, 0)
    roads = np.mean(total_roads, 0)
    settlements = np.mean(total_settlements, 0)
    cities = np.mean(total_cities, 0)


    end = time.perf_counter()
    output = ""
    output += "Turns:\n"
    output += "\tMean: " + str(turns) + "\n"
    output += "\tSt. Dev.: " + str(np.std(total_turns, 0)) + "\n"
    output += "Wins\n"
    output += "\tCount: " + str(wins) + "\n"
    output += "\tPercent: " + str(np.sum(total_wins, 0) / sims) + "\n"
    output += "Points:" + "\n"
    output += "\tMean: " + str(points) + "\n"
    output += "\tSt. Dev.: " + str(np.std(total_points, 0)) + "\n"
    output += "Roads:" + "\n"
    output += "\tMean: " + str(roads) + "\n"
    output += "\tSt. Dev.: " + str(np.std(total_roads, 0)) + "\n"
    output += "Settlements:" + "\n"
    output += "\tMean: " + str(settlements) + "\n"
    output += "\tSt. Dev.: " + str(np.std(total_settlements, 0)) + "\n"
    output += "Cities:" + "\n"
    output += "\tMean: " + str(cities) + "\n"
    output += "\tSt. Dev.: " + str(np.std(total_cities, 0)) + "\n"

    output += "Strategies Used: " + str(strats) + "\n"
    output += "Random Player Order: " + str(random_order) + "\n"
    output += "Total Elapsed: " + str(datetime.timedelta(seconds=end - start)) + "\n"

    summary = np.vstack((np.pad(turns, (0, 3), mode='constant'), wins, points, roads, settlements, cities))
    np.savetxt("Data/summary.csv", summary, fmt="%f", delimiter=",")

    print(output)
    with open("Data/output.txt", "w") as f:
        print(output, file=f)

    np.savetxt("Data/turns.csv", total_turns, fmt="%d", delimiter=",")
    np.savetxt("Data/wins.csv", total_turns, fmt="%d", delimiter=",")
    np.savetxt("Data/points.csv", total_points, fmt="%d", delimiter=",")
    np.savetxt("Data/roads.csv", total_roads, fmt="%d", delimiter=",")
    np.savetxt("Data/settlements.csv", total_settlements, fmt="%d", delimiter=",")
    np.savetxt("Data/cities.csv", total_cities, fmt="%d", delimiter=",")


    #total_turns = np.loadtxt("Data/turns.csv", dtype=np.unit8, delimiter=",")
    #total_points = np.loadtxt("Data/points.csv", dtype=np.unit8, delimiter=",")