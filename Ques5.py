def Sales(sales):
    if (sales>50000):
        print("Total sales: ",sales)
        print("Total commission: ", 0.05*sales)
        if(sales>=80000):
            print("Excellent")
        elif(sales>60000 and sales<80000):
            print("Good")
    
        elif (sales >=40000 and sales < 60000):
            print("Average")

        elif (sales < 40000):
            print("Work Hard")
    else:
        print("Total sales: ", sales)
        if (sales >=40000 and sales < 60000):
            print("Average")

        elif (sales < 40000):
            print("Work Hard")

spw=int(input("Enter the Sales per week"))
spm=4*spw
Sales(spm)