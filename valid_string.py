a=input()
b=set(a)
x=[]
c=0
for i in b:
    x.append(a.count(i))
for i in x:
    if i!=max(x):
        c+=1
if c<=1:
    print("Valid String")
else:
    print("Not Valid")