# quiz_app.py

def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. Berlin", "C. Madrid", "D. Rome"],
            "answer": "A"
        },
        {
            "question": "Which data type is used to store text in Python?",
            "options": ["A. int", "B. str", "C. float", "D. bool"],
            "answer": "B"
        },
        {
            "question": "What keyword is used to define a function in Python?",
            "options": ["A. func", "B. function", "C. def", "D. define"],
            "answer": "C"
        },
        {
            "question": "Which operator is used for exponentiation in Python?",
            "options": ["A. ^", "B. **", "C. //", "D. %"],
            "answer": "B"
        },
        {
            "question": "Which of the following is a mutable data type in Python?",
            "options": ["A. Tuple", "B. String", "C. List", "D. Integer"],
            "answer": "C"
        },
        {
            "question": "Which built-in function returns the length of a list?",
            "options": ["A. count()", "B. size()", "C. length()", "D. len()"],
            "answer": "D"
        },
        {
            "question": "What is the output of: print(2 == 2.0)?",
            "options": ["A. False", "B. True", "C. Error", "D. None"],
            "answer": "B"
        },
        {
            "question": "Which keyword is used to create a class in Python?",
            "options": ["A. object", "B. define", "C. class", "D. struct"],
            "answer": "C"
        },
        {
            "question": "Which symbol is used to start a comment in Python?",
            "options": ["A. //", "B. /*", "C. #", "D. <!--"],
            "answer": "C"
        },
        {
            "question": "Which of these is used to handle exceptions in Python?",
            "options": ["A. try-except", "B. do-catch", "C. if-else", "D. switch-case"],
            "answer": "A"
        }
    ]

    score = 0

    print("Welcome to the Python Quiz!\n")

    for idx, q in enumerate(questions, 1):
        print(f"Q{idx}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    print(f"🎉 Quiz Completed! Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    run_quiz()
