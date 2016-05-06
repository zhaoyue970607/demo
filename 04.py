class Shape(object):
    @property
    def area(self):
        pass
class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(side, side)
class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        super().__init__()
        self.width = width
        self.height = height         
    @property
    def area(self):
        return self.width * self.height         

class Ellipse(Shape):
    pi = 3.1415926535
    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y         
    @property
    def area(self):
        return self.x * self.y * self.pi        
class Circle(Ellipse):
    def __init__(self, r=0):
        super().__init__(r, r)         
shapes = [Ellipse(10,20), Square(15), Circle(5), Rectangle(20,15), Circle(5), Square(15), Ellipse(10,20)] 
def computer__area(shapes):
    areas = [a.area for a in shapes]
    return sum(areas)
total__area = computer__area(shapes)
print('total_area: ',total__area)
