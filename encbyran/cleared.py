from string import punctuation


def cleared(word: str) -> str:
    """
    :param word: The word that needs to be cleared of punctuation characters at the edges.

    :return: A word without punctuation characters at the edges.
    """
    for sym in (word[0], word[-1]):
        if sym in punctuation:
            word = word.replace(sym, '')

    return word
