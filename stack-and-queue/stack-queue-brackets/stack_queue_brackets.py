from stack.stack import Stack

# brackets = "}[]{hi(})"
brackets = "([tow]{})"

def validate_brackets(brackets_str):
    """
    Checks if the brackets in a string are balanced and properly nested.

    Args:
        brackets_str (str): The string containing brackets to validate.

    Returns:
        bool: True if the brackets are balanced and properly nested, False otherwise.
    """
    brackets = {"(": ")", "{": "}", "[": "]"}
    stack = Stack()

    for char in brackets_str:
        if char in brackets.keys():
            stack.push(char)
        elif char in brackets.values():
            if not stack or char != brackets[stack.pop()]:
                return False

    if stack.is_empty():
      return True 
    else: return False
        

print(validate_brackets(brackets))