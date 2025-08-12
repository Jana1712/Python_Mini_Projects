questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the color of the sky?": "Blue"
}

def quiz_game():
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            score += 1
    print(f"Your score is {score}/{len(questions)}")


quiz_game()


# Output

What is the capital of France? paris
What is 2 + 2? 4
What is the color of the sky? red
Your score is 2/3

