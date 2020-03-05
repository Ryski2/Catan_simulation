from Simulation import *
import random
import sys

seed = random.randrange(sys.maxsize)
random.seed(seed)

# run simulation once with four players who have no strategyes with the basic board layout (basic_layout.jpg).
sim = Simulation( [None] * 4, "basic")
sim.run()
print("Seed: " + str(seed))
