import numpy as np

class Weather:
    def __init__(self):
        self.temperature = 18.0

    def get_weather(self):
        return np.round(np.random.normal(18.0, 5.0), decimals=1)