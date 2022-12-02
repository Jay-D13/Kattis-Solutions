import sys
import math
    
triangles = []
for line in sys.stdin:
    triangles.append(list(map(int, line.split())))

triangles.pop(0)[0]

l = 0
for i in triangles:
    a = i[0]
    b = i[1]
    c = i[2]

    angleBC = math.acos((b**2+c**2-a**2)/(2*b*c))
    
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    medianAB = math.sqrt((c/2)**2+b**2-b*c*math.cos(angleBC))

    height = (2 * (area/2))/medianAB

    l += height*2

print(l)
