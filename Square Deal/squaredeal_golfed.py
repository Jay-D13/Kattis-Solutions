i=lambda:map(int,input().split())
a,b=i()
c,d=i()
e,f=i()
print(["NO","YES"][e==b+d+f or d+f==c+b or f+c==e+b])