sum=0
while True:
    n=int(input('Enter a positive number (<100) : '))
    print('Press 101 to end')
    if n<100:
        sum = sum + n
    elif n == 0:
        print('Enter a positive integer')
    elif n == 101:
        break
    else:
        print('Enter a number less than 100')
    print("The sum is : ", sum)

