def isValid(s: str) -> bool:
    chars = []
    opens = ['(', '[', '{']
    closes = [')', '}', ']']
    for i in range(len(s)):
        if s[i] in opens:
            chars.append(s[i])
        if len(chars) == 0 and s[i] in closes:
            return False
        if len(chars) > 0 and s[i] in closes:
            conditions = chars[-1] == '(' and s[i] == ')' or chars[-1] == '[' and s[i] == ']' or chars[-1] == '{' and s[i] == '}'
            if conditions:
                chars.pop()
            else:
                return False
    if len(chars) == 0:
        return True
    else:
        return False

print(isValid('[[(())]]'))
