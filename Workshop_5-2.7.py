
n=int(input("Enter the term"))
sum=0
i=1
count=0
if n==1:
        print(sum)
elif n==2:
        print(i)
else:
    while count < n:
        print(sum)
        fib = sum + i
        sum=i
        i=fib
        count=count+1
