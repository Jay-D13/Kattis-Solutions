d={}
for _ in[1]*int(input()):
 r=d
 for j in input():
  if j not in r:r[j]={"":0}
  r=r[j];r[""]+=1
 print(r[""]-1)