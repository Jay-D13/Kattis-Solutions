s=0
for i in input().split(';'):

    if'-'in i:
        
        a=list(map(int,i.split('-')))
        s+=a[1]-a[0]+1
        
    else: 
        s+=1

print(s)

# sum(*[1for i in input().split(';')]if'-'not in i)

