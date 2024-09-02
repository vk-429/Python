
import random
import msvcrt
import os

mp = {1:"Snake",2:"Water",3:"Gun"}

while True:
    os.system('cls')
    print("\n################ Snake Water Gun ################\n")
    print("1. Snake")
    print("2. Water")
    print("3. Gun\n")

    choice = int(input("Enter Your Choice: "))
    computers_choice = random.randint(1,3)

    print(f"Your Choice: {mp[choice]}")
    print(f"Computer's Choice: {mp[computers_choice]}\n")
    if(choice == computers_choice):
        print("Draw !")
    elif((choice == 1 and computers_choice == 3) or (choice == 2 and computers_choice == 1) or (choice == 3 and computers_choice == 2)):
        print("You Lost !")
    else:
        print("You Won !")

    print("\nWant to Play Again? (Enter y for yes and n for no): ")
    play_again = msvcrt.getch().decode('utf-8')
    play_again = play_again.upper()
    if(play_again == 'N'):
        break

