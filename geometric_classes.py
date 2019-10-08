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
    
    def sqare(self):
        if b == None:
            return a**2
        else:
            return a * b
        
    def perimeter(self):
        if b == None:
            return a*2
        else:
            return a + b
        
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
        return pi * sqrt(3/2*(a+b) - sqrt(a*b))
    
    def sqare(self):
        return pi * a * b
    
    def info(self):
        return __class__.__name__

class circle(geometric_figures):
    
    def info(self):
        return __class__.__name__

new = volumetric(12,2,3)
print(new.info())
