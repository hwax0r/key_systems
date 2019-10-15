from math import pi, sqrt

class geometric_figures():
    
    def __init__(self, a, b = None, c = None):
        self.a = a
        self.b = b
        self.c = c
        
    def info(self):
        return __class__.__name__
    
    def square(self):
        return 'there is no formula of square for this object'
    
    def perimeter(self):
        return 'there is no formula of perimeter for this object'
    def volume(self):
        return 'there is no formula of volume for this object'

    def all_info(self):
        print(f'square = {self.square()}')
        print(f'perimeter = {self.perimeter()}')
        print(f'volume = {self.volume()}')
        print('______________________________________________________________')
    
class volumetric(geometric_figures):
    
    def volume(self):
        if self.b == None:
            return self.a**3
        elif self.c == None:
            return 'Error' 
        else:
            return self.a * self.b * self.c
        

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
        
class vertex(flat):
    
    def info(self):
        return __class__.__name__

class non_vertex(flat):
    
    def info(self):
        return __class__.__name__

class ellipse(non_vertex):
    
    def perimeter(self):
        return pi * sqrt(3/2*(self.a+self.b) - sqrt(self.a * self.b))
    
    def square(self):
        return pi * self.a * self.b
    
    def info(self):
        return __class__.__name__

class circle(non_vertex):
    
    def square(self):
        return pi * (self.a/2)**2
    
    def perimeter(self):
        return pi * self.a
    
    def info(self):
        return __class__.__name__

new = volumetric(12,2,3)
#print(new.info())
neew = geometric_figures(12)
#print(neew.square())
new.all_info()