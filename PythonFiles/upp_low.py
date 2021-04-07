st=input()
d={"uppercase":0,"lowercase":0}
for c in st:
  if c.isupper():
    d["uppercase"]+=1
  elif c.islower():
    d["lowercase"]+=1
  else:
    pass
print("uppercase letters:",d["uppercase"])
print("lowercase letters:",d["lowercase"])
print(d)