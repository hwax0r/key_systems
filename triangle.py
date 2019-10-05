# Задание 2.
# Описать класс, представляющий треугольник.
# Предусмотреть методы для создания объектов, вычисления площади,
# периметра и точки пересечения медиан.
# Описать свойства для получения состояния объекта.
from math import sqrt, sin, pi, radians

class triangle():
    def __init__(self, a, b, c, alpha = None):
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        
    def area(self):
        p = (self.a + self.b + self.c) / 2
        result = sqrt( p * (p - self.a) * (p - self.b) * (p - self.c) )
        return result
        
    def area_sin(self):
        if self.alpha == None:
            pass
        else:
            return 0.5 * self.a * self.b * sin(radians(self.alpha))

    def perimeter(self):
        return self.a + self.b + self.c

    def median(self):
        pass
    
    def info(self):
        print('____info about triangle____')
        print(f'sides are {self.a}, {self.b}, {self.c}')
        print(f'area is {self.area()}')
        #print(f'area_sin is {self.area_sin()}')
        print(f'perimetr is {self.perimeter()}')
        print('___________________________')

new = triangle(3,4,5)
new.info()
