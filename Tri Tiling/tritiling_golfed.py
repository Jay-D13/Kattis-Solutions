# t=lambda n:0if n&1else 3if n==2else 4*t(n-2)-t(n-4)if n else 1

# t=lambda n:4*t(n-2)-t(n-4)if n>2else[~n&1,3][n==2]
# while(n:=int(input()))+1:print(t(n))

# [1,y][b] -> y**b (-n//2)**(~n%2)
# -(-n//1)
s=2+3**.5
while(n:=int(input()))+1:print(~n%2*round((s+1)*s**(n/2)/6))

# s=2+3**.5
# while(n:=int(input()))+1:print(round((1+s)*s**n/6)*((n:=n//2)%2==0))

# s=2+3**.5
# while(n:=int(input())//2)+1:print(round((1+s)*s**n/6))

# s=3**.5
# while(n:=int(input())//2)+1:print(~(n==2)&round((3+s)*(2+s)**n/6))