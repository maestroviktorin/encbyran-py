"""
These are technical lists of random letter combinations
that define `plus` or `minus` operation applied to the ASCII letter number.
"""

from string import ascii_letters
from random import choice, randint

from config import length, amount_of_words

action_plus = {''.join(word) for word in (tuple(choice(ascii_letters) for _ in range(randint(*length))) for _ in range(amount_of_words))}
action_minus = {''.join(word) for word in (tuple(choice(ascii_letters) for _ in range(randint(*length))) for _ in range(amount_of_words))}

action_plus, action_minus = tuple(action_plus - action_minus), tuple(action_minus - action_plus)
