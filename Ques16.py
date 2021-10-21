def Ques16(lst:list):
    y = [0]*len(lst)
    for i in range(len(lst)):
        for j in range(i,-1,-1):
            y[i] +=lst[j]
    return y
n = int(input("No of Elements: "))
a = []
if n>0:
    for i in range (n):
        a.append(int(input("Enter element: ")))
    print("Entered list: ")
    print("Entered list: ",a)
    print("Cumulative list: ",Ques16(a))
    
