import math

class Shape(object):        
    def _init_(self,base,side,theta=90):
        self.base=base
        self.side=side
        self.theta=theta

    def area(self):
        return self.base*self.side*math.sin(math.radians(self.theta))

    def bst(self):
        return [self.base, self.side, self.theta]

    def _str_(self):
        return 'I am a %s with area of %d' % (type(self)._name_, self.area())

class Rectangle(Shape):     
    def _init_(self, base, side):
        super(Rectangle, self)._init_(base,side)
        
class Rhombus(Shape):
     def init(self, base, theta):
        super(Rhombus, self).init(base,base,theta)

class Parallelogram(Shape):       
    def init(self, base, side, theta):
        super(Parallelogram, self).init(base,side,theta)