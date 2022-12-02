import sys

classes = []
for line in sys.stdin:
    classes.append(list(map(int,line.strip().split(" "))))
classes.pop(0)
for c in classes:
    numStudents = c.pop(0)
    average = sum(c)/len(c)
    count = len([i for i in c if i > average])
    print("{:.3f}".format((count/numStudents)*100) + "%")