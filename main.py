import random


def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = [line.strip().split(';') for line in file if line.strip()]
    return questions


def save_result(file_path, player_name, score, total):
    with open(file_path, 'a') as file:
        file.write(f"{player_name} scored {score}/{total}\n")


def math_quiz():
    questions = load_questions('questions.txt')
    if not questions:
        return

    player_name = input("Enter your name: ")
    num_questions = int(input("Enter the number of questions: "))
    selected_questions = random.sample(questions, min(num_questions, len(questions)))

    score = 0
    for q in selected_questions:
        print(f"Question: {q[0]}")
        print(f"A. {q[1]}  B. {q[2]}  C. {q[3]}  D. {q[4]}")
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q[5]:
            score += 1

    print(f"Your score: {score}/{len(selected_questions)}")
    save_result('data.txt', player_name, score, len(selected_questions))


if __name__ == "__main__":
    math_quiz()
