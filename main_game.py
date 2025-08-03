# main_game.py

import quiz_questions

def quiz_game():
    score = 0
    print("\nWelcome to the Quiz Game!\n")

    score += quiz_questions.question1()
    score += quiz_questions.question2()
    score += quiz_questions.question3()

    print(f"\nGame Over! Your final is : {score}/3")

# Start the game
if __name__ == "__main__":
    quiz_game()
    