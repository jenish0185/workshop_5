sum=0
for i in range (1,201):
    if i<100:
         continue
    if i%2==0:
        sum=sum+i
    elif i == 201:
        break
print(sum)



