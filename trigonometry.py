import math

def triangle_area_heron(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

side1, side2, side3 = 3, 4, 5
area = triangle_area_heron(side1, side2, side3)
print(f"Triangle Area: {area}")
