from math import sqrt, sin, floor, atan

class Vec2:
    X : float
    Y : float

    def __init__(self, x, y):
        '''
        A 2-dimensional, cartesian representation of a Vector.
        '''
        self.X = x
        self.Y = y
    
    def __mul__(self, value):
        if isinstance(value, Vec2):
            return Vec2(self.X * value.X, self.Y * value.Y)
        else:
            return Vec2(value * self.X, value * self.Y)
    
    def __add__(self, value):
        if isinstance(value, Vec2):
            return Vec2(self.X + value.X, self.Y + value.Y)
        else:
            return Vec2(value + self.X, value + self.Y)
    
    def __sub__(self, value):
        return Vec2(self.X - value.X, self.Y - value.Y)

    def size(self):
        return sqrt(self.dot(self))

    def size_squared(self):
        return self.dot(self)

    def __str__(self):
        return f'({self.X}, {self.Y})'

    def dot(self, other):
        return self.X * other.X + self.Y * other.Y
    
    def sin(self):
        return Vec2(sin(self.X), sin(self.Y))
    
    def floor(self):
        return Vec2(floor(self.X), floor(self.Y))
    
    def get_angle(self):
        return atan(self.Y / self.X)
    

class Vec3:

    X : float
    Y : float
    Z : float

    def __init__(self, x, y, z) -> None:
        self.X = x
        self.Y = y
        self.Z = z
    
    def size(self):
        return sqrt(self.dot(self))

    def size_squared(self):
        return self.dot(self)
