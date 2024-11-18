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

question, correct_answer = generate_question()
