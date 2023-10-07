import math


def compute_circle_area(radius):
    return math.pi * radius ** 2


def compute_triangle_area(side1, side2, side3):
    # Проверка на прямоугольный треугольник
    sides = [side1, side2, side3]
    sides.sort()
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        is_right_triangle = True
    else:
        is_right_triangle = False

    # Вычисление площади по формуле Герона
    semiperimeter = (side1 + side2 + side3) / 2
    area = math.sqrt(semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3))

    return area, is_right_triangle