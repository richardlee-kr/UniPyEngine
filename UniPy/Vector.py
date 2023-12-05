import math

class Vector:
    def __init__(self, x, y):
        if -1.0e-10 < x < 1.0e-10: x = 0
        if -10.e-10 < y < 1.0e-10: y = 0

        self.x = x
        self.y = y
        self.magnitude = math.sqrt(x*x + y*y)
    
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)
    def __mul__(self, m):
        return Vector(self.x*m, self.y*m)
    def __truediv__(self, d):
        return Vector(self.x/d, self.y/d)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __eq__(self, other):
        return ((self.x==other.x) and (self.y==other.y))

    def __str__(self):
        return "{0}, {1}".format(self.x, self.y)

    def Set(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = math.sqrt(x*x + y*y)
    
    def Normalize(self):
        return Vector(self.x/self.magnitude, self.y/self.magnitude)

    def Rotate(self, angle):
        x = (self.x*math.cos(math.radians(angle)) - self.y*math.sin(math.radians(angle)))
        y = (self.x*math.sin(math.radians(angle)) + self.y*math.cos(math.radians(angle)))
        return Vector(x,y)

    @staticmethod
    def Angle(v1, v2):
        #return math.degrees(math.acos(Vector.Dot(v1, v2) / (v1.magnitude * v2.magnitude)))
        return math.acos(Vector.Dot(v1, v2) / (v1.magnitude * v2.magnitude))
    @staticmethod
    def Angle(v):
        #return math.degrees(math.acos(Vector.Dot(v1, Vector.right) / (v1.magnitude * Vector.right.magnitude)))
        return math.acos(Vector.Dot(v, Vector.right) / (v.magnitude * Vector.right.magnitude))

    @staticmethod
    def Distance(v1, v2):
        return math.sqrt(math.pow((v2-v1).magnitude,2))

    @staticmethod
    def Dot(v1, v2):
        return (v1.x*v2.x + v1.y*v2.y)

    @staticmethod
    def ToList(v):
        return (v.x, v.y)

    @staticmethod
    def Abs(v):
        return Vector(abs(v.x), abs(v.y))

Vector.right = Vector(1,0)
Vector.left = Vector(-1,0)
Vector.up = Vector(0,-1)
Vector.down = Vector(0,1)
Vector.one = Vector(1,1)
Vector.zero = Vector(0,0)