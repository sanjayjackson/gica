import json

questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "choices": ["A. Oxygen", "B. Gold", "C. Silver", "D. Helium"],
        "answer": "A"
    }
]

def run_quiz(questions):
    score = 0

    for idx, q in enumerate(questions, 1):
        print(f"Question {idx}: {q['question']}")
        for choice in q['choices']:
            print(choice)

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    print("Welcome to the Quiz!\n")
    run_quiz(questions)
