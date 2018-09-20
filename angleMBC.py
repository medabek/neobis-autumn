import math

ab=int(input())
bc=int(input())
ac=math.sqrt(ab**2 + bc**2)

sinO=(ac/2)/bc

angle = round(180*sinO/math.pi)
print(angle,"°")
