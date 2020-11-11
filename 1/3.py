import math
x = float(input('qual é o ângulo?:'))
y= math.sin(math.radians(x))
z= math.cos(math.radians(x))
c= math.tan(math.radians(x))
print('o cosseno do ângulo é {}, o seno é {} e a sua tangente é {}'.format(y,z,c))
