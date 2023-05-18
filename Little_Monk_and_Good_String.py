a=list(input())
vowels=['a','e','i','o','u']
c=0
res=0
for i in range(len(a)):
    if a[i] in vowels:
        c+=1
        res=max(res,c)
    else:
        c=0
print(res)