inputs = [map(int, input().split()) for _ in"123"]

h1,w1 = map(int,inputs[0])
h2,w2 = map(int,inputs[1])
h3,w3 = map(int,inputs[2])


if (h1==h2==h3 and w1+w2+w3==h1): #case side by side
    print("YES")
elif w2+w3==h1 and h2==h3 and h2+w1==h1: #rotate 1
    print("YES")
elif w2+h3==h1 and h2==w3 and h2+w1==h1: #rotate 2
    print("YES")
elif w3+h2==h1 and w2==h3 and h3+w1==h1: #rotate 3
    print("YES")
else: print("NO")
