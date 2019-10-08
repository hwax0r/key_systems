from math import pi, sqrt

class geometric_figures():
    
    def __init__(self, a, b = None, c = None):
        self.a = a
        self.b = b
        self.c = c
        
    def info(self):
        return __class__.__name__
    
class volumetric(geometric_figures):
    
    def volume(self):
        if self.b == None:
            return self.a**3
        elif self.c == None:
            return 'Error' 
        else:
            return self.a * self.b * self.c
        
    def info(self):
        return __class__.__name__

class flat(geometric_figures):
    
    def square(self):
        if self.b == None:
            return self.a**2
        else:
            return self.a * self.b
        
    def perimeter(self):
        if self.b == None:
            return self.a*2
        else:
            return self.a + self.b
        
    def info(self):
        return __class__.__name__
        
class vertex(geometric_figures):
    
    def info(self):
        return __class__.__name__

class non_vertex(geometric_figures):
    
    def info(self):
        return __class__.__name__

class ellipse(geometric_figures):
    
    def perimeter(self):
        return pi * sqrt(3/2*(self.a+self.b) - sqrt(self.a * self.b))
    
    def square(self):
        return pi * self.a * self.b
    
    def info(self):
        return __class__.__name__

class circle(geometric_figures):
    def square
    
    def info(self):
        return __class__.__name__

new = volumetric(12,2,3)
print(new.info())
