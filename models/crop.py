class Crop:

    def __init__(self, name):
        self._height = 0.0
        self._name = name
    def next(self):
        self._height += 1.0

    def __repr__(self):
        return "<Crop "+self._name+" ("+str(hex(id(self)))+"), height="+str(self._height)+">"