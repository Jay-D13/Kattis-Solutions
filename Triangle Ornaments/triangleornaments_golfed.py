l=0
for i in[[*(map(int,input().split()))]for p in[1]*int(input())]:
 a,b,c=i
 s=sum(i)/2
 l+=4*(-((a-s)*(b-s)*(c-s)*s)/(2*(a**2+b**2)-c**2))**.5
print(l)