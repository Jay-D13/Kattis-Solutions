string = input()

def cyclicString(s):
    for i in range(len(s)):
        
        #reversed substring of s
        t = s[0:i][::-1] 
        
        # we concatenate 's' to itself to show the cycles
        cycledS = s*2 
        
        # if the reverse substring is not in the cycled string
        # then it is not internally reversibly cyclic
        if t not in cycledS:
            return 0
        
    return 1
    
print(cyclicString(string))