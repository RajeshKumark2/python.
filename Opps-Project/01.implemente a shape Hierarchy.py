class Shape: 
    def are(self):
        raise NotImplementedError("Subclasses must implement")
    
class Circle(Shape):
    def __init__(self, radies): 
        self.radies = radies 

    def area(self): 
        return 3.14 * self.radies ** 2 
    
class Square(Shape): 
    def __init__(self, side): 
        self.side = side

    def area(self): 
        return self.side ** 2 
     
shapes = [Circle(5), Square(4)]
for shape in shapes: 
    print(f"Area: {shape.area()}")