import random

score = []

def highscore():
    if len(score) == 0:
        print()
    else:
        print("\nThe HIGHSCORE IS {}".format(min(score)))


def start_game():
    attempt_count = 1
    ANSWER = random.randint(1, 10)
    print("\n>>>>>>>> Welcome to the Number Guessing Game <<<<<<<<\n")

    game_running = True
    while game_running:
        try:
            number = int(input("Pick a number between 1 and 10: "))
        except ValueError as err:
            print("That value is not one of the options :(, try again...")
            attempt_count += 1
        else:
            if number not in range(1, 11):
                print("That value is not one of the options :(, try again...")
                attempt_count += 1
            elif number < ANSWER:
                print("Not the right one. A clue: It is higher!")
                attempt_count += 1
            elif number > ANSWER:
                print("Not the right one. A clue: It is lower!")
                attempt_count += 1
            else:
                print("\nYou got it in just {} tries!".format(attempt_count))
                again = input("would you like to play again? y/n: ")
                score.append(attempt_count)
                highscore()
                if again.lower() == "y":
                    start_game()
                else:
                    print("\nThank you for playing The Number Guessing Game, See you soon!")
                game_running = False

if __name__ == '__main__':
    start_game()
