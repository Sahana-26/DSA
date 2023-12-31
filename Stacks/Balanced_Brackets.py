def isBalanced(expr):
    stack = []
    
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char=stack.pop()
            if current_char == '(':
                if char != ')':
                    return False
            if current_char == '{':
                if char != '}':
                    return False
            if current_char == '[':
                if char != ']':
                    return False
    if stack:
        print("not balanced")
    else:
        print("balanced")

expr = '[(())]'
x=isBalanced(expr)
print(x)
