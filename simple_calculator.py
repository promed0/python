#create a calculator using addition , multiplication , substract, division, expotential, modulus fully basic operatio

print("Enter Your first number value")
a=int(input())
print("Enter Your second number value")
b= int(input())
print("You can enter those operator in your calcullation \n \n Addition, substraction, multiplication, division, floor division, Expotential and Modulus\n \n ")
print("Enter your operator for continue your calculation\n")
c=str(input())

if(c=="+"):
 print("Your addition value is", a+b)
elif(c=="-"):
 print("Your substraction value is", a-b)
elif(c=="*"):
 print("Your multiplication value is", a*b) 
elif(c=="/"):
 print("Your division value is", a/b) 
elif(c=="//"):
 print("Your floor division value is", a//b) 
elif(c=="**"):
 print("Your expotential value is", a**b) 
elif(c=="%"):
 print("Your modulus value is", a%b)     
else:
 print("Error operator \n please enter a valid operator for continu your calculation\n")

