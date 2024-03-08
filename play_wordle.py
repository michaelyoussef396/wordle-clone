from wordle import Wordle


def main():
    print("Hello Wordle!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:  # Use the instance property, not the class property.
        guess = input("Type your guess: ").strip()
        wordle.attempt(guess)  # This is correct and should be used.

        if wordle.is_solved:
            print("You won!")
            break
        elif wordle.remaining_attempts == 0:
            print("You've run out of attempts!")
            break
        else:
            print(
                f"Guess again. You have {wordle.remaining_attempts} attempts left.")

    if not wordle.is_solved:
        print(f"The correct word was: {wordle.secret}")


if __name__ == "__main__":
    main()
