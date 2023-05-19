a=int(input())
b=int(input())
for num in range(a,b+1):
    temp=num
    rev=0
    while(temp>0):
        rem=temp%10
        rev=(rev*10)+rem
        temp=temp//10
    if(num==rev):
        print("%d "%num,end="")