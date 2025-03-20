def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    balance = 0

    for char in parens:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        
        # If balance goes negative, there's an unmatched closing parenthesis
        if balance < 0:
            return False

    # The string is valid only if the final balance is zero
    return balance == 0