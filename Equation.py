#lilly middleman
#01/19/2022

#objectives: Other operators +-*/  ** exponent % modulus
#               Format printing escape character

#program creating an equation, asking user input,
#  and formattinh the output
import os
os.system('cls')
#declare variable
var1=10
var2=2
var3=2.9
var4=5

#calculate equation given
#print format
# print(2**4)
result= (3*var1 - 2*(var2)**2/var3)/var4
print("var1= %5d "% var1)
print("var2= %5d "% var2)
print("var3= %8.2f "% var3)
print("var4= %5d "% var4)
print("result = %6.2f "% result, end=" ----")

print("the \" quotes\" tabs \t backslash \\")