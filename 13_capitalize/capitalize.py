def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

    >>> capitalize('python')
    'Python'

    >>> capitalize('only first word')
    'Only first word'
    """
    if not phrase:
        # Return empty string if phrase is empty
        return phrase

    # Split only the first word
    words = phrase.split(" ", 1)
    # Capitalize the first word
    words[0] = words[0].capitalize()

    # Rejoin the words back into a phrase
    return " ".join(words)
