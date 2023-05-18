def getsecondmostfreq(str):
    no_of_chars=256
    count=[0]*no_of_chars
    for i in range(len(str)):
        count[ord(str[i])]+=1
    first,second=0,0
    for i in range(no_of_chars):
        if count[i]>count[first]:
            second=first
            first=i
        elif (count[i]>count[second] and count[i]!=count[first]):
            second=i
    return chr(second)
str=input()
res=getsecondmostfreq(str)
if res!=NULL:
    print(res)
else:
    print("-1")