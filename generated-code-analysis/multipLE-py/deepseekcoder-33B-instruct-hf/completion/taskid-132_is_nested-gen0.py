def is_nested(string: str) -> bool:
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    >>> is_nested('[[]]')
    True
    >>> is_nested('[]]]]]]][[[[[]')
    False
    >>> is_nested('[][]')
    False
    >>> is_nested('[]')
    False
    >>> is_nested('[[][]]')
    True
    >>> is_nested('[[]][[')
    True
    """


    # Define a stack
    stack = []

    # Traverse through the string
    for bracket in string:
        if bracket == "[":
            # Push the bracket to the stack
            stack.append(bracket)
        else:
            # If the current bracket is a closing bracket, check if the stack is not empty and the top element of the stack is an opening bracket
            if len(stack) > 0 and stack[-1] == "[":
                # Pop the top element of the stack
                stack.pop()
            else:
                return True
    
    return False
