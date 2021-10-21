def Ques14(s:str):
    s1 = ""
    s1 = s[::-1] #Extended slice syntax
    if s1==s:
        return True
    return False
string1 = input("Enter your String: ")
print("Is entered string palindrome: ",Ques14(string1))