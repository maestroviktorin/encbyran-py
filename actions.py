"""
These are technical lists of special words necessary for the execution of the encrypting and decrypting.
You can edit the lists for more secure encryption.

The lists can contain words or letter combinations of ONLY 4 characters.
"""

action_plus = ['skin', 'when', 'bull', 'sorb', 'rock', 'cake', 'home', 'bush', 'back', 'fire']  # default config
action_minus = ['bath', 'fish', 'deer', 'feel', 'hurt', 'mark', 'cold', 'unit', 'buck', 'coal']  # default config

# Insurance against extra characters
action_plus = list(map(lambda x: x[:4], action_plus))
action_minus = list(map(lambda x: x[:4], action_minus))
