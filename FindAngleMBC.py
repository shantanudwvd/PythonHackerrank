import math as m
perpendicular = int(input())
base = int(input())
hypotenuse = m.sqrt(perpendicular**2 +base**2)
hypotenuse /= 2
angle = m.degrees(m.asin(hypotenuse/base))
print(round(angle), chr(176).strip())
