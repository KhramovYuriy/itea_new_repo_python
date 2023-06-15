import random

def get_random_answer():
    answers = ["так", "ні", "можливо"]
    return random.choice(answers)

def main():
    while True:
        question = input("Задайте ваше питання (або введіть 'вийти' для завершення): ")
        if question.lower() == "вийти":
            break
        answer = get_random_answer()
        print("Відповідь:", answer)

if __name__ == "__main__":
    main()