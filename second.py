# Исходный список содержит положительные и отрицательные числа.
# Требуется положительные поместить в один список, а отрицательные - в другой.
# Для создания списка использовать модуль random
from random import randint
raw  = [ randint(-100,100) for element in range(1,100)  ]
print(f'raw : {raw}')
positive = []
negative = []
for elem in raw:
    if elem >= 0:
        positive.append(elem)
    else:
        negative.append(elem)
print(f'+: {positive}')
print(f'-: {negative}')
