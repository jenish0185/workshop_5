def largest(a):
    num=str(a)
    b=0
    for i in num:
        if int(i)>b:
            b=int(i)
    print(b)
largest(86421)