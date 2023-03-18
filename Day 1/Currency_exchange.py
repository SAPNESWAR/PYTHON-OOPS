curr=input("Enter the Currency")
amnt=int(input("Enter the inr"))
if(curr=="Euro"):
    print(amnt*0.01417)
elif(curr=="British pound"):
    print(amnt*0.0100)
elif(curr=="Austrilian dollar"):
    print(amnt*0.02140)
elif(curr=="Canadian dollar"):
    print(amnt*0.02027)
else:
    print("Invalid")
    
    
    
