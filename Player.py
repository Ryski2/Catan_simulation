#for storing player states
class Player:
    def __init__(self, id = None):
        self.ID = id
        self.lumberCount = 0
        self.woolCount = 0
        self.oreCount = 0
        self.grainCount = 0
        self.brickCount = 0
        self.setCount = 0
        self.cityCount = 0
        self.longestRoad = 0
        self.locations = []

    def points(self):
        return self.setCount + self.cityCount * 2 + self.longestRoad

    def can_build_set(self):
        return self.lumberCount >= 1 and self.brickCount >= 1 and self.woolCount >= 1 and self.grainCount >= 1

    def build_set(self):
        self.lumberCount -= 1
        self.brickCount -= 1
        self.woolCount -= 1
        self.grainCount -= 1
        self.setCount += 1

    def can_build_road(self):
        return self.lumberCount >= 1 and self.brickCont >= 1
    
    def build_road(self):
        self.lumberCount -= 1
        self.brickCount -= 1

    def can_build_city(self):
        return self.oreCount >= 3 and self.grainCount >= 2 and self.setCount >= 1
        
    def build_city(self):
        self.oreCount -= 3
        self.grainCount -= 2
        self.setCount -= 1
        self.cityCount += 1

    def total_resources(self):
        return self.lumberCount + self.woolCount + self.oreCount + self.grainCount + self.brickCount

    def discard_half(self):
        discards = player.total_resources() // 2
        for i in range(0, discards):
            resource = random.randint(1,5)
            if resource == 1:
                lumberCount -= 1
            elif resource == 2:
                woolCount -= 1
            elif resource == 3:
                oreCount -= 1
            elif resouce == 4:
                grainCount -= 1
            else:
                brickCount -= 1

