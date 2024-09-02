name = "Harry,Shubham"
print(name[0:5])
print(len(name))
len1 = len("Mango")
print("Mango is a",len1,"character word.")

fruit = "Mango"
mangolen = len(fruit)
print(mangolen)
print(fruit[0:4]) # inclusing 0 but not 4
print(fruit[1:4]) 
print(fruit[:5])
print(fruit[0:len(fruit)-3])

print(fruit[-1:-3])
print(fruit[-3:-1])

# Quick Quiz:
nm = "Harry"
print(nm[-4:-2])

# ans = ar

pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index