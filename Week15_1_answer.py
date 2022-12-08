from math import sqrt
class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Segment2D:
    dist = 0.0
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def getDist(self):
        self.dist = sqrt((self.p2.x-self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
        return self.dist

p1 = Point2D(30,20)
p2 = Point2D(x=60,y=50)

s1 = Segment2D(p1,p2)
c = s1.getDist()

print(c)
