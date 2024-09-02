for i in range(6):
    if(i==4):
        break
    print(i)

else:
    print("Sorry no i")

i = 0
while i<7:
    print(i)
    i = i +1
    if(i==4):
        break
else:
    print("Sorry no i")


for x in range(5):
    print (f"iteration no {x+1} in for loop")
else:
    print ("else block in loop")
print ("Out of loop")

#  if loop will execute without any interruption 
# after executing the last iteration the condition will
# become false and else block will execute
# but if we break at some condition then the conditon
# never becomes false actually, hence else block will
# not execute