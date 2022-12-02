import sys

def cake(n, h, v):
    areas = [v*h, (n-v)*h, (n-h)*v, (n-h)*(n-v)]
    return max(areas)*4
    
vars = []
for line in sys.stdin:
    vars = line.split()

print(cake(int(vars[0]),int(vars[1]),int(vars[2])))