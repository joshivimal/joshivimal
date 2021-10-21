def Ques15_multiply(X,Y,result):
    #Multiplication
    for i in range(len(X)):
     for j in range(len(Y[0])):
      for k in range(len(Y)):
       result[i][j] += X[i][k] * Y[k][j]
    for r in result:
     print(r)
def Ques15_Add(X,Y,result):
    #Add
    for i in range(len(X)):
     for j in range(len(X[0])):
      result[i][j] = X[i][j] + Y[i][j]
    for r in result:
     print(r)

A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

C = [[1, 9, 31],
    [40, 5, 6],
    [17, 8, 9]]

r1 = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]
    
r2 = [[0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

print("ADD: ")
Ques15_Add(A,C,r1)
print("MULTIPLY: ")
Ques15_multiply(A,B,r2)
