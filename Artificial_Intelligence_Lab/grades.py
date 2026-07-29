a=int(input("Enter Your marks for AI:"))
b=int(input("Enter Your marks for DS:"))
c=int(input("Enter your marks for OS:"))
d=int(input("Enter your marks for DM:"))
e=int(input("Enter your marks for DELD:"))

avg=(a+b+c+d+e)/5

print("Your Total percentage is :",avg)

if(60>avg>40):
 print("Your grade is Second Class")
elif(75>avg>60):
 print("Your grade is First class")
elif(100>avg>75):
 print("Your grade is Distinction")
else:
 print("You are failed")
