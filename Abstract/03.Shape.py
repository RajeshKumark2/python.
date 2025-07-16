from abc import ABC, abstractmethod 
import math 

class Shape(ABC) :
    @abstractmethod
    def area(self): 
        pass 

    @abstractmethod
    def perimeter(self): 
        pass 

class Circle(Shape): 
    def __init__(self, radies):
        self.radies = radies 

    def area(self): 
        return math.pi * self.radies  
    
    def perimeter(self):
        return 2 * math.pi * self.radies 

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2 

    def perimeter(self):
        return 4 * self.side 
    
shape = [Circle(5), Square(4)]
for s in shape:
    print(f"{s.__class__.__name__}: Area={s.area(): 2f}, perimeter={s.perimeter():2f}")
    