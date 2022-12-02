#A < B < C
import sys

abc = []
for line in sys.stdin:
    abc.append(line.strip())
nums = sorted(list(map(int, abc[0].split())))
map = {'A': nums[0], 'B': nums[1], 'C': nums[2]}
result = ""
for l in abc[1]:
    result += str(map[l]) + " "
print(result)
