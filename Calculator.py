import math


a = int(input("Enter first number:"))

print("Select operation.")    
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide")

c = int(input("Enter Choice(1/2/3/4):"))

b = int(input("Enter second number:"))

if c==1:
    d = a  + b
elif c==2:
    d = a - b     
elif c==3:
    d = a * b 
elif c==4 & b!=0:
    d = a / b 
else:
    print("Error: Invalid Input")
        
print("Result:", d)
