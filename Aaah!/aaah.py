import sys
v = []
for l in sys.stdin:
    v.append(l)
print(v)
print("go") if v[0].count('a') >= v[1].count('a') else print("no")