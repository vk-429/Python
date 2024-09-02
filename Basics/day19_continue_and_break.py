for i in range(12):
    if(i==10):
        break
    print("5 x ",i+1,"=",5*(i+1))
    

print("Loop ko chhodkar nikal gya\n")

for i in range(12):
    if(i>=10):
        print("Skip the iteration")
        continue
    print("5 x ",i+1,"=",5*(i+1))

i = 1
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break