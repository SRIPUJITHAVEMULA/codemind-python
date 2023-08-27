a=input()
c=0
maxx=0
for i in range(len(a)):
    if a[i] in "123456789":
        c=c+int(a[i])
print(c)