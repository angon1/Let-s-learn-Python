for i in range(1,10):
    if(i<=5):
        for j in range(i):
            print("*",end="")
        print()
    if(i>=5):
        for j in range(6,i):
            print("*",end="")
        print()