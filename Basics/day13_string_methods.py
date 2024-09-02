a = "!!Harry !!!!!!!!!! Harry!!!" # I can't change a, but i can make a copy of it
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))

blogHeading = "intrOductioN to js"
print(blogHeading.capitalize())

str1 = "welcome to console!!!"
print(len(str1))
print(str1.center(50))
print(a.count("Harry"))

print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "welcome00"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())
print(str1.isupper())

str1 = "we wish you a Merry Christmas\n"
print(str1.isprintable())

str1 = "        "
print(str1.isspace())
str1 = "        "
print(str1.isspace())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())

str2 = "   Silver Spoon "
print(str2.strip())