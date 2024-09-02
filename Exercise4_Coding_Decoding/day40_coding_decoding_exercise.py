import random
import string

def append_random_char_end(s):
    i = 0
    while i<3:
        random_char = random.choice(string.ascii_letters + string.digits)
        s = s + random_char
        i = i + 1
    return s

def append_random_char_start(s):
    i = 0
    while i<3:
        random_char = random.choice(string.ascii_letters + string.digits)
        s = random_char + s
        i = i + 1
    return s

while True:
    print("1. Want to Code")
    print("2. Want to Decode")
    print("3. Want to Exit")

    choice = int(input("Enter Your Choice: "))
    if choice == 3:
        break
    content = input("\nEnter Content to Code:-\n")
    words = content.split()
    result = []

    match choice:
        case 1:
            for word in words:
                if len(word)<=2:
                    word = word[::-1]
                else:
                    word = word[1:] + word[0]
                    word = append_random_char_end(word)
                    word = append_random_char_start(word)
                result.append(word)
            result = " ".join(result)
        case 2:
            for word in words:
                if len(word)<=2:
                    word = word[::-1]
                else:
                    word = word[3:-3]
                    word = word[-1] + word[:-1]
                result.append(word)
            result = " ".join(result)
        case _:
            print("Please Enter a Valid Choice!")
            
    if(choice == 1 or choice == 2):
        print(f"\nRequired Result:- \n{result}\n")
