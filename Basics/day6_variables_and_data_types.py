# Built in data types
a=12
print(a)
b="Harry" # "" are used to specify that it is a string
print(b)
c=True
d=None
# print(a+b) # error a and b should be of same type
a1=9
print(a+a1)
print("The type of a is ",type(a))
print("The type of a is ",type(b))
print("The type of a is ",type(c))
print("The type of a is ",type(d))

e=complex(4,3)
print("The type of a is ",type(e))
f=1.1
print("The type of a is ",type(f))

# list - collection of elements, can have different data types
# list can contain a list inside it
list1 = [2,3.4,[-4,5],["Apple","Banana"]]
print(list1)

# tuple - they are immutable means they can not be changed
# tuple is also the collection of various types of element

tuple1=(("parrot","sparrow"),("lion","tiger"))
print(tuple1)

# dict - map data type (key,value) pair
dict1 = {"name":"sakshi","age":20,"canvote":True}
print(dict1)