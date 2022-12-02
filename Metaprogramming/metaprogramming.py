import sys
defined = {}

inputs = [line.strip().split() for line in sys.stdin]

for i in inputs:

    if i[0] == "define":
        defined[i[2]] = int(i[1])
        
    if i[0] == "eval":
        if i[1] not in defined or i[-1] not in defined:
            print("undefined")
        elif i[2] == "<":
            print("true" if defined[i[1]] < defined[i[-1]] else "false")
        elif i[2] == "=":
            print("true" if defined[i[1]] == defined[i[-1]] else "false")
        elif i[2] == ">":
            print("true" if defined[i[1]] > defined[i[-1]] else "false")
            
print(defined)