# #Previous version 99 chars:
# p=int(input().split()[1])
# b=c=0
# for x in map(int,input().split()):b=max(b,c:=max(0,c+x-p))
# print(b)

#87 chars:
i=lambda:map(int,input().split())
_,p=i()
c=0
print(max([c:=max(c+x-p,0)for x in i()]))
