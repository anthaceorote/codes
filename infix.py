from string import ascii_uppercase, digits


def infixToPostfix(infix):
    precedence = {'/': 4, '*': 3, '+': 2, '-': 2, '(': 1}
    operators = []
    postfix = []
    valid_operands = ascii_uppercase + digits

    for ch in infix:
        if ch in valid_operands:
            postfix.append(ch)
        elif ch == '(':
            operators.append(ch)
        elif ch == ')':
            top = operators.pop()
            while top != '(':
                postfix.append(top)
                top = operators.pop()
        else:
            while operators and precedence[operators[-1]] >= precedence[ch]:
                postfix.append(operators.pop())
            operators.append(ch)
    while operators:
        postfix.append(operators.pop())

    return ''.join(postfix)


def infixToPrefix(infix):
    rev_infix = infix[::-1]

    rev_infix = rev_infix.replace(')', '@')
    rev_infix = rev_infix.replace('(', ')')
    rev_infix = rev_infix.replace('@', '(')

    prefix = infixToPostfix(rev_infix)[::-1]

    return prefix


if __name__ == '__main__':
    assert infixToPrefix('(A+B)*C') == '*+ABC'
    assert infixToPrefix('A+B*C') == '+A*BC'
    assert infixToPrefix('(A+B)*(C+D)') == '*+AB+CD'

    assert infixToPrefix('A*B*C*D+E+F') == '+*A*B*CD+EF'
    assert infixToPrefix('A+((B+C)*(D+E))') == '+A*+BC+DE'
    assert infixToPrefix('(A+B)*(C+D)*(E+F)') == '*+AB*+CD+EF'
