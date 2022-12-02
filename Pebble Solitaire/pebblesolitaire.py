s=lambda p:min([s(p[:i]+"o--"[::j]+p[i+3:])for i in range(12)for j in(1,-1)if p[i:i+3]=="-oo"[::j]]+[p.count('o')])
exec("print(s(input()));"*int(input()))