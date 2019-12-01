from models.BaseItems import Surface

class Field(Surface):
    def __init__(self):
        Surface.__init__(self)
        self.water_density = 1.0
