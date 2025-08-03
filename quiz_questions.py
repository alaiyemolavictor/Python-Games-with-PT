# quiz_questions.py

def question1():
    while True:
        try:
            answer = int(input("1. Enter a number that is divisible by 5: "))
            if answer % 5 == 0:
                print("Correct!")
                return 1
            else:
                print("Incorrect. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def question2():
    while True:
        answer = input("2. What has an eye but cannot see? ").strip().lower()
        if "needle" in answer:
            print("Correct!")
            return 1
        else:
            print("Incorrect. Try again.")


def question3():
    while True:
        answer = input("3. George Washington died in 1800 and dinosaurs were discovered in 1800 or 1820. true or False? ").strip().lower()
        if answer == "false":
            print("Correct!")
            return 1
        else:
            print("Incorrect. Try again.")