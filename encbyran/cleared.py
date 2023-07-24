from string import punctuation


def cleared(word: str) -> str:
    """
    ### Parameters

    `word`: The word that needs to be cleared of punctuation characters at the edges.

    ### Returns

    Word without punctuation characters at the edges.
    """
    for sym in (word[0], word[-1]):
        if sym in punctuation:
            word = word.replace(sym, '')

    return word
