a = int(input("Enter Your Age: "))
print("Your age is:",a)

# Conditional Operators
# >, <, >=, <=, ==
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if(a>18):
    print("You can drive")
else:
    print("You cannot drive")
    print("No")
print("Yay!")

applePrice = 190
budget = 200
if(budget - applePrice > 50):
    print("Alexa, add 1 kg Apples to the cart.")
elif(budget - applePrice >70):
    print("Its Okay you can buy")
else:
    print("Alexa, do not add Apples to the cart.")