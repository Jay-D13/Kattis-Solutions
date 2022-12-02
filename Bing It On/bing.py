dictionary={}

for _ in range(int(input())):
    
    reference=dictionary
    
    for char in input():
        if char not in reference:
            reference[char] = {"counter":0}
            
        reference=reference[char]
        reference["counter"]+=1
        
    print(reference["counter"]-1)