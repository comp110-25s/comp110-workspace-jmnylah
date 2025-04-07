"""My Wordle Game"""

__author__: str = "730665624"


def contains_char(answer: str, letter_checker: str) -> bool:
    """Is your character in my word?"""
    assert (
        len(letter_checker) == 1
    ), f"len( ' {letter_checker} ' ) is not 1"  # Is your input one character?
    idx: int = 0
    while idx < len(
        answer
    ):  # Will keep checking if your character is in our word until we get to the end
        if (
            answer[idx] == letter_checker
        ):  # Checks to see if the chracters are the same at a specfic index
            return True
        else:
            idx = idx + 1  # How we are able to check the next character
    return False


def emojified(guess: str, secret: str) -> str:
    """Is your guess correct?"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    idx: int = 0
    result: str = ""  # This is what our emojies will be added to
    while idx < len(
        guess
    ):  # Adds emojies to our empty string until we have checked ever character
        if (
            guess[idx] == secret[idx]
        ):  # Check to see if a charcter is in the same spot in our guess and secret
            result += GREEN_BOX
        elif contains_char(
            secret, guess[idx]
        ):  # Check to see if your character is any where in our secret word
            result += YELLOW_BOX
        else:  # Indicates your character is not in our secret word
            result += WHITE_BOX
        idx = idx + 1  # How we are able to check the next character
    return result


WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def input_guess(guess_length: int) -> str:
    result: str = input("Enter a " + str(guess_length) + " character word:")
    while guess_length != len(
        result
    ):  # Will run until the length of your guess matches the length of our secret word
        result: str = input("That wasn't " + str(guess_length) + " chars! Try again:")
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    round: int = 1
    while round <= 6:  # This loop shows how each attempt will work
        print("=== Turn " + str(round) + "/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        round += 1
        if guess == secret:  # How you tell the player they won the game
            print("You won in in " + str(round) + "/6 turns!")
            return None
        elif round > 6:  # How to tell the player they lost the game
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")  # The secret word
