class Rectangle:
    
    def __init__(self, width, length ):
        self.width = width
        self.length = length
    
    def perimeter(self):
        return 2 * self.width + 2 * self.length
        
    def area(self):
        return self.width * self.length
        
obj1 = Rectangle(7,5)
print(obj1.perimeter())
print(obj1.area())