def is_valid(s: str) -> bool:
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c == ')' and (not stack or stack[-1] != '('):
            return False
        elif c == ']' and (not stack or stack[-1] != '['):
            return False
        elif c == '}' and (not stack or stack[-1] != '{'):
            return False
        else:
            stack.pop()
    return not stack
