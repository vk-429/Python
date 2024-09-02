x = 4
y =10
print(x)

def hello():
    x = 5
    print(f"\nThe local x is {x}")
    # print("Hello Vivek")
    global y
    print("Changing y from within the function hello\n")
    y = 5

print(f"The global x is {x}")
print(f"The global y is {y}")
hello()
print(f"The global y is {y}")


