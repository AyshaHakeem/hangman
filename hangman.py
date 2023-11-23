from random import choice
import string

MAX_INCORRECT_GUESSES = 6

def select_word():
    with open('words.txt', mode ='r') as words:
        list = words.readlines()
    return choice(list).strip()
    
def get_player_input(guessed_letters):
    while True:
        player_input = input("Guess a letter: ").lower()
        if _validate_input(player_input, guessed_letters):
            return player_input


def _validate_input(player_input, guessed_letters):
    return (
        len(player_input) == 1 and
        player_input in string.ascii_lowercase and
        player_input not in guessed_letters      
    )

def join_guessed_letters(guessed_letters):
    return " ".join(sorted(guessed_letters))

def build_guessed_word(guessed_letters, target_word):
    current_letters = []
    for letter in guessed_letters:
        if letter in target_word:
            current_letters.append(letter)
        else:
            current_letters.append('_')
    
    return " ".join(current_letters)

# hangman.py
# ...

def draw_hanged_man(wrong_guesses):
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[wrong_guesses])

def game_over(target_word, guessed_letters, wrong_guesses):
    return (
        wrong_guesses == MAX_INCORRECT_GUESSES
        or set(target_word) <= guessed_letters
    )

def start_game():
    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(guessed_letters, target_word)
    wrong_guesses = 0

    while not game_over(target_word, guessed_letters, wrong_guesses):
        draw_hanged_man(wrong_guesses)
        print(f"Your guessed word is: {guessed_word}")
        print(f"Guessed Letters: {join_guessed_letters(guessed_letters)}")
        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            print("Great guess!")
        else:
            print("Sorry, it's not there.")
            wrong_guesses += 1
        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

    if wrong_guesses == MAX_INCORRECT_GUESSES:
        print("Sorry, you lost!")
    else:
        print("Congrats! You did it!")
    print(f"Your word was: {target_word}")

if __name__ == '__main__':
    start_game()