class Point:
    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord

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