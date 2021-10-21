def Ques9(n):
    if(n>9):
        Rev_num = 0
        while(n>0):
            remainder = n%10
            Rev_num = (Rev_num*10) + remainder
            n = n //10
        return Rev_num
    print("Not a two digit number")

num = int(input("Enter your number: "))
if (num>9):
    print("Reverse of ",num,"is: ", Ques9(num))
else:
    print("Enter 2 digit number")
     