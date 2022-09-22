import stack

operators = '+-*/()'

def eval_infix(expression):
    inp = expression.split()
    numStack = stack.Stack()
    opStack = stack.Stack()
    opStack.push('(')
    
    for token in inp:
        if token in operators:
            operate(token, opStack, numStack)
        else:
            numStack.push(float(token))
            
    operate(')', opStack, numStack)
    
    return numStack.pop()

def precedence(char):
    if char == '(' or char == ')':
        return 0
    if char == '+' or char == '-':
        return 1
    if char == '*' or char =='/':
        return 2
    
def operate(operator, opStack, numStack):
    if operator == '(':
        opStack.push(operator)
        return
    while precedence(operator) <= precedence(opStack.top()):
        topOp = opStack.pop()
        if topOp == '+':
            first = numStack.pop()
            sec = numStack.pop()
            numStack.push(first + sec)
        if topOp == '-':
            first = numStack.pop()
            sec = numStack.pop()
            numStack.push(sec - first)
        if topOp == '*':
            first = numStack.pop()
            sec = numStack.pop()
            numStack.push(sec * first)      
        if topOp == '/':
            first = numStack.pop()
            sec = numStack.pop()
            numStack.push(sec / first)
        if topOp == '(':
            return
        
    if precedence(operator) > precedence(opStack.top()):
        opStack.push(operator)
        return
    
    
def main():
    expr = input("Enter an infix expression to evaluate: ")
    result = eval_infix(expr)
    print("The result of evaluating", expr,"is", result)
    
    
if __name__ == "__main__":
    main()