"""
These are technical lists of random letter combinations
that define `plus` or `minus` operation applied to the ASCII letter number.
"""

from random import choice, randint
from string import ascii_letters

from config import length, amount_of_words


def get_random_set() -> set[str]:
    return {''.join(word) for word in
            (tuple(choice(ascii_letters) for _ in range(randint(*length))) for _ in range(amount_of_words))}


action_plus = get_random_set()
action_minus = get_random_set()
new_line = get_random_set()

# Excluding all the common elements.
action_plus, action_minus, new_line = \
    action_plus - action_minus - new_line, action_minus - \
    action_plus - new_line, new_line - action_plus - action_minus
