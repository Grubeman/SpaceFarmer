import numpy as np

class Weather:
    def __init__(self):
        self.temperature = 18.0

    def get_daily(self, day):
        nb_days = 365.0
        angle = day * 2.0 * np.pi / nb_days - np.pi
        print(angle)
        mean = 20.0 * np.cos(angle) + 20.0
        print(mean)
        return np.round(np.random.normal(mean, 5.0), decimals=1)