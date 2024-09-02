marks = [3,5,6,"Harry",True,7,8,10,20,30]
print(marks)
print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])

# Separated by comma(,) and enclosed within square braces([])
# Changeable/mutable
# ordered collection
# It can store different types of data
# Bound checking available

# Negative Indexing
# print(marks[-3]) # Positive index = length - negative index
# print(marks[len(marks)-3])
# print(marks[5-3])
# print(marks[2])

if "Harry" in marks:
    print("Yes")
else:
    print("No")

# Same applies for string as well
if "arry" in "Harry":
    print("Yes")

print(marks)
print(marks[1:])
print(marks[1:-1])
print(marks[1:8:2]) # 2 - Jump index