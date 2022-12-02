def t(n):

    if n==1:
        return 0
    if n == 0:
        return 1
    if n == 2:
        return 3
 
    return 4*t(n-2) - t(n-4)


while True:
    n = int(input())
    if n < 0: break
    print(t(n))
    