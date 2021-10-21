n = int(input("Enter the number of rows : "))
for i in range(n):
    for m in range(n-i):
        print(' ',end="")
    for j in range(i+1):
        print((i+j+1)%10,end="")
    for k in range(2*i,i,-1):
        print(k%10,end="")
    print()