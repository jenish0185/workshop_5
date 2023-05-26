s=input("Enter a string:")
v="aAeEiIoOuU"
count=0
for i in s:
    if i in v:
        count+=1
print("Number of vowels :", count)
