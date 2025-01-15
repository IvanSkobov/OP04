#Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа, после return перечислить все значения через запятую): периметр квадрата, площадь квадрата и диагональ квадрата.

import math

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)

    return perimeter, area, diagonal

side_length = float(input("Введите длину стороны квадрата: "))
perimeter, area, diagonal = square(side_length)

print("Периметр квадрата:", perimeter)
print("Площадь квадрата:", area)
print("Диагональ квадрата:", diagonal)