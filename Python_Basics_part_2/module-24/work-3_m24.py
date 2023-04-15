import math


class Circle:
    def __init__(self, x=0, y=0, radius=1):
        self.X = x
        self.Y = y
        self.R = radius

    def square(self):
        return self.R ** 2 * math.pi

    def length(self):
        return self.R * 2 * math.pi

    def scale(self, k):
        return self.square() * k

    def is_intersect(self, other):
        return (self.X - other.X) ** 2 + (self.Y - other.Y) ** 2 <= (self.R + other.R) ** 2




