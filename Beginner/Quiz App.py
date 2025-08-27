import random

questions = [
    ("What is 2 + 2?", "4"),
    ("What is the capital of France?", "Paris"),
    ("What is 5 * 3?", "15"),
    ("What is the largest planet?", "Jupiter"),
    ("What is 10 - 7?", "3"),
    ("What is the capital of Japan?", "Tokyo"),
    ("What is 6 * 7?", "42"),
    ("What color do you get mixing red and blue?", "Purple"),
    ("How many days in a week?", "7"),
    ("What is the smallest prime number?", "2"),
    ("What is the capital of Italy?", "Rome"),
    ("What is 8 + 5?", "13"),
    ("How many continents are there?", "7"),
    ("What is 9 * 4?", "36"),
    ("What is the capital of Spain?", "Madrid"),
    ("What is 15 - 8?", "7"),
    ("What gas do plants absorb?", "Carbon dioxide"),
    ("What is 12 / 3?", "4"),
    ("What is the fastest land animal?", "Cheetah"),
    ("What is 7 + 6?", "13"),
    ("How many sides does a triangle have?", "3"),
    ("What is the capital of Germany?", "Berlin"),
    ("What is 4 * 8?", "32"),
    ("What ocean is the largest?", "Pacific"),
    ("What is 20 - 12?", "8")
]

num_questions = int(input(f"How many questions do you want? (1-{len(questions)}): "))
selected_questions = random.sample(questions, min(num_questions, len(questions)))

score = 0
for question, answer in selected_questions:
    user_answer = input(f"{question} ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer is {answer}")

print(f"Your score: {score}/{len(selected_questions)}")