a=int(input("Enter a number:"))
sum=0
while a>0:
    s=a%10
    sum+=s
    a//=10
print("The sum is", sum)
