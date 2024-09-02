marks = [12,56,32,98,12,45,1,4]

index = 0
for mark in marks:
    print(mark, end = " ")
    if(index == 3):
        print("\nHarry, awesome")
    index += 1

print("\n")

for index,mark in enumerate(marks,start =1):
    print(mark,end = " ")
    if(index == 3):
        print("\nHarry, awesome")

print("\n")