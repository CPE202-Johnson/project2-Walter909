from stack_array import Stack
# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    #Create stack
    s = Stack(20)
    tokens = input_str.split( )
    operators = ['+', '-', '*', '/', '**', '<<', '>>']
    if input_str == '':
        return ''
    #Go through stack
    for char in tokens:
        if char in operators:
            try:
                n2 = s.pop()
                n1 = s.pop()
            except IndexError:
                raise PostfixFormatException('Insufficient operands')
            if char == '+':
                result = n1 + n2
                s.push(result)
            if char == '-':
                result = n1 - n2
                s.push(result)
            if char == '*':
                result = n1 * n2
                s.push(result)
            if char == '/':
                if n2 == 0:
                    raise ValueError('Cannot divide by 0!')
                result = n1 / n2
                s.push(result)
            if char == '**':
                result = n1 ** n2
                s.push(result)
            if char == '<<':
                if type(n1) == float or type(n2) == float:
                    raise PostfixFormatException('Illegal bit shift operand')
                result = n1 << n2
                s.push(result)
            if char == '>>':
                if type(n1) == float or type(n2) == float:
                    raise PostfixFormatException('Illegal bit shift operand')
                result = n1 >> n2
                s.push(result)
        elif char.lstrip('-').replace('.','',1).isdigit():
            if '.' not in char:
                s.push(int(char))
            else:
                s.push(float(char))
        else:
            raise PostfixFormatException('Invalid token')
    final = s.pop()
    if not s.is_empty():
        raise PostfixFormatException('Too many operands')
    return final

def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    s = Stack(20)
    tokens = input_str.split( )
    i = len(tokens) - 1
    operators = ['+','-','*','/','<<','>>','**']
    if input_str == '':
        return ''
    while i >= 0:
        char = tokens[i]
        if char.lstrip('-').replace('.','',1).isdigit():
            s.push(char)
            i -= 1
        elif char in operators:
            op1 = s.pop()
            op2 = s.pop()
            inf = op1 + ' ' + op2 + ' ' + char
            s.push(inf)
            i -= 1
        else:
            break
    return s.pop()


