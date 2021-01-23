def check_parentheses(str) ->bool :
    l = []

    for s in str:
        if s == '(' or s == '{' or s == '[':
            l.append(s)
        else:
            if s == ')' and (not len(l) or l.pop() != '('):
                return False
            elif s == '}' and (not len(l) or l.pop() != '{'):
                return False
            elif s == ']' and (not len(l) or l.pop() != '['):
                return False

    return False if len(l) else True


print(check_parentheses(')'))



