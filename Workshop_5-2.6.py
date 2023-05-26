p=0
n=0
z=0
while True:
    a=int(input("Enter a number: "))
    print('press 101 to end')
    if a==101:
        break
    elif a>0:
        p=p+1
    elif a<0:
        n=n+1
    elif a==0:
        z=z+1
    else:
        print('invalid input')

print(f'The number of positive numbers is {p}. The number of negative numbers is {n}. The number  of zero is {z}')





