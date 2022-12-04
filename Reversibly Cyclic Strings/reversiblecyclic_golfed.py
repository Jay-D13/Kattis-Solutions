"""
Progression:

33 chars:
    You only need to verify the final 'in' check: 
        -> verifying that the full string in reverse is in the doubled string 
           (doubled string = popping out the pausible cycle)
"""
s=input()
print(+(s[::-1]in s*2))


"""
59 chars:
    Little python list/string splitting trick
"""
s=input()
print(+all(s[i::-1]in s*2for i in range(len(s))))


"""
62 chars:
    Discovered you can add `+` to a bool condition to turn it into an int
"""
s=input()
print(+all(s[:i][::-1]in s*2for i in range(len(s))))


"""
66 chars
"""
s=input()
print(int(all(s[:i][::-1]in s*2for i in range(len(s)))))
