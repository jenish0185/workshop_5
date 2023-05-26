n=0
sum=0
d=0
while n<=100:
    n=n+1
    if n%3==0 and n%5==0:
        sum=sum+n
    
print(sum)