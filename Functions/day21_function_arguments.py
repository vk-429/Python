#  default argument
# def average(a=9,b=1): 
#     print("The average is ",(a+b)/2)

# average(3,6)
# average()
# average(5)
# average(b=9)
# average(b=9,a=21) # Keyword Argument, order doesn't matter
# Required Argument

# def name(fname,mname = 'Jhon', lname = "Whatson"):
#     print("Hello", fname,mname,lname)

# name("Amy", "Agrawal", "Jain")

# Varuable length argument
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

c = average(5,6,7,8,9)
print(c)

def name(**name):
    print(type(name))
    print("Hello", name["fname"],name["mname"],name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")




