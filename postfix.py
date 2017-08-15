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


def evaluatePostfix(postfix):
    def calculate(first, second, operator):
        if operator == '/':
            return first / second
        elif operator == '*':
            return first * second
        elif operator == '+':
            return first + second
        elif operator == '-':
            return first - second
        else:
            raise StandardError('Unknown operator in expression')

    valid_operands = ascii_uppercase + digits
    operands = []
    operators = {'/', '*', '+', '-'}
    for ch in postfix:
        if ch in valid_operands:
            operands.append(ch)
        elif ch in operators:
            secondOperand = operands.pop()
            firstOperand = operands.pop()
            # result = calculate(firstOperand, secondOperand, ch) # In case of evaluating expression with digits
            result = '(' + firstOperand + ch + secondOperand + ')'
            operands.append(result)

    return operands.pop()


if __name__ == '__main__':
    assert infixToPostfix('(A+B)*C') == 'AB+C*'
    assert infixToPostfix('A+B*C') == 'ABC*+'
    assert infixToPostfix('(A+B)*(C+D)') == 'AB+CD+*'

    assert evaluatePostfix('78+32+/') == '((7+8)/(3+2))'
