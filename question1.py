def is_balanced(string):
    # Stack to keep track of opening brackets
    bracket_stack = []
    # Dictionary to map opening brackets to their corresponding closing brackets
    brackets = {"(": ")", "[": "]", "{": "}"}

    # Iterate through each character in the input string
    for char in string:
        # If the character is a closing bracket
        if char in brackets.values():
            # Push it onto the stack
            bracket_stack.append(char)
        # If the character is an opening bracket
        elif char in brackets.keys():
            # Check if the stack is empty or if the top of the stack matches the current closing bracket
            if not bracket_stack or brackets[bracket_stack.pop()] != char:
                # If not, the expression is not balanced
                return False

    # If the stack is empty, the expression is balanced
    return not bracket_stack


expression1 = "([]{})"
expression2 = "([)]"

print("Expression 1 is balanced: ", is_balanced(expression1))
print("Expression 2 is balanced: ", is_balanced(expression2)) 