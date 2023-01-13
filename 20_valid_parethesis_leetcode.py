def isValid(s: str) -> bool:
    a = {'}': '{',')': '(', ']': '['}
    c = ''
    for _ in s:
        if _ in '({[':
            c = f"{c}{_}"
        else:
            if not len(c) or a[_] != c[-1]:
                return False
            else:
                c=c[:-1]        
    return not len(c)

print(isValid("()[]{}"))
