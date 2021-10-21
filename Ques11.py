def Ques11(x, n):
    sum = 1
    term = 1
    fct = 1
    p = 1
    multi = 1
    for i in range(1, n):
        fct = fct * multi * (multi+1)
        p = p*x*x
        term = (-1) * term
        multi += 2
        sum = sum + (term * p)/fct
    return sum

x = 9
n = 10
print("x=3, n=5: ",Ques11(x, n))