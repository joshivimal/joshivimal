def Ques3(s1, s2, s3):
    if(s1+s2>=s3 and s1+s3>=s2 and s2+s3>=s1):
        semiPer = s1+s2+s3/3
        return (semiPer*(semiPer-s1)*(semiPer-s2)*(semiPer-s3))**0.5
    print("The pair is not a triangle")

print(Ques3(4,3,10))