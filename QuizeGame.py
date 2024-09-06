questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2+2?", "answer": "4"},
    {"question":" Who invented the Python programming laungauge?","answer": "guido van rossum"},
    {"question": "Which programming paradigm emphasizes encapsulation, inheritance, and polymorphism?", "answer":"oops"}
]
score = 0
for question in questions:
    user_answer = input(question["question"] + " ")
    if user_answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
print(f"Final score: {score}/{len(questions)}")