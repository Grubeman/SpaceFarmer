import math

class Crop:
    def __init__(self, seed, field):
        self.set_seed(seed)
        self.field = field
        self.height = 0.0
        self.diameter = 0.0
        self.density = 1.0
        self.stage = 0

    def set_seed(self, seed):
        self.seed = seed

    def grow(self, weather):
        self.seed.grow(self, weather)

    def __repr__(self):
        return "<Crop "+self.seed.name+" ("+str(hex(id(self)))+"), height="+str(self.seed.height)+">"