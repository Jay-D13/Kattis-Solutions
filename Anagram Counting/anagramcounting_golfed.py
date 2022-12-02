import sys,math as m
f=m.factorial
for i in sys.stdin:print(f(len(i)-1)//m.prod(f(i.count(j))for j in set(i)))

#Note to self: on peut faire len(i)-1 au lieu de len(i.strip()) car le formattage du .in fait que 
#toutes les entrées ont un '\n'

# f=lambda x:x*f(x-1)if x else 1
# import sys
# import math
# for i in sys.stdin:print(math.factorial(len(i.strip()))//math.prod(map(i.count,set(i))))
