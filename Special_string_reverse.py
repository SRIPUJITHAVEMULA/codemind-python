s=input()
x=""
y=""
z=0
for i in s:
    if i in "abcdefghijklmnopqrstuvwxyz":
        x+=i
x=x[::-1]
for i in range(len(s)):
    if s[i] not in "abcdefghijklmnopqrstuvxyz":
        y+=s[i]
    else:
        y+=x[z]
        z+=1
print(y)