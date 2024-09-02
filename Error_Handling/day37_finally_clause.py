
def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the Index: "))
        print(l[i])
        return 1
    except:
        print("Some Error Occured!")
        return 0
    finally:
        print("I am Always Executed")
    # print("I am Always Executed")

x = func1()
print(x)
