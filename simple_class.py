# Задание 1.
# Создать класс с двумя переменными.
# Добавить функцию вывода на экран и функцию изменения этих переменных.
# Добавить функцию, которая находит сумму значений этих переменных,
# и функцию которая находит наибольшее значение из этих двух переменных.

class smth():
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def output(self):
        print(f'first is {self.first}, while second is {self.second}')
        
    def change(self, third, fourth):
        self.first = third
        self.second = fourth
        
    def sum(self):
        summ = self.first + self.second 
        print(f'sum is {summ}')
        return summ
    def the_biggest(self):
        return max(self.first, self.second)
    
test = smth(1,2)
test.output()
test.sum()
print(test.the_biggest())
test.change(3,4)
test.output()
test.sum()
print(test.the_biggest())
