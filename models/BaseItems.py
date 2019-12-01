class Point:
    def __init__(self, x_coord, y_coord, z_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._z_coord = z_coord

    def to_json(self):
        return {"x":self._x_coord, "y":self._y_coord, "z":self._z_coord}

class Segment:
    def __init__(self, start, end):
        self._start = start
        self._end = end   

class Line:
    def __init__(self):
        self._segments = []  

class Surface:
    def __init__(self):
        self._vertices = []  

    def to_json(self):
        points = [p.to_json() for p in self._vertices]
        return {"points":points}