dates=[]
for _ in range(int(input())):
    s,f=map(int,input().split())
    for i in range(s,f+1):
        dates+=i,
print(len(set(dates)))