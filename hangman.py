import os
import time
import random

def print_end(win):
    count = 1
    if not win:
        while True:
            print(end_gallows[count%4])
            print(f"FAILURE\n\nResult was: {goal_word}")

            time.sleep(.075)
            count+=1
            os.system('cls' if os.name == 'nt' else 'clear')
    else:
        while True:
            print(end_gallows[count%4 +4])
            # print(f"{end_gallows[4]}\n")
            print(f"\n{'_'.join(results)}!!!\n\nWINNER!!!")
            time.sleep(.075)
            count+=1
            os.system('cls' if os.name == 'nt' else 'clear')


def get_word():
    with open("hangman_words.txt", "r") as readfile:
        word_list = readfile.read().split(", ")
    return random.choice(word_list).upper()


end_gallows = [
        """
   _____
  |    \\|
\\_O_    |
  |_\\   |
_/  \\   |
        |
-----------
""",
        """
   _____
  |    \\|
\\_O_    |
 _| \\   |
/ |_    |
        |
-----------
""",
"""
   _____
  |    \\|
 _O_/   |
/_|     |
/ |_    |
        |
-----------
""",
"""
   _____
  |    \\|
 _O_/   |
/ |_    |
_/  \\   |
        |
-----------
""",
    """
   _____
  |    \\|
        |
        |
        |      \\
        |       \\O_/
-----------      |
           |    / \\
""",
    """
   _____
  |    \\|
        |
        |
        |
        |      \\_O_/
-----------      |
           |    / \\
""",
    """
   _____
  |    \\|
        |
        |
        |          /
        |      \\_O/
-----------      |
           |    / \\
""",
    """
   _____
  |    \\|
        |
        |
        |      \\   /
        |       \\O/
-----------      |
           |    / \\
""",
    ]

gallows = [
    """
   _____
  |    \\|
        |
        |
        |
        |
-----------
""",
"""
   _____
  |    \\|
  O     |
        |
        |
        |
-----------
""",
"""
   _____
  |    \\|
  O     |
  |     |
        |
        |
-----------
""",
# """
#    _____
#   |    \\|
#   O     |
#   |\\    |
#         |
#         |
# -----------
# """,
# """
#    _____
#   |    \\|
#   O     |
#  /|\\    |
#         |
#         |
# -----------
# """,
# """
#    _____
#   |    \\|
#   O     |
#  /|\\    |
#    \\    |
#         |
# -----------
# """,
# """
#    _____
#   |    \\|
#   O     |
#  /|\\    |
#  / \\    |
#         |
# -----------
# """
# Easy / Hard
"""
   _____
  |    \\|
  O_    |
  |     |
        |
        |
-----------
""",
"""
   _____
  |    \\|
  O_    |
  | \\   |
        |
        |
-----------
""",
"""
   _____
  |    \\|
 _O_    |
  | \\   |
        |
        |
-----------
""",
"""
   _____
  |    \\|
\\_O_    |
  | \\   |
        |
        |
-----------
""",

"""
   _____
  |    \\|
\\_O_    |
  |_\\   |
        |
        |
-----------
""",
"""
   _____
  |    \\|
\\_O_    |
  |_\\   |
    \\   |
        |
-----------
""",
"""
   _____
  |    \\|
\\_O_    |
  |_\\   |
  | \\   |
        |
-----------
""",
"""
   _____
  |    \\|
\\_O_    |
  |_\\   |
 _| \\   |
        |
-----------
""",
]

os.system('printf "\e[8;24;80t"')
os.system('cls' if os.name == 'nt' else 'clear')

goal_word = "PYTHON"
# goal_word = "MISSILE"
# goal_word = get_word()

results = ["_" for _ in goal_word]

correct_guesses = ''
incorrect_guesses = ''

body_parts = 0
max_body_parts = 10

while True:
    user_input = input("Give me a letter: ").upper()


    if user_input in incorrect_guesses or user_input in correct_guesses:
        print(f"Already guessed {user_input}")
        continue
    if len(user_input) > 1 or not user_input.isalpha():
        print("Enter a valid single letter response.")
        continue
    os.system('cls' if os.name == 'nt' else 'clear')

    if user_input in goal_word:
        correct_guesses += user_input
        char_index_list = [index for index, char in enumerate(goal_word) if char == user_input]
        for idx in char_index_list: results[idx] = user_input

        if '_' not in results:
            print_end(True)
            break

    else:
        incorrect_guesses += user_input
        body_parts += 1
        if body_parts == max_body_parts:
            print_end(False)
            break
    print(gallows[body_parts])
    print(f"{''.join(results)}\n")
    print(f"Incorrect Guesses({body_parts}/{max_body_parts}): {incorrect_guesses}\n")