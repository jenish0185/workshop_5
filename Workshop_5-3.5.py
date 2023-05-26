n=int(input("Enter a number:"))
s=9
while n>0:
    a=n%10
    if a<s:
        s=a
    n//=10
print("The smallest number is", s)
