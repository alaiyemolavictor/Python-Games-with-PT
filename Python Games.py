def quiz_game():
    score = 0

    # Question 1
    print("1. Enter a number that is divisible by 5.")
    answer1 = input("Your answer: ")
    try:
        if int(answer1) % 5 == 0:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The number is not divisible by 5.")
    except ValueError:
        print("That's not a valid number.")

    # Question 2
    print("\n2. What has an eye but cannot see?")
    answer2 = input("Your answer: ").strip().lower()
    if "needle" in answer2:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The answer is a needle.")

    # Question 3
    print("\n3. George Washington died in 1800 and dinosaurs were discovered in 1800 or 1820. True or False?")
    answer3 = input("Your answer (true/false): ").strip().lower()
    if answer3 == "false":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is False.")

    # Final Score
    print(f"\nGame Over! Your final score is: {score}/3")

# Run the quiz game
quiz_game()
