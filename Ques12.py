def Ques12(s:str,s1:str):
    count = 0
    for i in range(len(s)):
        if s[i] in s1:
            count += 1
    return count
a = input("String I: ")
b = input("String II : ")
print("Matching characters: ",Ques12(a,b))