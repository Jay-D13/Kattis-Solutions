n,h,v=map(int,input().split())
i,j=n-v,n-h
print(max(v*h,i*h,j*v,j*i)*4)