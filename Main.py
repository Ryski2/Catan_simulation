from Simulation import *
import random
import sys

seed = random.randrange(sys.maxsize)
random.seed(seed)

sim = Simulation()
sim.run()
print("Seed: " + str(seed))