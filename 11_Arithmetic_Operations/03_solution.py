
import random

def generate_question():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    print(num1) # choose the 1-20 number
    print(num2) # choose the 1-20 number
    operation = random.choice(operations)
    print(operation) # choose random opreation 
    
    # Avoid division by zero and ensure integer division
    if operation == '/':
        num1 = num1 * num2  # Ensures the division results in an integer
    question = f"{num1} {operation} {num2}"
    answer = eval(question)  # Evaluate the correct answer
    print("answer", answer)
    return question, answer


def arithmetic_game():
    print("Welcome to the Arithmetic Quiz Game!")
    print("Solve as many questions as you can. Type 'exit' to quit.")
    
    score = 0
    while True:
        question, correct_answer = generate_question() # method call 
        
        # Ask the user input 
        print(f"\nQuestion: {question}")
        user_input = input("Your answer: ")
        
        if user_input.lower() == 'exit':
            break
        
        # Check if the answer is correct
        # try-except (try-catch block in javascript) 
        # understad the flow of code base 
        try:
            user_answer = float(user_input)
            if abs(user_answer - correct_answer) < 1e-5:  # Allow minor float differences
                print("Correct! 🎉")
                score += 1
            else:
                print(f"Wrong. The correct answer was: {correct_answer}")
        except ValueError:
            print("Invalid input. Please enter a number or 'exit'.")
    
    print(f"\nGame Over! Your final score is: {score}")

arithmetic_game()
