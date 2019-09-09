import math

class Crop:
    _STAGES = [
        "GERMINATION",
        "CROISSANCE",
    ]
    
    def __init__(self, name, field):
        self.height = 0.0
        self.diameter = 0.0
        self.density = 1.0
        self.name = name
        self.field = field
        self.stage = 0
        
    def grow(self, weather):
        if self.stage == 0:
            if weather.temperature >= 15:
                self.stage = 1
        if self.stage == 1:

            grow_volume = (math.pi * ((self.diameter + 0.001) / 2.0) ** 2.0) * self.height - (math.pi * (self.diameter / 2.0) ** 2.0) * self.height
            grow_volume += (math.pi * ((self.diameter + 0.001) / 2.0) ** 2.0) * 0.002
            self.field.water_density -= grow_volume

            self.diameter += 0.001
            self.height += 0.002

    def __repr__(self):
        return "<Crop "+self.name+" ("+str(hex(id(self)))+"), height="+str(self.height)+">"