
import math
class Seed:
    _STAGES = [
        "GERMINATION",
        "CROISSANCE",
    ]
    

    @staticmethod
    def grow(crop, weather):
        if crop.stage == 0:
            if weather.temperature >= 15:
                crop.stage = 1
        if crop.stage == 1:

            grow_volume = (math.pi * ((crop.diameter + 0.001) / 2.0) ** 2.0) * crop.height - (math.pi * (crop.diameter / 2.0) ** 2.0) * crop.height
            grow_volume += (math.pi * ((crop.diameter + 0.001) / 2.0) ** 2.0) * 0.002
            crop.field.water_density -= grow_volume

            
            if crop.height == 0.0:
                crop.height = 0.002
                crop.diameter = 0.001
            else:
                crop.height *= 1.01
                crop.diameter *= 1.01