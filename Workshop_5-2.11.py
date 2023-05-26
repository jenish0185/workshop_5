for i in range(2,6):
    for j in range(1,11):
        if i==3:
            continue
        else:
            print(i, "*", j, "=", j*i, end="\t")
    print()