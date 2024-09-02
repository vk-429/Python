import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

questions = [
        # Easy questions
        {
            "question": "What is the capital of France?",
            "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
            "answer": "A",
            "prize": 1000
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A) Charles Dickens", "B) J.K. Rowling", "C) William Shakespeare", "D) Leo Tolstoy"],
            "answer": "C",
            "prize": 2000
        },
        {
            "question": "What is the largest planet in our Solar System?",
            "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
            "answer": "B",
            "prize": 3000
        },
        {
            "question": "What is the boiling point of water?",
            "options": ["A) 90°C", "B) 100°C", "C) 110°C", "D) 120°C"],
            "answer": "B",
            "prize": 5000
        },
        # Medium questions
        {
            "question": "Who is known as the 'Father of Computers'?",
            "options": ["A) Charles Babbage", "B) Alan Turing", "C) Bill Gates", "D) Steve Jobs"],
            "answer": "A",
            "prize": 10000
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["A) Oxygen", "B) Gold", "C) Osmium", "D) Silver"],
            "answer": "A",
            "prize": 20000
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
            "answer": "C",
            "prize": 40000
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Michelangelo"],
            "answer": "C",
            "prize": 80000
        },
        # Hard questions
        {
            "question": "What is the main ingredient in traditional guacamole?",
            "options": ["A) Tomatoes", "B) Avocado", "C) Mango", "D) Potato"],
            "answer": "B",
            "prize": 160000
        },
        {
            "question": "What is the currency of Japan?",
            "options": ["A) Dollar", "B) Peso", "C) Yen", "D) Euro"],
            "answer": "C",
            "prize": 320000
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
            "answer": "B",
            "prize": 640000
        },
        {
            "question": "Who invented the telephone?",
            "options": ["A) Alexander Graham Bell", "B) Nikola Tesla", "C) Thomas Edison", "D) Guglielmo Marconi"],
            "answer": "A",
            "prize": 1250000
        },
        # Very hard questions
        {
            "question": "Which is the longest river in the world?",
            "options": ["A) Amazon", "B) Nile", "C) Yangtze", "D) Mississippi"],
            "answer": "B",
            "prize": 2500000
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Platinum"],
            "answer": "C",
            "prize": 5000000
        },
        {
            "question": "Which country hosted the 2016 Summer Olympics?",
            "options": ["A) China", "B) Brazil", "C) USA", "D) Russia"],
            "answer": "B",
            "prize": 10000000
        },
        {
            "question": "Which physicist developed the theory of general relativity?",
            "options": ["A) Isaac Newton", "B) Galileo Galilei", "C) Albert Einstein", "D) Niels Bohr"],
            "answer": "C",
            "prize": 70000000
        }
    ]

def quiz_game():

    total_money = 0
    current_money = 0
    for idx, q in enumerate(questions):
        while True:
            clear_screen()
            print("########################## KAUN BANEGA KARORPATI ##########################\n")
            print(f"Question {idx+1}: {q['question']}")
            for option in q['options']:
                print(option)
            
            print(f"\nPrize Money: {q['prize']}\n")
            user_answer = input("Enter Your Answer (A/B/C/D) or Enter Q if You Want to Quit the Game: ").strip().upper()
            if user_answer in ['A', 'B', 'C', 'D', 'Q']:
                break
            else:
                print("Please Enter a Valid Option (A/B/C/D).")
                time.sleep(2)

        if user_answer == 'Q':
            print("Quitting The Game!")
            time.sleep(2)
            clear_screen()
            print("\n")
            if idx>9:
                print("Congratulations! ")
            print(f"You Won a Total of ₹{current_money}.")
            if idx<=9 :
                print("Better Luck Next Time!")
            print("\n")
            break
        elif user_answer == q['answer']:
            current_money = q['prize']
            if(idx == 4 or idx == 9 or idx == 15):
                total_money = current_money
            print(f"Correct Answer! You Have Won ₹{q['prize']}.")
            time.sleep(2)
        else:
            print("Wrong Answer!!!")
            time.sleep(2)
            clear_screen()
            print("\n")
            if idx>9:
                print("Congratulations! ")
            print(f"You Won a Total of ₹{total_money}.")
            if idx<=9 :
                print("Better Luck Next Time!")
            print("\n")
            break
    else:
        clear_screen()
        print(f"\nAmazing! You Answered All The Questions Correctly And Won a Total of ₹{total_money}!\n")

quiz_game()
